import os

relativePath=os.getcwd()
file1=open(relativePath+"\Resource\\french.txt","r")
file2=open(relativePath+"\Resource\\eng_spanish_1.txt","r")
file3=open(relativePath+"\Resource\\german.txt","r")

def read_file():
    list_files=[file1,file2,file3]
    weightage=[]
    for item in list_files:
        emo_vector=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        total=0.0
        for line in item:
            #print line.replace("\n"," ")
            arr=line.replace("\n","").split(",")
            #print arr
            for i in range(8):
                emo_vector[i]=emo_vector[i]+float(arr[i])
                total=total+float(arr[i])
        #print item,total,emo_vector
        vector=[]
        for i in emo_vector:
            value=float(float(i/total)*100)
            vector.append(value)
        weightage.append(vector)
    for item in weightage:
        print item
        sum=0
        for tot in item:
            sum=sum+tot
        print sum

read_file()