import codecs
import re
from pymongo import MongoClient
import numpy as np
import os

relativePath=os.getcwd()


def ExtractFoods():
    FoodCount=open(relativePath+"\Resource\\MontrealColorCount.csv","r")
    foodData_write=open(relativePath+"\Resource\\Food_Joints.txt","w")
    count=0
    list1 = ['Food','Restaurant','Pub','Bar','Breakfast'];
    with FoodCount as entry:
        for line in entry:
            if int(count)==0:
                        count=count+1
                        continue
            for item in list1:
                if item.lower() in line.lower():

                    string=line.split(",")
                    var=str(string[0])
                    line1=var.strip()
                    print count,line1
                    foodData_write.write(line1)
                    foodData_write.write("\n")
                    break

def ClassifyFoods():
    ExtractFoods()
    foodClassify=open(relativePath+"\Resource\\Food_Joints.txt","r")
    classes= ["Pubs_Beer_Wine_Cocktail_Breweries","Pizza_Italian","Sushi","Seafood","Indian","Breakfast_Brunch_Burger_Sandwiches","Yogurt_Desserts_Ice Cream","Vegetarian_Vegan","Asian_Fusion","Nightlife","Fast_Food","Coffee_Tea"]
    classes_list=[[],[],[],[],[],[],[],[],[],[],[],[]]
    miscellaneous=[]
    count1=0
    count2=0
    count3=0
    for line in foodClassify:
            #print line
            count1=count1+1
            flag=0
            #print count1
            for item in classes:
                arr=item.split("_")
                if arr[0]=="Fast":
                    temp=arr[0]+" "+arr[1]
                    arr[:]=[]
                    arr.append(temp)
                #print item
                for content in arr:
                    if content.lower() in line.lower():
                        classes_list[classes.index(item)].append(line.strip())
                        flag=1
                        break
            if flag==1:
                count2+=1
            if flag==0:
                count3+=1
                #print "Unmatched",count3
                miscellaneous.append(line.strip())
                """
                if flag==1:
                    print classes.index(item)
                    classes_list[classes.index(item)].append(line.strip())
                    break
                """
    for i in range(0,12):
        print classes[i],"=",classes_list[i]
    print "TotalRead",count1
    print  "Unmatched=",len(miscellaneous)
    print "Matched",count2
    print miscellaneous
    return classes_list,miscellaneous


def getFoods():
    FoodCount=open(relativePath+"\Resource\\MontrealColorCount.csv","r")
    matched=[]
    unmatched=[]
    matched,unmatched=ClassifyFoods()
    aggregate=[]
    for line in FoodCount:
        string=line.split(",")
        size=len(string)
        break
    for i in range(0,12):
        sum1=np.array([])
        sum1=[0] * (size-1)
        for items in matched[i]:
            count=-1
            for line in FoodCount:
                count=count+1
                if int(count)==0:
                    continue
                string=line.strip().split(",")
                #size1=len(string)
                var=str(string[0])
                if items in var:
                    for j in range(1,size):
                        sum1[j]=sum1[j]+int(string[j])
                    break
        aggregate.append(sum1)
        sum1=np.array([])
        sum1=[0] * (size-1)
        for items in unmatched:
            count=-1
            for line in FoodCount:
                count=count+1
                if int(count)==0:
                     continue
                string=line.split(",")
                #size1=len(string)
                var=str(string[0])
                if items in var:
                    for j in range(1,size):
                        sum1[j]=sum1[j]+int(string[j])
                    break
        aggregate.append(sum1)
        print aggregate






def getDistri(fileName,isNormalized,topCol=0):
     classes= ["Pub","Pizza & Italian","Sushi Bar","Seafood Food","Indian Food","Breakfast Brunch & Burger","Desserts","Vegetarian","Asian Fusion","Nightlife","Fast Food","Coffee Tea"]
     consolidatedResult=open(relativePath+"\Resource\\"+fileName+".csv","a")
     FoodCount=open(relativePath+"\Resource\\MontrealColorCount.csv","r")
     matched,unmatched=ClassifyFoods()
     count=0
     classDistDict={}
     totalClasses=len(classes)
     colorList=[]
     for line in FoodCount:
         if count==0:
             consolidatedResult.write(line)

             colArr=line.split(",")
             for i in range(1,len(colArr)):
                 colorList.append(colArr[i])
             count+=1
             continue

         arr=line.replace("\n","").split(",")
         business=arr[0]
         tempArr=[]
         for i in range(1,len(arr)):
             #try:
                 tempArr.append(float(arr[i]))
             #except ValueError:
               #  print arr[i],business

         for i in range(len(matched)):
             if business in matched[i]:
                 if classDistDict.has_key(classes[i]):
                     exsistingArr=classDistDict[classes[i]]
                     exsistingArr=exsistingArr+np.array(tempArr)
                     classDistDict[classes[i]]=exsistingArr
                 else:

                     classDistDict.update({classes[i]:np.array(tempArr)})
                 break

     #print classDistDict
     if topCol==0:
         for key in classDistDict:
                 line=key
                 list=classDistDict[key]
                 if isNormalized:
                     list=calPercentage(list)
                 for item in list:
                     line=line+","+str(item)
                 consolidatedResult.write(line)
                 consolidatedResult.write("\n")
     else:
         for key in classDistDict:
                 line=key
                 list=classDistDict[key]
                 valList,colList=findTopColor(topCol,list,colorList)
                 line1="Bisuness Category"+","+str(colList).replace("[","").replace("]","").replace("\n","").replace("'","")
                 if isNormalized:
                     valList=calPercentage(valList)
                 for item in valList:
                     line=line+","+str(item)
                 consolidatedResult.write(line1)
                 consolidatedResult.write("\n")
                 consolidatedResult.write(line)
                 consolidatedResult.write("\n")


     consolidatedResult.write("\n")
     consolidatedResult.write("\n")

def findTopColor(colCount,colValList=[],colList=[]):
     colDict={}
     selectedColList=[]
     for i in range(len(colList)):
         colDict.update({colList[i]:colValList[i]})


     sortedArray=np.sort(colValList)[-colCount:]
     for val in sortedArray:
         for key in colDict:
             if val==colDict[key]:
                 if key not in selectedColList:
                     selectedColList.append(key)
                     break
     return sortedArray,selectedColList

def calPercentage(list=[]):
    count=0
    for item in list:
        count=count+item
    tempList=[]
    for item in list:
        tempList.append((float(item)/float(count))*100)
    return tempList



#getDistri("consolidatedResult",True,10)
getFoods()

"""
arr1=np.array([1,2,3,4,5,6])
arr2=np.array([1,2,3,4,5,6])
temarr=[]
temparr=arr1+arr2
print temparr
"""