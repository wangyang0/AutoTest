# -*- coding: UTF-8 -*-
import time
from http import cookiejar
from urllib import request
import requests
import json
import jsonpath
import random



class common(object):
    @staticmethod
    def GetCookie_str(url,companyname,username,password):
        """
        获取erp cookie
        :param url: 网址
        :param companyname: 公司名
        :param username: 用户名
        :param password: 网址
        :return: cookie
        """
        companyname = companyname.encode("utf-8").decode("latin1")
        username = username.encode("utf-8").decode("latin1")
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        payload = 'companyName='+ companyname+'&userName='+username+'&password='+password
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.cookies)
        if response.status_code == 200:
            dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
            cookiestr = ""
            for key in dict_cookies.keys():
                value = dict_cookies.get(key)
                if cookiestr =="":
                    cookiestr = key+"="+value
                else:
                    cookiestr=cookiestr+";"+key+"="+value
            print(cookiestr)
            return cookiestr
        else:
            print("response code"+ str(response.status_code))
            print("登录失败")



    @staticmethod
    def SendHttpRequest(cookie, url, req_body=None):
        """
        发送http请求
        :param req_body: 请求时需手动把\改为\\\
        :return: response的string形式

        Example:
        | *Keywords*           |  *Parameters*  |
post请求 | Send Http Request    |cookie          |url            |req_body
get请求  | Send Http Request    |cookie          |url
        """

        headers = {
            'cookie': cookie,
            'cache-control': "no-cache"
        }
        s = requests.session()
        s.keep_alive = False
        # 发送get请求
        if req_body is None:
            resp = requests.get(url, cookie, headers=headers)
            print("发送get请求，url为：" + url)

        else:
            # 发送post请求,请求参数是json类型
            if req_body.startswith("{") or req_body.startswith("["):
                headers["Content-Type"] = "application/json;charset=UTF-8; charset=UTF-8"
                req_body = req_body.replace('false', 'False').replace('true', 'True')
                dict_pay = eval(req_body)
                print("发送post请求，url为：" + url + "；请求参数为：" + req_body)
                resp = requests.request("POST", url, data=json.dumps(dict_pay), headers=headers)

            else:
                # 发送post请求,请求参数是Form_Data类型
                if req_body is not None:
                    req_body = req_body.encode("utf-8").decode("latin1")
                headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
                print("发送post请求，url为：" + url)
                print("请求参数为：" + req_body)
                resp = requests.post(url, data=req_body, headers=headers)

        if str(resp.status_code) != "200":
            raise Exception("请求发送错误，status code:" + str(resp.status_code) + "；错误内容：" + resp.text)
            return False
        else:
            context = resp.text
            print("请求结果为" + context)
            return resp.text

    @staticmethod
    def GetResonseValue(response,path):
        response = response.replace("false","False").replace("true","True")
        res = eval(response)
        path1 = "$."+path
        result = jsonpath.jsonpath(res, path1)[0]
        if result is False:
            return False
        elif result is True:
            return True
        else:
            print("获取的结果"+path+"为："+str(result))
            return str(result)

    def sysStatus_random(self):
       list1 = [[1,'pay'],[3, 'end'], [2,'consign'],]
       sysStatus = random.choice(list1)
       return sysStatus




if __name__ == "__main__":
    com=common()
    # url = "https://puberp.superboss.cc/account/login"
    # companyname = "咖啡测试3"
    # username = "yytest"
    # password = "E80A4CCAB76648EC13AE0891B8053D90"
    # cookie = {"_censeid": "fbbfabe0693757e0caa2da648ca9ce0119ff07ab","acw_tc": "3ccdc15216595057319243387e554659268c110e5478aab4bf8a3b821a3c19"}    #cookie = {"acw_tc": "3ccdc16716594968867153960e186adcc42f57a277704755161eceb1bfeebe","_censeid": "bf0bcf1ae548d579f642724aaec5094903158702"}
    # cookie = com.Get_Cookie(url,companyname,username,password)
    # print(cookie)
    #data = 'None'
    #url = "https://puberp.superboss.cc/kmzk/profit/report/shop?api_name=kmzk_profit_report_shop&sysStatus=1&startTime=1658851200000&endTime=1659455999000&shopUniIds=10438_84864&timeOrderType=asc&showDimension=0&ruleId=204987643321253888&showSuit=1&refundSumType=0&consignBeforeRate=&consignAfterRate=&isTrusted=true"
    #url="https://puberp.superboss.cc/kmzk/categoryValuePlan/list/concise?api_name=kmzk_categoryValuePlan_list_concise"
    #result = com.my_request('GET',url,data,cookie)
    # response = '{"code": 0,"data": [],"msg": True}'
    # com.GetResonseValue(response,'msg')



