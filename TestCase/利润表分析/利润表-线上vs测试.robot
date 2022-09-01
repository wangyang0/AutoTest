*** Settings ***
Suite Setup       登录获取cookie    ${CompanyName}    ${UserName}    ${Password}
Resource          ../../UserKeywords/智库模块.robot
Resource          ../../UserKeywords/通用模块.robot
Resource          ../../UserVariable/智库模块.robot
Library           String

*** Test Cases ***
店铺利润表-线上vs测试
    #获取时间戳
    ${date}    前7天
    ${date_start}    Set Variable    ${date[0]}    #获取开始时间
    ${date_end}    Set Variable    ${date[1]}    #获取结束时间
    #获取店铺id
    ${shoplist}    店铺列表    ${cookie}
    ${shopUniIds}    Evaluate    random.choice(${shoplist})    random
    ${shopid}    Set Variable    ${shopUniIds[0]}
    #获取科目列表
    ${categoryType}    Set Variable    shop
    ${categorylist}    科目列表    ${cookie}    ${categoryType}
    #获取取值规则
    ${ruleId}    获取规则    ${cookie}
    #测试环境店铺利润表接口
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shopid}&timeOrderType=asc&showDimension=0&ruleId=${ruleId}&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true    None
    ${res_1}    To Json    ${response}
    #线上测试环境店铺利润表接口
    ${response}    发送请求    ${cookie}    ${domain2}/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shopid}&timeOrderType=asc&showDimension=0&ruleId=${ruleId}&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true \    None
    ${res_2}    To Json    ${response}
    店铺利润表对比    ${res_1}    ${res_2}    ${categorylist}

汇总利润表-线上vs测试
    #获取时间戳
    ${date}    前7天
    ${date_start}    Set Variable    ${date[0]}    #获取开始时间
    ${date_end}    Set Variable    ${date[1]}    #获取结束时间
    #获取科目列表
    ${categoryType}    Set Variable    total
    ${categorylist}    科目列表    ${cookie}    ${categoryType}
    #获取取值规则
    ${ruleId}    获取规则    ${cookie}
    #获取店铺id
    ${shoplist}    店铺列表    ${cookie}
    FOR    ${shopUniIds}    IN    @{shoplist}
        log    ${shopUniIds[0]}
        ${shopid}    Set Variable    ${shopUniIds[0]}
    #测试环境店铺利润表接口
        ${response}    发送请求    ${cookie}    ${domain}/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shopid}&timeOrderType=asc&showDimension=0&ruleId=${ruleId}&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true    None
        ${res_1}    To Json    ${response}
    #线上测试环境店铺利润表接口
        ${response}    发送请求    ${cookie}    ${domain2}/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shopid}&timeOrderType=asc&showDimension=0&ruleId=${ruleId}&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true \    None
        ${res_2}    To Json    ${response}
        店铺利润表对比    ${res_1}    ${res_2}    ${categorylist}
    END

链接利润表-线上vs测试
    #获取时间戳
    ${date}    前7天
    ${date_start}    Set Variable    ${date[0]}    #获取开始时间
    ${date_end}    Set Variable    ${date[1]}    #获取结束时间
    #获取店铺id
    ${shoplist}    店铺列表    ${cookie}
    ${shopUniIds}    Evaluate    random.choice(${shoplist})    random
    ${shopid}    Set Variable    ${shopUniIds[0]}
    #获取取值规则
    ${ruleId}    获取规则    ${cookie}
    #获取连接利润表展示科目
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/profit/support/title/link?api_name=kmzk_profit_support_title_link    None
    ${title_link}    Set Variable    ${response}
    #连接利润表测试
    ${param}    Set Variable    api_name=kmzk_profit_report_link&querySnapshot=false&pageNo=1&pageSize=20&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shopid}&itemId=&keyWord=&ruleId=${ruleId}&showSuit=1&isProfit=&needSummary=1
    ${res1}    发送请求    ${cookie}    ${domain}/kmzk/profit/report/link    ${param}
    #连接利润表测试
    ${param}    Set Variable    api_name=kmzk_profit_report_link&querySnapshot=false&pageNo=1&pageSize=20&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shopid}&itemId=&keyWord=&ruleId=${ruleId}&showSuit=1&isProfit=&needSummary=1
    ${res2}    发送请求    ${cookie}    ${domain2}/kmzk/profit/report/link    ${param}
    #连接利润表对比
    链接利润表总计对比    ${res1}    ${res2}    ${title_link}
    链接利润表id对比    ${res1}    ${res2}    ${title_link}

链接利润表明细-线上vs测试
    #获取时间戳
    ${date}    前7天
    ${date_start}    Set Variable    ${date[0]}    #获取开始时间
    ${date_end}    Set Variable    ${date[1]}    #获取结束时间
    #获取科目列表
    ${categoryType}    Set Variable    link
    ${categorylist}    科目列表    ${cookie}    ${categoryType}
    #获取店铺id
    ${shoplist}    店铺列表    ${cookie}
    ${shopUniIds}    Evaluate    random.choice(${shoplist})    random
    ${shopid}    Set Variable    ${shopUniIds[0]}
    ${shop_id}    Set Variable    37741_88387
    #测试环境链接利润表接口
    ${itemId}    Set Variable    475365573059072
    ${param}    Set Variable    api_name=kmzk_profit_report_linkDetail&shopUniIds=${shop_id}&itemId=${itemId}&sysStatus=1&startTime=${date_start}&endTime=${date_end}
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/profit/report/linkDetail    ${param}
    ${res_1}    To Json    ${response}
    #线上环境链接利润表接口
    ${param}    Set Variable    api_name=kmzk_profit_report_linkDetail&shopUniIds=${shop_id}&itemId=${itemId}&sysStatus=1&startTime=${date_start}&endTime=${date_end}
    ${response}    发送请求    ${cookie}    ${domain2}/kmzk/profit/report/linkDetail    ${param}
    ${res_2}    To Json    ${response}
    店铺利润表对比    ${res_1}    ${res_2}    ${categorylist}

订单利润表-线上vs测试
    #获取时间戳
    ${date}    前7天
    ${date_start}    Set Variable    ${date[0]}    #获取开始时间
    ${date_end}    Set Variable    ${date[1]}    #获取结束时间
    #获取取值规则
    ${ruleId}    获取规则    ${cookie}
    ${shop_id}    Set Variable    37741_88387
    #测试环境订单利润表接口
    ${param}    Set Variable    api_name=kmzk_profit_report_order&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shop_id}&ruleId=${ruleId}&needSummary=1
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/profit/report/order    ${param}
    ${res1}    To Json    ${response}
    #线上环境订单利润表接口
    ${param}    Set Variable    api_name=kmzk_profit_report_order&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shop_id}&ruleId=${ruleId}&needSummary=1
    ${response}    发送请求    ${cookie}    ${domain2}/kmzk/profit/report/order    ${param}
    ${res2}    To Json    ${response}
    订单利润表对比1    ${res1}    ${res2}


    订单利润表-线上vs测试
    #获取时间戳
    ${date}    前7天
    ${date_start}    Set Variable    ${date[0]}    #获取开始时间
    ${date_end}    Set Variable    ${date[1]}    #获取结束时间
    #获取取值规则
    ${ruleId}    获取规则    ${cookie}
    ${shop_id}    Set Variable    37741_88387
    #测试环境订单利润表接口
    ${param}    Set Variable    api_name=kmzk_profit_report_order&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shop_id}&ruleId=${ruleId}&needSummary=1
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/profit/report/order    ${param}
    ${res1}    To Json    ${response}
    #线上环境订单利润表接口
    ${param}    Set Variable    api_name=kmzk_profit_report_order&sysStatus=1&startTime=${date_start}&endTime=${date_end}&shopUniIds=${shop_id}&ruleId=${ruleId}&needSummary=1
    ${response}    发送请求    ${cookie}    ${domain2}/kmzk/profit/report/order    ${param}
    ${res2}    To Json    ${response}
    订单利润表对比1    ${res1}    ${res2}
