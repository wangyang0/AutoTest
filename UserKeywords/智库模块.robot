*** Settings ***
Resource          通用模块.robot
Resource          智库模块.robot
Resource          ../UserVariable/智库模块.robot
Library           ../Library/ApiLib/get_kemulist.py
Library           ../Library/ApiLib/get_shoplist.py
Library           ../Library/ApiLib/get_ruleid.py
Library           SeleniumLibrary    timeout=10
Library           String
Library           ../Library/ApiLib/compare.py

*** Keywords ***
店铺列表
    [Arguments]    ${cookie}
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/common/shopList/v2?api_name=kmzk_common_shopList_v2&platformIds=    None
    ${shop_list}    analyse_shoplist    ${response}
    [Return]    ${shop_list}

科目列表
    [Arguments]    ${cookie}    ${categoryType}
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/categoryManage/getCategoryList    api_name=kmzk_categoryManage_getCategoryList&queryContent=1&categoryType=${categoryType}
    ${kemu_list}    get_kemulist.getCategroylist    ${response}
    [Return]    ${response}

获取规则
    [Arguments]    ${cookie}
    ${response}    发送请求    ${cookie}    ${domain}/kmzk/categoryValuePlan/list/concise?api_name=kmzk_categoryValuePlan_list_concise    None
    ${ruleid}    get ruleid    ${response}
    [Return]    ${ruleid}

页面登录
    [Arguments]    ${company}    ${account}    ${passwords}
    Open Browser    https://puberp.superboss.cc/login.html    chrome
    Maximize Browser Window
    Input Text    id=login-company    ${company}
    Input Text    id=login-account    ${account}
    Input Text    id=login-password    ${passwords}
    click Button    id=login-btn
    Wait Until Element Is Enabled    xpath=//span[contains(text(),'店铺状态异常确认')]/../span[@class='el-dialog__headerbtnGroup']
    click Element    xpath=//span[contains(text(),'店铺状态异常确认')]/../span[@class='el-dialog__headerbtnGroup']
    title should be    快麦ERP--首页

店铺利润表_报表按财务-数据对比
    [Arguments]    ${res_1}    ${res_2}
    log    销售额
    Run Keyword And Continue On Failure    should be equal    ${res_1['data'][-2]['realsales']}    ${res_2['data']['amount']['saleMoney']}
    log    订单数
    Run Keyword And Continue On Failure    should be equal    ${res_1['data'][-2]['trade_num']}    ${res_2['data']['amount']['tradeCount']}
    log    商品数
    Run Keyword And Continue On Failure    should be equal    ${res_1['data'][-2]['num']}    ${res_2['data']['amount']['itemCount']}
    log    退货成本
    ${refund_cost}    Evaluate    abs(${res_1['data'][-2]['onsale_refund_cost']}+${res_1['data'][-2]['after_refund_cost']})
    Run Keyword And Continue On Failure    should be equal    ${refund_cost}    ${res_2['data']['amount']['refundItemCost']}
    log    商品成本
    Run Keyword And Continue On Failure    should be equal    ${res_1['data'][-2]['gcost']}    ${res_2['data']['amount']['itemCost']}
    log    退款
    ${refund}    Evaluate    ${res_1['data'][-2]['onsale_refund']}+${res_1['data'][-2]['after_refund']}
    Run Keyword And Continue On Failure    should be equal    ${refund}    ${res_2['data']['amount']['rawRefundMoney']}
    log    发货前退款
    Run Keyword And Continue On Failure    should be equal    ${res_1['data'][-2]['onsale_refund']}    ${res_2['data']['amount']['rawNotRefundItemMoney']}
    log    发货后退款
    Run Keyword And Continue On Failure    should be equal    ${res_1['data'][-2]['after_refund']}    ${res_2['data']['amount']['rawRefundItemMoney']}

店铺利润表对比
    [Arguments]    ${res_1}    ${res_2}    ${categorylist}
    compare.compare_shop    ${res_1}    ${res_2}    ${categorylist}

链接利润表总计对比
    [Arguments]    ${res_1}    ${res_2}    ${linktitle}
    compare.sum_copm    ${res1}    ${res2}    ${linktitle}

链接利润表id对比
    [Arguments]    ${res_1}    ${res_2}    ${linktitle}
    compare.link_comp    ${res1}    ${res2}    ${linktitle}

订单利润表对比
    [Arguments]    ${res1}    ${res2}
    ${response}    run keyword if    ${res1["data"]["totalCount"]}!=0 and ${res2["data"]["totalCount"]}!=0    compare.order_comp    ${res1['data']['summary']}    ${res2['data']['summary']}
    ...    ELSE    log    数据不同不能对比
    run keyword if    ${response}    log    数据一样
    ...    ELSE    FOR    index    IN RANGE    get length    ${res1['data']['list']}
                            log    111111111111
                        END

订单利润表对比1
    [Arguments]    ${res1}    ${res2}
    ${response}    run keyword if    ${res1["data"]["totalCount"]}!=0 and ${res2["data"]["totalCount"]}!=0    compare.order_comp    ${res1['data']['summary']}    ${res2['data']['summary']}
    ...    ELSE    log    数据不同不能对比
    run keyword if    ${response}    log    数据一样
    ...    ELSE    ${kk}    Set Variable    ${res1['data']['list']}
    ${kk}
    log    ${kk}
    FOR    ${index}    IN RANGE    get length    Evaluate    ${res1['data']['list']}
        log    ${index}
    END
