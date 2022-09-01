# -*- coding: UTF-8 -*-
import json



#拿到全部科目信息
def getCategroylist(res):
    kemulist = json.loads(res)
    kemulist = kemulist["data"]
    kemulist = kemulist["list"]
    kemu_list=[]
    kemuid_list=[]
    for item in kemulist:
        categoryname = item["categoryName"]
        categoryid = item["detailId"]
        kemuid_list.append(categoryid)
        kemu_list.append(categoryname)
        if 'childList' in item.keys():
            for childList1 in item['childList']:
                categoryname = childList1["categoryName"]
                categoryid = childList1["detailId"]
                kemuid_list.append(categoryid)
                kemu_list.append(categoryname)
                if 'childList' in childList1.keys():
                    for childList2 in childList1["childList"]:
                        categoryname = childList2["categoryName"]
                        categoryid = childList2["detailId"]
                        kemuid_list.append(categoryid)
                        kemu_list.append(categoryname)
                        if 'childList' in childList2.keys():
                            for childList3 in childList2["childList"]:
                                categoryname = childList3["categoryName"]
                                categoryid = childList3["detailId"]
                                kemuid_list.append(categoryid)
                                kemu_list.append(categoryname)
                                if 'childList' in childList3.keys():
                                    for childList4 in childList3["childList"]:
                                        categoryname = childList4["categoryName"]
                                        categoryid = childList4["detailId"]
                                        kemuid_list.append(categoryid)
                                        kemu_list.append(categoryname)
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue
        else:
            continue
    #print(kemu_list)
    #kemudict = dict(zip(kemu_list[::2], kemu_list[1::2]))同一个list里面组合成字典
    kemudict = dict(zip(kemuid_list,kemu_list))
    #print(kemuid_list)
    #print(kemudict)
    return kemuid_list,kemudict


def getlink_catelist(res):
    res=json.loads(res)
    res_list = res["data"]
    label=[]
    prop=[]
    for item in res_list:
        label.append(item["label"])
        prop.append(item["prop"])
        propdict = list(zip(prop,label))
    print(propdict)
    return propdict




