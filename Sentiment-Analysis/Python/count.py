import random
import os

relativePath=os.getcwd()
file1=open(relativePath+"\Resource\\french.txt","r")
file2=open(relativePath+"\Resource\\eng_spanish_1.txt","r")
file3=open(relativePath+"\Resource\\german.txt","r")


def read_file():
    pos_list=[]
    neg_list=[]
    list_files=[file1,file2,file3]
    for item in list_files:
        pos_cnt=0
        neg_cnt=0
        #print item
        for line in item:
            #print line.replace("\n"," ")
            arr=line.replace("\n","").split(",")
            print arr[8]
            if arr[8] == 'pos':
                pos_cnt+=1
            elif arr[8] == 'neg':
                neg_cnt+=1
        pos_list.append(pos_cnt)
        neg_list.append(neg_cnt)
    print pos_list
    print  neg_list





read_file()
