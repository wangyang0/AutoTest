*** Settings ***
Suite Setup       登录获取cookie    ${CompanyName}    ${UserName}    ${Password}
Resource          ../../UserKeywords/智库模块.robot
Resource          ../../UserKeywords/通用模块.robot
Resource          ../../UserVariable/智库模块.robot

*** Test Cases ***
测试用户-店铺利润表vs财务报表
    #获取时间戳
    ${date}    前7天
    ${date_start}    Set Variable    ${date[0]}    #获取开始时间
    ${date_end}    Set Variable    ${date[1]}    #获取结束时间
    #获取店铺id
    ${shoplist}    店铺列表    ${cookie}
    ${shopUniIds}    Evaluate    random.choice(${shoplist})    random
    ${shopUniId}    Set Variable    ${shopUniIds[0]}
    ${shopid}    shopid    ${shopUniId}
    ${sysStatus}    common.sysStatus_random
    #获取取值规则
    ${ruleId}    获取规则    ${cookie}
    #店铺利润表接口
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=${sysStatus[0]}&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shopUniId}&timeOrderType=asc&showDimension=0&ruleId=${ruleId}&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true    None
    ${res_my}    To Json    ${response}
    #快麦财务接口
    ${param_erp}    Set Variable    pageNo=1&pageSize=50&pageId=1123&queryFlag=shop&startTime=${date_start}&endTime=${date_end}&vipSign=true&sysStatus=${sysStatus[1]}&sellerFlags=&tradeTypes=&containTagIds=&exceptTagIds=&userIds=${shopid}&warehouseIds=&isAccurate=&itemFlag=0&tradeSysStatus=&scalping=&sysSkuIds=&sysItemIds=&outerIds=&cids=&brandIds=&containTradeOut=true&onlyTradeOut=false&destIds=&sourceIds=&supplyIds=&buyerNicks=&templateIds=&showProcessItemDetail=&showGroupItemDetail=&isOuterIdFuzzy=0&shipper=&queryByCake=&matchFlag=1&virtualFlag=1&showSuit=0&createdStartTime=&createdEndTime=&buyerNick=&classifyIds=&afterSaleTimeType=finish&shouldSort=false&sortField=&sortType=&api_name=report_sale_dimensions_finance_list
    ${response_erp}    发送请求    ${cookie}    ${domain}/report/sale/dimensions/finance/list    ${param_erp}
    ${res_erp}    To Json    ${response_erp}
    #断言
    店铺利润表_报表按财务-数据对比    ${res_my}    ${res_erp}
