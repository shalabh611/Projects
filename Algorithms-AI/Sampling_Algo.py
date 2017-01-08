import numpy as np
import random

def gen(sample_count=0):
    prob_count=sample_count*5
    prob_list=np.random.uniform(0,1,prob_count)
    return  prob_list

def create_CPT_order():
    CPT={}
    CPT.update({"B":{"t":0.001,"f":0.999}})
    CPT.update({"E":{"t":0.002,"f":0.998}})
    CPT.update({"A":{"tt":0.95,"tf":0.94,"ft":0.29,"ff":0.001}})
    CPT.update({"J":{"t":0.001,"f":0.5}})
    CPT.update({"M":{"t":0.7,"f":0.1}})
    order=["B","E","A","J","M"]
    return CPT,order


def takeInput(func="",count=0):
    args=raw_input(">")
    arr=args.split(" ")
    evdnc=[]
    query=[]
    for i in range(int(arr[0])):
        args=raw_input(">")
        evdnc.append(args)
    for i in range(int(arr[1])):
        args=raw_input(">")
        query.append(args+" t")
    #print evdnc
    #print query
    if func == 'e':
        print "In complete"
        #enumeration1(evdnc,query)
    elif func == 'p':
        forwardsampling(evdnc,query,count)
    elif func == 'r':
        rejectionsampling(evdnc,query,count)
    elif func == 'l':
        weightedsampling(evdnc,query,count)
    else:
        forwardsampling(evdnc,query,count)
        rejectionsampling(evdnc,query,count)
        weightedsampling(evdnc,query,count)
"""
finalList=[]
def enumeration1(ev=[], qu=[]):
    CPT_dict,order_list=create_CPT_order()
    ev_data={}
    qu_data={}
    for i in ev:
        arr=i.split(" ")
        index=order_list.index(arr[0])
        ev_data.update({int(index):arr[1]})
    for i in qu:
        arr=i.split(" ")
        index=order_list.index(arr[0])
        qu_data.update({int(index):arr[1]})
    parents={}
    parents.update({"B":None})
    parents.update({"E":None})
    parents.update({"A":["B","E"]})
    parents.update({"J":["A"]})
    parents.update({"M":["A"]})
    query_list=[]
    for item in qu:
        query_list=list(ev)
        query_list.append(item)
        enumerate2(order_list,query_list,parents)
    finalList.reverse()
    for i in range(0,2):
        temp="t"
        evidenceToBepassed=list(ev)
        if i==1:
            temp="f"
        evidenceToBepassed.append(qu[0]+" "+temp)
        Probability_calculate(list(finalList),evidenceToBepassed,None)


def enumerate2(order,evidence_list,parents_dict):
    if len(order) == 0:
        return 1;
    first=order.pop()
    parents= parents_dict.get(first)
    evidencePresent=[]
    for items in evidence_list:
        items=items.split(" ")[0]
        evidencePresent.append(items)
    if first in evidencePresent:
        finalList.append([first,parents])
        return enumerate2(order,evidence_list,parents_dict)
    else:
        finalList.append(["sum ",first,parents])
        evidenceToPass=list(evidence_list)
        evidenceToPass.append(first)
        return enumerate2(order,evidence_list,parents_dict)

"""
def forwardsampling(ev=[],qu=[],sample_count=0):
    CPT_dict,order_list=create_CPT_order()
    prob_list=gen(sample_count)
    ev_data={}
    qu_data={}
    for i in ev:
        arr=i.split(" ")
        index=order_list.index(arr[0])
        ev_data.update({int(index):arr[1]})
    forward_sample_list=[]
    index=-1
    for i in range(sample_count):
        record=[]
        for node in order_list:
            index=index+1
            prob=prob_list[index]
            if node == "B" or node =="E":
                value="t"
            elif node=="A":
                value=record[0]+record[1]
            elif node == "J" or node=="M":
                 value=record[2]
            if prob <= CPT_dict.get(node).get(value):
                 record.append("t")
            else:
                record.append("f")
        forward_sample_list.append(record)
    result={}
    for item1 in qu:
        arr=item1.split(" ")
        index=order_list.index(arr[0])
        qu_data.update({int(index):arr[1]})
        numerator=0
        denominator=0
        for item in forward_sample_list:
            flag_num=1
            flag_deno=1
            for i in ev_data:
                if ev_data[i] != item[i]:
                    flag_deno=0
                    break
            if flag_deno==1:
                denominator+=1
                for i in qu_data:
                    if qu_data[i] != item[i]:
                        flag_num=0
                        break
                if flag_num==1:
                    numerator+=1
        probability=0
        if denominator!=0:
            probability=float(numerator)/float(denominator)
        result.update({arr[0]:probability})
    for i in result:
        print i," ",result[i]

def rejectionsampling(ev=[],qu=[],sample_count=0):
    CPT_dict,order_list=create_CPT_order()
    prob_list=gen(sample_count)
    ev_data={}
    qu_data={}
    ev_keys={}
    for i in ev:
        arr=i.split(" ")
        index=order_list.index(arr[0])
        ev_data.update({int(index):arr[1]})
        ev_keys.update({arr[0]:arr[1]})
    sample_list=[]
    index=-1
    for i in range(sample_count):
        record=[]
        for node in order_list:
            index=index+1
            prob=prob_list[index]
            if node == "B" or node =="E":
                value="t"
            elif node=="A":
                value=record[0]+record[1]
            elif node == "J" or node=="M":
                 value=record[2]
            if prob <= CPT_dict.get(node).get(value):
                record.append("t")
                ch="t"
            else:
                record.append("f")
                ch="f"
            if node in ev_keys:
                if ev_keys[node] != ch:
                    record=[]
                    break
        if len(record)==5:
            sample_list.append(record)
    result={}
    for item1 in qu:
        arr=item1.split(" ")
        index=order_list.index(arr[0])
        qu_data.update({int(index):arr[1]})
        numerator=0
        denominator=0
        for item in sample_list:
            flag_num=1
            flag_deno=1
            for i in ev_data:
                if ev_data[i] != item[i]:
                    flag_deno=0
                    break
            if flag_deno==1:
                denominator+=1
                for i in qu_data:
                    if qu_data[i] != item[i]:
                        flag_num=0
                        break
                if flag_num==1:
                    numerator+=1
        probability=0
        if denominator!=0:
            probability=float(numerator)/float(denominator)
        result.update({arr[0]:probability})
    for i in result:
        print i," ",result[i]

def weightedsampling(ev=[],qu=[],sample_count=0):
    CPT_dict,order_list=create_CPT_order()
    prob_list=gen(sample_count)
    ev_data={}
    qu_data={}
    ev_keys={}
    for i in ev:
        arr=i.split(" ")
        index=order_list.index(arr[0])
        ev_data.update({int(index):arr[1]})
        ev_keys.update({arr[0]:arr[1]})
    sample_list=[]
    index=-1
    for i in range(sample_count):
        record=[]
        weight=1.00
        for node in order_list:
            if node in ev_keys:
                record.append(ev_keys[node])
                if node == "B" or node =="E":
                    value=ev_keys[node]
                elif node=="A":
                    value=record[0]+record[1]
                elif node == "J" or node=="M":
                     value=record[2]
                #print "value=",value
                var1=CPT_dict.get(node).get(value)
                #print "var1",var1
                weight=weight*var1
            else:
                index=index+1
                prob=prob_list[index]
                if node == "B" or node =="E":
                    value="t"
                elif node=="A":
                    value=record[0]+record[1]
                elif node == "J" or node=="M":
                     value=record[2]
                if prob <= CPT_dict.get(node).get(value):
                    record.append("t")
                else:
                    record.append("f")
        record.append(weight)
        sample_list.append(record)
    result={}
    for item1 in qu:
        arr=item1.split(" ")
        index=order_list.index(arr[0])
        qu_data.update({int(index):arr[1]})
        numerator=0
        denominator=0
        for item in sample_list:
            flag_num=1
            flag_deno=1
            for i in ev_data:
                if ev_data[i] != item[i]:
                    flag_deno=0
                    break
            if flag_deno==1:
                denominator=denominator+item[5]
                for i in qu_data:
                    if qu_data[i] != item[i]:
                        flag_num=0
                        break
                if flag_num==1:
                    numerator=numerator+item[5]
        probability=0
        if denominator!=0:
            probability=float(numerator)/float(denominator)
        result.update({arr[0]:probability})
    for i in result:
        print i," ",result[i]





takeInput('p',100)