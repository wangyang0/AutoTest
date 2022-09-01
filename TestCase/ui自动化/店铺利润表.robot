*** Settings ***
Suite Setup       页面登录    ${CompanyName}    ${UserName}    ${passwords}
Suite Teardown    Close Browser
Library           SeleniumLibrary    timeout=10
Library           Selenium2Library
Resource          ../../UserKeywords/智库模块.robot

*** Test Cases ***
通过data_id找元素
    click Element    //*[@data-id="5000"and @class="item"]
    Wait Until Element Is Enabled    //*[@data-id="5001"and @class="children-item-path"]
    click Element    //*[@data-id="5001"and @class="children-item-path"]

通过text找元素
    click Element    xpath=//span[contains(text(),'智库')]
    Wait Until Element Is Enabled    xpath=//a[contains(text(),'店铺利润表')and @class="children-item-path"]
    click Element    xpath=//a[contains(text(),'店铺利润表')and @class="children-item-path"]
    Wait Until Element Is Enabled    xpath=//*[@class='el-select__input']
    Input Text    xpath=//*[@class='el-select__input']    0901dianpuceshi
    click Element    xpath=//span[contains(text(),'计算数据')]
    Wait Until Element Is Enabled    xpath=//div[@class='el-table__body-wrapper is-scrolling-left']//span[contains(text(),'收入:合计(排除特殊单)')]
    Element Text should be    xpath=//div[@class='el-table__body-wrapper is-scrolling-left']//span[contains(text(),'收入:合计(排除特殊单)')]    收入:合计(排除特殊单)    不存在
    Element Text should be    xpath=//thead[@class='is-group has-gutter']//div[contains(text(),'0901dianpuceshi')]    0901dianpuceshi    不存在2
