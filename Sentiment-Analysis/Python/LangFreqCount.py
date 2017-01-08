
from pymongo import MongoClient
import os
import numpy


relativePath=os.getcwd()
file=open(relativePath+"\Resource\\ReviewID.txt","r")


def count():
    dict1={}
    cnt=0
    for line in file:
        cnt=cnt+1
        print cnt
        arr=line.split(":")
        #print arr[1].strip('\n')
        arr[1]=arr[1].strip('\n')
        if len(dict1)== 0:
            dict1.update({str(arr[1]):1})
        else:
            if dict1.has_key(str(arr[1])):
                dict1[arr[1]]+=1
            else:
                dict1.update({str(arr[1]):1})
    print dict1

count()



