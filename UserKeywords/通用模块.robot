*** Settings ***
Library           DateTime
Library           ../Library/ApiLib/last_month.py
Library           ../Library/ApiLib/common.py
Library           RequestsLibrary
Resource          ../UserVariable/智库模块.robot

*** Keywords ***
获取指定时间戳
    [Arguments]    ${day}
    #获取当前时间
    ${time}    Get Current Date    result_format=timestamp
    #获取90天前时间
    ${time_7days}    Add Time To Date    ${time}    ${day}
    log    ${time_7days}
    #当前转化为时间戳
    ${time_stamp}    Convert Date    ${time}    epoch
    ${time_stamp2}    Evaluate    int(round(${time_stamp} * 1000))
    #获取90天前的时间戳
    ${time_stamp_7days}    Convert Date    ${time_7days}    epoch
    ${time_stamp_7days2}    Evaluate    int(round(${time_stamp_7days} * 1000))
    [Return]    ${time_stamp2}    ${time_stamp_7days2}

当前时间戳
    ${time}    Get Time
    Log    ${time}
    #获取当前时间
    ${current_date}    Get_Current_Date    result_format=timestamp
    Log    ${current_date}
    #获取当前时间戳
    ${time_stamp}    Convert Date    ${current_date}    epoch
    Log    ${time_stamp}
    #转化为毫秒级时间戳
    ${time_stamp2}    Evaluate    int(round(${time_stamp}*1000))
    Log    ${time_stamp2}

昨天
    ${date}    整点时间    -1days
    log    ${date}
    ${startTime}    Set Variable    ${date[0]}
    ${endTime}    Set Variable    ${date[1]}
    [Return]    ${startTime}    ${endTime}

整点时间
    [Arguments]    ${day}
    ${today}    Get_Current_Date    result_format=timestamp
    Log    ${today}
    #获取当前时间戳
    ${time_stamp}    Convert Date    ${today}    datetime
    Log    ${time_stamp}
    ${hour}    Set Variable    ${time_stamp.hour}
    ${minute}    Set Variable    ${time_stamp.minute}
    ${second}    Set Variable    ${time_stamp.second}
    ${microsecond}    Set Variable    ${time_stamp.microsecond}
    ${now}=    Catenate    SEPARATOR=    ${hour}:    ${minute}:    ${second}.    ${microsecond}
    ${today}    Add Time To Date    ${today}    -${now}
    log    ${today}
    ${midnight_0}    Add Time To Date    ${today}    ${day}
    ${start}    Convert Date    ${midnight_0}    epoch
    log    ${start}
    ${start_stamp}    Evaluate    int(round(${start} * 1000))
    ${night_59}    Add Time To Date    ${today}    -1second
    ${end}    Convert Date    ${night_59}    epoch
    log    ${end}
    ${end_stamp}    Evaluate    int(round(${end} * 1000))
    [Return]    ${start_stamp}    ${end_stamp}

前3天
    ${date}    整点时间    -3days
    ${startTime}    Set Variable    ${date[0]}
    ${endTime}    Set Variable    ${date[1]}
    [Return]    ${startTime}    ${endTime}

前7天
    ${date}    整点时间    -7days
    ${startTime}    Set Variable    ${date[0]}
    ${endTime}    Set Variable    ${date[1]}
    [Return]    ${startTime}    ${endTime}

前15天
    ${date}    整点时间    -15days
    log    ${date}
    ${startTime}    Set Variable    ${date[0]}
    ${endTime}    Set Variable    ${date[1]}
    [Return]    ${startTime}    ${endTime}

前30天
    ${date}    整点时间    -30days
    log    ${date}
    ${startTime}    Set Variable    ${date[0]}
    ${endTime}    Set Variable    ${date[1]}
    [Return]    ${startTime}    ${endTime}

上月
    ${last_month}    last_month.last month
    ${startTime}    Set Variable    ${last_month[0]}
    ${endTime}    Set Variable    ${last_month[1]}
    [Return]    ${startTime}    ${endTime}

登录获取cookie
    [Arguments]    ${CompanyName}    ${UserName}    ${Password}
    ${cookie}    common.GetCookie_str    ${domain}/account/login    ${CompanyName}    ${UserName}    ${Password}
    Set Suite Variable    ${cookie}
    log    ${cookie}
    [Return]    ${cookie}

双日时间戳
    [Arguments]    ${start}    ${end}
    ${time}    stamp    ${start}    ${end}
    [Return]    ${time}

发送请求
    [Arguments]    ${cookie}    ${url}    ${data}=None
    sleep    1
    ${response}    Send Http Request    ${cookie}    ${url}    ${data}
    [Return]    ${response}
