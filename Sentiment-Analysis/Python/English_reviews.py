__author__ = 'Anup'
import os
import EmotionParser as em
from pymongo import MongoClient

relativePath=os.getcwd()
file=open(relativePath+"\Resource\\ReviewID.txt","r")
trainingFilePath=relativePath

emotionList=['anticipation', 'enjoyment', 'sad', 'disgust', 'anger', 'surprise', 'fear', 'trust']

client = MongoClient()
db = client['yelp']
review=db["reviewData"]
def convReviewIntoVector(maxCount,skip,fname='englishVector.txt'):
    global file
    non_eng_list=[]
    for line in file:
        arr=line.replace("\n","").split(':')
        id=str(arr[0])
        non_eng_list.append(id)
    global trainingFilePath
    trainingFilePath=trainingFilePath+"\\"+fname
    find={}
    count=1
    skipCount=1
    for rev in review.find(find,no_cursor_timeout=True):
        id=rev["review_id"]
        print count
        if id in non_eng_list:
            continue
        if skipCount<=skip:
            skipCount+=1
            continue
        if count>maxCount:
            break
        resultVect=[]
        star=rev["stars"]
        if star==5 or star==4 or star==1 or star==2 :
            file=open(trainingFilePath,"a")
            cato="pos"
            resultDict=em.consolodateResult(rev["text"])
            for emo in emotionList:
                resultVect.append(resultDict[emo])
            count+=1
            if star==1 or star==2:
                cato="neg"
            file.write(str(resultVect).replace("[","").replace("]","")+","+cato)
            file.write("\n")
            file.close()


convReviewIntoVector(15000,0)
#error at 8930