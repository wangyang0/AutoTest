# -*- coding: UTF-8 -*-
import json
from get_kemulist import getlink_catelist
from get_kemulist import getCategroylist
import get_kemulist

def compare_kemu(res1,res2):
    list1 = get_kemulist.getCategroylist(res1)[0]
    list2 = get_kemulist.getCategroylist(res2)[0]
    diff = list(set(list1).difference(set(list2)))
    diff.extend(list(set(list2).difference(set(list1))))
    if diff == []:
        print(True)
    else:
        print(False)


def compare_shop(data1,data2,kemures):
    detailid_list = get_kemulist.getCategroylist(kemures)[0]
    kemudict = get_kemulist.getCategroylist(kemures)[1]
    if type(data1)==str:
        data1 = json.loads(data1)["data"]
        data2 = json.loads(data2)["data"]
    else:
        data1 = data1["data"]
        data2 = data2["data"]
    for index in range(len(data1)):
        if "columnName" in data1[index] and data1[index]["columnName"]=="占比":
            print("=============================================对比占比=============================================")
        elif "columnName" in data1[index] and data1[index]["columnName"]=="合计":
            print("=============================================对比合计=============================================")
        else:
            print("=============================================",data1[index]["time"],"=============================================")
        for detailID in detailid_list:
            try:
                print(kemudict[detailID])
                detailid = detailID.lower()
                if data1[index][detailid] == data2[index][detailid]:
                    print(data1[index][detailid], "==", data2[index][detailid])
                else:
                    print(data1[index][detailid], "!=", data2[index][detailid])
            except:
                continue

def link_comp(res1,res2,res):
    linktitle = getlink_catelist(res)
    #对比每个商品id的
    res1 = json.loads(res1)
    res2 = json.loads(res2)
    list1 = res1["data"]["list"]
    list2 = res2["data"]["list"]
    len1 = len(list1)
    len2 = len(list2)
    if len1 == len2:
        print("长度相等")
        for index in range(len1):
            #print("===================================比较第%x组=====================================" % index)
            for titles in linktitle:
                title = titles[0]
                if title in list1[index] and title in list2[index]:
                    print(titles[1])
                    if list1[index][title] == list2[index][title]:
                        print(list1[index][title],"==",list2[index][title])
                    else:
                        print(list1[index][title], "!=", list2[index][title])
                        print(list1[index]["platform_id"])
                else:
                    print("键值对不匹配")
    else:
        print("长度不想等")

def sum_copm(res1,res2,res):
    linktitle = getlink_catelist(res)
    res1 = json.loads(res1)
    res2 = json.loads(res2)
    # 对比每个商品id的
    list1 = res1["data"]["summary"]
    list2 = res2["data"]["summary"]
    for titles in linktitle:
        title = titles[0]
        if title in list1 and title in list2:
            print(titles[1],title)
            if list1[title] == list2[title]:
                print(list1[title], "==", list2[title])
            else:
                print(list1[title], "!=", list2[title])
        else:
            print("不存在该字段",title)


def order_comp(res1,res2):
    pass_num = 0
    fail_num = 0
    print(res1)
    print(res2)
    key_list1 = res1.keys()
    key_list2 = res2.keys()
    key_list = set(list(key_list1) + list(key_list2))#取键值对并集并去重
    for item in key_list:
        if item in res1 and item in res2 and res1[item] == res2[item]:
            pass_num+=1
        elif item in res1 and item not in res2:
            print("2串中没有该key",item)
            fail_num += 1
        else:
            print("1串中没有该key",item)
            fail_num+=1
    if fail_num > 0:
        print("False")
        return True
    else:
        print("True")
        return False


if __name__ == "__main__":
    res1 = {"clueId":"491436339483136457","data":{"summary":{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":807.00,"unrelate_order_charge":0.00,"num_unrefund":14.00,"platform_charge":0.00,"trade_profit_uncost":807.00,"refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":807.00,"trade_profit_unrefund_rate":400.00,"total_charge_rate":3.86,"cost_syscon":0.00,"refund_count":0.00,"reportcount":8.00,"sale_num":14.00,"goods_cost":0.00,"sales_item_fee":607.00,"trade_profit_rate":396.14,"estimate_charge":8.00,"pf_payment":0.00,"total_charge":8.00,"num_syscon":1.00,"discount_devide":-200.00,"sale_cost":0.00,"cost_unrefund":0.00,"trade_profit":799.00,"refund":0.00},"page":{"offsetRow":20,"pageNo":1,"pageSize":20,"startRow":0},"list":[{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":207.00,"unrelate_order_charge":0.00,"num_unrefund":1.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"","platform_charge":0.00,"t_sid":3923565228597805.00,"trade_profit_uncost":207.00,"warehouseName":"默认仓库","tid":"490512384496128","platform":"tb","refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":207.00,"trade_profit_unrefund_rate":100.00,"total_charge_rate":"3.86%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"平台","sale_num":1.00,"insert_date":1661443200000,"goods_cost":0.00,"sales_item_fee":207.00,"trade_profit_rate":96.14,"estimate_charge":8.00,"shop_uni_id":"37741_88387","short_id":3241.00,"pf_payment":0.00,"total_charge":8.00,"pay_time":"2022-08-26 11:36:08","num_syscon":1.00,"discount_devide":0.00,"sys_sid":3923565228597805.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":199.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":200.00,"unrelate_order_charge":0.00,"num_unrefund":2.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"3912867522291199","platform_charge":0.00,"t_sid":3920593995062109.00,"trade_profit_uncost":200.00,"warehouseName":"默认仓库","tid":"488916124281344-ztc9u3","platform":"sys","refund_cost":0.00,"tagNames":"测试赠品标签","suidan_total":0.00,"sales_unrefund":200.00,"trade_profit_unrefund_rate":100.00,"total_charge_rate":"0.00%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":2.00,"insert_date":1661270400000,"goods_cost":0.00,"sales_item_fee":200.00,"trade_profit_rate":100.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3237.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-24 10:58:16","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3920593995062109.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":200.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":200.00,"unrelate_order_charge":0.00,"num_unrefund":2.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"3912867522291199","platform_charge":0.00,"t_sid":3920593995062115.00,"trade_profit_uncost":200.00,"warehouseName":"默认仓库","tid":"488916124281344-bxe3r9","platform":"sys","refund_cost":0.00,"tagNames":"测试赠品标签","suidan_total":0.00,"sales_unrefund":200.00,"trade_profit_unrefund_rate":100.00,"total_charge_rate":"0.00%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":2.00,"insert_date":1661270400000,"goods_cost":0.00,"sales_item_fee":100.00,"trade_profit_rate":100.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3239.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-24 10:58:16","num_syscon":0.00,"discount_devide":-100.00,"sys_sid":3920593995062115.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":200.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":0.00,"unrelate_order_charge":0.00,"num_unrefund":1.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"","platform_charge":0.00,"t_sid":3924058433348429.00,"trade_profit_uncost":0.00,"warehouseName":"默认仓库","tid":"490512384496128","platform":"sys","refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":0.00,"trade_profit_unrefund_rate":0.00,"total_charge_rate":"0%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":1.00,"insert_date":1661443200000,"goods_cost":0.00,"sales_item_fee":0.00,"trade_profit_rate":0.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3247.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-26 11:36:08","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3924058433348429.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":0.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":200.00,"unrelate_order_charge":0.00,"num_unrefund":2.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"3912867522291199","platform_charge":0.00,"t_sid":3920593995062118.00,"trade_profit_uncost":200.00,"warehouseName":"默认仓库","tid":"488916124281344-6g4dhf","platform":"sys","refund_cost":0.00,"tagNames":"测试赠品标签","suidan_total":0.00,"sales_unrefund":200.00,"trade_profit_unrefund_rate":100.00,"total_charge_rate":"0.00%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":2.00,"insert_date":1661270400000,"goods_cost":0.00,"sales_item_fee":100.00,"trade_profit_rate":100.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3240.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-24 10:58:16","num_syscon":0.00,"discount_devide":-100.00,"sys_sid":3920593995062118.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":200.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":0.00,"unrelate_order_charge":0.00,"num_unrefund":1.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"","platform_charge":0.00,"t_sid":3923555649182386.00,"trade_profit_uncost":0.00,"warehouseName":"默认仓库","tid":"490512384496128","platform":"sys","refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":0.00,"trade_profit_unrefund_rate":0.00,"total_charge_rate":"0%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":1.00,"insert_date":1661443200000,"goods_cost":0.00,"sales_item_fee":0.00,"trade_profit_rate":0.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3246.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-26 11:36:08","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3923555649182386.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":0.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":0.00,"unrelate_order_charge":0.00,"num_unrefund":1.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"","platform_charge":0.00,"t_sid":3923566624809616.00,"trade_profit_uncost":0.00,"warehouseName":"默认仓库","tid":"490512384496128","platform":"sys","refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":0.00,"trade_profit_unrefund_rate":0.00,"total_charge_rate":"0%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":1.00,"insert_date":1661443200000,"goods_cost":0.00,"sales_item_fee":0.00,"trade_profit_rate":0.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3245.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-26 11:36:08","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3923566624809616.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":0.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":0.00,"unrelate_order_charge":0.00,"num_unrefund":4.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"3912867522291199","platform_charge":0.00,"t_sid":3920593995062112.00,"trade_profit_uncost":0.00,"warehouseName":"默认仓库","tid":"488916124281344-4gxye2","platform":"sys","refund_cost":0.00,"tagNames":"测试赠品标签","suidan_total":0.00,"sales_unrefund":0.00,"trade_profit_unrefund_rate":0.00,"total_charge_rate":"0%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":4.00,"insert_date":1661270400000,"goods_cost":0.00,"sales_item_fee":0.00,"trade_profit_rate":0.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3238.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-24 10:58:16","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3920593995062112.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":0.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00}],"totalCount":8.00,"summaryState":1},"qTime":49,"result":1,"suc":True}
    res2 = {"clueId":"491436336714240860","data":{"summary":{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":807.00,"unrelate_order_charge":0.00,"num_unrefund":14.00,"platform_charge":0.00,"trade_profit_uncost":807.00,"refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":807.00,"trade_profit_unrefund_rate":400.00,"total_charge_rate":3.86,"cost_syscon":0.00,"refund_count":0.00,"reportcount":8.00,"sale_num":14.00,"goods_cost":0.00,"sales_item_fee":607.00,"trade_profit_rate":396.14,"estimate_charge":8.00,"pf_payment":0.00,"total_charge":8.00,"num_syscon":1.00,"discount_devide":-200.00,"sale_cost":0.00,"cost_unrefund":0.00,"trade_profit":799.00,"refund":0.00},"page":{"offsetRow":20,"pageNo":1,"pageSize":20,"startRow":0},"list":[{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":0.00,"unrelate_order_charge":0.00,"num_unrefund":1.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"","platform_charge":0.00,"t_sid":3924058433348429.00,"trade_profit_uncost":0.00,"warehouseName":"默认仓库","tid":"490512384496128","platform":"sys","refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":0.00,"trade_profit_unrefund_rate":0.00,"total_charge_rate":"0%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":1.00,"insert_date":1661443200000,"goods_cost":0.00,"sales_item_fee":0.00,"trade_profit_rate":0.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3247.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-26 11:36:08","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3924058433348429.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":0.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":200.00,"unrelate_order_charge":0.00,"num_unrefund":2.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"3912867522291199","platform_charge":0.00,"t_sid":3920593995062118.00,"trade_profit_uncost":200.00,"warehouseName":"默认仓库","tid":"488916124281344-6g4dhf","platform":"sys","refund_cost":0.00,"tagNames":"测试赠品标签","suidan_total":0.00,"sales_unrefund":200.00,"trade_profit_unrefund_rate":100.00,"total_charge_rate":"0.00%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":2.00,"insert_date":1661270400000,"goods_cost":0.00,"sales_item_fee":100.00,"trade_profit_rate":100.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3240.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-24 10:58:16","num_syscon":0.00,"discount_devide":-100.00,"sys_sid":3920593995062118.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":200.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":200.00,"unrelate_order_charge":0.00,"num_unrefund":2.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"3912867522291199","platform_charge":0.00,"t_sid":3920593995062115.00,"trade_profit_uncost":200.00,"warehouseName":"默认仓库","tid":"488916124281344-bxe3r9","platform":"sys","refund_cost":0.00,"tagNames":"测试赠品标签","suidan_total":0.00,"sales_unrefund":200.00,"trade_profit_unrefund_rate":100.00,"total_charge_rate":"0.00%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":2.00,"insert_date":1661270400000,"goods_cost":0.00,"sales_item_fee":100.00,"trade_profit_rate":100.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3239.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-24 10:58:16","num_syscon":0.00,"discount_devide":-100.00,"sys_sid":3920593995062115.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":200.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":0.00,"unrelate_order_charge":0.00,"num_unrefund":1.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"","platform_charge":0.00,"t_sid":3923555649182386.00,"trade_profit_uncost":0.00,"warehouseName":"默认仓库","tid":"490512384496128","platform":"sys","refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":0.00,"trade_profit_unrefund_rate":0.00,"total_charge_rate":"0%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":1.00,"insert_date":1661443200000,"goods_cost":0.00,"sales_item_fee":0.00,"trade_profit_rate":0.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3246.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-26 11:36:08","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3923555649182386.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":0.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":0.00,"unrelate_order_charge":0.00,"num_unrefund":4.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"3912867522291199","platform_charge":0.00,"t_sid":3920593995062112.00,"trade_profit_uncost":0.00,"warehouseName":"默认仓库","tid":"488916124281344-4gxye2","platform":"sys","refund_cost":0.00,"tagNames":"测试赠品标签","suidan_total":0.00,"sales_unrefund":0.00,"trade_profit_unrefund_rate":0.00,"total_charge_rate":"0%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":4.00,"insert_date":1661270400000,"goods_cost":0.00,"sales_item_fee":0.00,"trade_profit_rate":0.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3238.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-24 10:58:16","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3920593995062112.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":0.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":207.00,"unrelate_order_charge":0.00,"num_unrefund":1.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"","platform_charge":0.00,"t_sid":3923565228597805.00,"trade_profit_uncost":207.00,"warehouseName":"默认仓库","tid":"490512384496128","platform":"tb","refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":207.00,"trade_profit_unrefund_rate":100.00,"total_charge_rate":"3.86%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"平台","sale_num":1.00,"insert_date":1661443200000,"goods_cost":0.00,"sales_item_fee":207.00,"trade_profit_rate":96.14,"estimate_charge":8.00,"shop_uni_id":"37741_88387","short_id":3241.00,"pf_payment":0.00,"total_charge":8.00,"pay_time":"2022-08-26 11:36:08","num_syscon":1.00,"discount_devide":0.00,"sys_sid":3923565228597805.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":199.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":200.00,"unrelate_order_charge":0.00,"num_unrefund":2.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"3912867522291199","platform_charge":0.00,"t_sid":3920593995062109.00,"trade_profit_uncost":200.00,"warehouseName":"默认仓库","tid":"488916124281344-ztc9u3","platform":"sys","refund_cost":0.00,"tagNames":"测试赠品标签","suidan_total":0.00,"sales_unrefund":200.00,"trade_profit_unrefund_rate":100.00,"total_charge_rate":"0.00%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":2.00,"insert_date":1661270400000,"goods_cost":0.00,"sales_item_fee":200.00,"trade_profit_rate":100.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3237.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-24 10:58:16","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3920593995062109.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":200.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00},{"pf_refund":0.00,"post_fee":0.00,"real_pay_amount":0.00,"unrelate_order_charge":0.00,"num_unrefund":1.00,"shopName":"wj淘宝沙箱环境测试","t_tag_ids":"","platform_charge":0.00,"t_sid":3923566624809616.00,"trade_profit_uncost":0.00,"warehouseName":"默认仓库","tid":"490512384496128","platform":"sys","refund_cost":0.00,"suidan_total":0.00,"sales_unrefund":0.00,"trade_profit_unrefund_rate":0.00,"total_charge_rate":"0%","billing_status":"","cost_syscon":0.00,"refund_count":0.00,"platformName":"淘宝","order_type":"线下","sale_num":1.00,"insert_date":1661443200000,"goods_cost":0.00,"sales_item_fee":0.00,"trade_profit_rate":0.00,"estimate_charge":0.00,"shop_uni_id":"37741_88387","short_id":3245.00,"pf_payment":0.00,"total_charge":0.00,"pay_time":"2022-08-26 11:36:08","num_syscon":0.00,"discount_devide":0.00,"sys_sid":3923566624809616.00,"user_id":37741.00,"sale_cost":0.00,"billing_time":0,"cost_unrefund":0.00,"trade_profit":0.00,"is_sd":"否","warehouse_id":51753.00,"refund":0.00}],"totalCount":8.00,"summaryState":1},"qTime":34,"result":1,"suc":True}
    order_comp(res1,res2)
