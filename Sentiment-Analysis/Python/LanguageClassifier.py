__author__ = 'Anup'
import re

import langdetect
from pymongo import MongoClient
from langdetect import detect
import os
import codecs
import time

relativePath=os.getcwd()+"\Resource"
fileToWrite=open(relativePath+"\LanguageCount.txt","w")
fileToWriteForAllCity=open(relativePath+"\LanguageCountForAllCity.txt","a")
cityNameFiles=open(relativePath+"\CityName.txt")
langFreqFile=open(relativePath+"\LangFreq.csv","a")
languageMapperPath=open(relativePath+"\languageMapper.txt")
unIdentifiedLangFile=open(relativePath+"\unIdentifiedLangReview.txt","a")
unMappedLanguageFile=open(relativePath+"\unMappedLanguage.txt","a")
#errorReview=open("C:\Users\Anup\Desktop\Smm Project\Yelp\Error.txt","a")
#reviewrecord="C:\Users\Shalabh\Desktop\\books\\2nd_sem\Sentiment_analysis\review_record.txt"
langDict={}
languageFrequencyCountDict={}
#{en:english,de:german}
for lang in languageMapperPath:
    arr=lang.split("\t")
    langDict.update({arr[1].lower().replace("\n",""):arr[0]})
    #langDict[arr[1].lower().replace("\n","")]=arr[0]

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
     if len(text)<5:
         return "lol"
     sent=splitReview(text)
     language="lol"
     try:
          language=detect(sent)

     except(UnicodeDecodeError,langdetect.lang_detect_exception.LangDetectException):
          #print "detect error",UnicodeDecodeError.message
          language=codecs.decode(sent,'utf-8')
          """
          errorReview.write(sent)
          errorReview.write("\n")
          """
     return language


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
                        """
                        errorReview.write(sent)
                        errorReview.write("\n")
                        """
            #fileToWrite.write(str(langDict))
            #fileToWrite.write("\n")

    client.close()

    return langDict

#Call this method to find language distribution for individual city.
#print getReviews("Paradise Valley",0)


#Call this method to find language distribution for entire city
def detectLanguageOfCities(noOfCityToSkip):
    cityNames=[]
    fileToWriteForAllCity.write("==================================================================")
    fileToWriteForAllCity.write("\n")
    for city in cityNameFiles:
       name=city.replace("\n","")
       if name not in cityNames:
         cityNames.append(name)

    cityNames=sorted(cityNames)
    count=0
    for city in cityNames:
        count+=1
        if count<=noOfCityToSkip:
            continue
        print "City Count ",count
        languageDict=getReviews(city,0)
        fileToWriteForAllCity.write(city+" "+str(languageDict))
        fileToWriteForAllCity.write("\n")
    fileToWriteForAllCity.close()
    cityNameFiles.close()
    fileToWrite.close()
    #errorReview.close()

def getLangDistributionForAllCities():
    client = MongoClient()
    db = client['yelp']
    reviewTable=db['reviewData']
    start=time.clock()
    find={}
    #count=1
    for review in reviewTable.find(find):
        #print "Review Processed ",count
        #count+=1
        text=review["text"]
        langCode=detectLanguage(text)
        if "lol"==langCode:
            unIdentifiedLangFile.write(text.encode('utf-8'))
            unIdentifiedLangFile.write("\n")
            unIdentifiedLangFile.write("==================================================")
            unIdentifiedLangFile.write("\n")
            continue
        key=""
        if langDict.has_key(langCode):
            key=langDict[langCode]
        else:
            unMappedLanguageFile.write(langCode.encode('utf-8'))
            unMappedLanguageFile.write("\n")
            continue

        if languageFrequencyCountDict.has_key(key):
            tempCount=languageFrequencyCountDict[key]
            tempCount+=1
            languageFrequencyCountDict[key]=tempCount
        else:
            languageFrequencyCountDict.update({key:1})


    langFreqFile.write("Language,Count")
    langFreqFile.write("\n")
    for key in languageFrequencyCountDict.keys():
        langFreqFile.write(key+","+str(languageFrequencyCountDict[key]))
        langFreqFile.write("\n")

    langFreqFile.write("\n")
    langFreqFile.write("\n")
    end=time.clock()
    print "Total Time Taken ",(end-start)

getLangDistributionForAllCities()
#detectLanguageOfCities(15)

