__author__ = 'Anup'
import os
import EmotionParser as em
from pymongo import MongoClient

relativePath=os.getcwd()+"\Resource"
trainingFilePath=relativePath

emotionList=['anticipation', 'enjoyment', 'sad', 'disgust', 'anger', 'surprise', 'fear', 'trust']

client = MongoClient()
db = client['yelp']
review=db["converted_reviews"]
def convReviewIntoVector(maxCount,skip,lan='fr',fname='french.txt'):
    global trainingFilePath
    trainingFilePath=trainingFilePath+"\\"+fname
    find={"lng":lan}
    count=1
    skipCount=1
    for rev in review.find(find,no_cursor_timeout=True):
        print count
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
            resultDict=em.consolodateResult(rev["translation"])
            for emo in emotionList:
                resultVect.append(resultDict[emo])
            count+=1
            if star==1 or star==2:
                cato="neg"
            file.write(str(resultVect).replace("[","").replace("]","")+","+cato)
            file.write("\n")
            file.close()


convReviewIntoVector(500,0,"es","spanish.txt")