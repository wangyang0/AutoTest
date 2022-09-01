# -*- coding: UTF-8 -*-
import json
def get_ruleid(res):
    rule_lists= json.loads(res)
    rule_list = rule_lists["data"]
    for item in rule_list:
        if item["defaultFlag"] == 1:
            print(item["ruleId"],item["ruleName"])
            return item['ruleId']

#if __name__ == "__main__":
    #res='{"clueId":"472658557794816","data":[{"defaultFlag":0,"ruleId":"57408607087624192","ruleName":"订单费用导入","status":1},{"defaultFlag":0,"ruleId":"60400004858249216","ruleName":"单项测试","status":1},{"defaultFlag":0,"ruleId":"67645336646189056","ruleName":"全关联表取值","status":1},{"defaultFlag":0,"ruleId":"67657262277197824","ruleName":"默认方案","status":1},{"defaultFlag":0,"ruleId":"67766830005092352","ruleName":"天端规则","status":1},{"defaultFlag":0,"ruleId":"70947928793022464","ruleName":"空配置测试","status":1},{"defaultFlag":0,"ruleId":"72728643293544448","ruleName":"测试订单分摊规则","status":1},{"defaultFlag":0,"ruleId":"77707224046239744","ruleName":"888888","status":1},{"defaultFlag":0,"ruleId":"81403032146935808","ruleName":"测试分摊","status":1},{"defaultFlag":1,"ruleId":"126370741649276928","ruleName":"利润表测试","status":1},{"defaultFlag":0,"ruleId":"151655242298163200","ruleName":"测试测试测试","status":1},{"defaultFlag":0,"ruleId":"157601109429583872","ruleName":"淘宝天猫","status":1},{"defaultFlag":0,"ruleId":"164020078977875968","ruleName":"qyp","status":1},{"defaultFlag":0,"ruleId":"171368490853335040","ruleName":"测试1","status":1}],"qTime":20,"result":1,"suc":true}'
    #get_ruleid(res)


