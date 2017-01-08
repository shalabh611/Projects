import random
import os

relativePath=os.getcwd()
file=open(relativePath+"\Resource\\eng_spanish","r")
file1=open(relativePath+"\Resource\\eng_spanish_1.txt","w")


def read_file():
    vector_list=[]
    list=[]
    for line in file:
        list=line.replace("\n","")
        vector_list.append(list)
    print len(vector_list)
    print  vector_list
    count=0
    vector=[]
    num_list=[]
    while(count<9401):
        num=random.randint(0,9400)
        if len(num_list)==0:
            num_list.append(num)
            vector.append(vector_list[num])
            count+=1
        else:
            if num in num_list:
                continue
            else:
                num_list.append(num)
                vector.append(vector_list[num])
                count+=1
    print num_list
    print  "vector",vector
    for item in vector:
        file1.write(item)
        file1.write("\n")



read_file()
