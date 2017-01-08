__author__ = 'Anup'
import re
import langdetect
import codecs
from pymongo import MongoClient
from langdetect import detect
import os
relativePath=os.getcwd()
reviewrecord=open(relativePath+"\Resource\\rv.txt","a")

client=MongoClient()
db=client['yelp']
errorCount=40
def splitReview(review):
    line=re.sub('[@/#?*]',"",review.encode('utf-8').replace("\n",""))
    stoper=[".","!","?"]
    for stop in stoper:
        if stop in line:
            list=line.split(stop)
            for sen in list:
                if len(sen)>10:
                    return sen

    return line

def detectLanguage(text):
     global errorCount
     if len(text)<5 and "." in text:
         return
     sent=splitReview(text)
     #sent=splitReview(text.encode("utf-8"))
     #print sent
     language="lol"
     try:
          language=detect(sent.encode("utf-8"))
          return language

     except(UnicodeDecodeError,langdetect.lang_detect_exception.LangDetectException):
         #print language
         print sent

         print "detect error",UnicodeDecodeError.message
         encoded=codecs.decode(sent,'utf-8')
         return detect(encoded)


"""
#Call this method to find language distribution for individual city.
def getReviews(cityName,recordToSkip):
    client = MongoClient()
    db = client['yelp']
    cluster=db["clusterData"]
    review=db["reviewData"]
    langDict={}
    find={"CityName":cityName}
    for city in cluster.find(find,no_cursor_timeout=True):
        reviewAndTipList=city["reviewAndTips"]
        businessCount=0
        for business in reviewAndTipList:
            businessCount+=1
            if businessCount<recordToSkip:
                continue
            # print "Business Count ",businessCount
            reviewIdList=business["Reviews"]
            for reviewID in reviewIdList:

                findReview={"review_id":reviewID}
                for re in review.find(findReview,no_cursor_timeout=True):
                    rev=re["text"]
                    sent=splitReview(rev)
                    try:
                       language=detect(sent)
                       if langDict.has_key(language):
                           count=langDict[language]
                           count+=1
                           langDict[language]=count
                       else:
                           langDict[language]=1
                    except (UnicodeDecodeError,langdetect.lang_detect_exception.LangDetectException):
                        print "detect error",UnicodeDecodeError.message
                        errorReview.write(sent)
                        errorReview.write("\n")
            #fileToWrite.write(str(langDict))
            #fileToWrite.write("\n")

    client.close()

    return langDict
"""

def getReview():
    global errorCount
    reviewTable=db['reviewData']
    find={}
    for review in reviewTable.find(find):
        text=review["text"]
        if errorCount<0:
            break
        detectLanguage(text)


getReview()