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
resultFile=open(relativePath+"\jsonOutput.txt","a")
fileToWriteForAllCity=open(relativePath+"\LanguageCountForAllCity.txt","a")
cityNameFiles=open(relativePath+"\CityName.txt")
#langFreqFile=open(relativePath+"\LangFreq.csv","a")
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

outputDict={}
def getLangDistributionForAllCities():
    client = MongoClient()
    db = client['yelp']
    reviewTable=db['reviewData']

    start=time.clock()
    find={}
    count=0
    for review in reviewTable.find(find,no_cursor_timeout=True):
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
            unMappedLanguageFile.write(review["review_id"])
            unMappedLanguageFile.write("\n")
            continue
        if langCode !='en':
                #print "Review Processed ",count
                #count+=1
                #if count>20:
                    #print outputDict
                    #break
                rID=review["review_id"]
                rating=review["stars"]
                businessID=review["business_id"]
                if outputDict.has_key(langCode):
                        tempLangDict=outputDict[langCode]

                        if rating==5 or rating==4:
                            tempLangDict["PosCount"]=tempLangDict["PosCount"]+1
                            tempLangDict["ReviewIDPos"].append(rID)
                            if tempLangDict["BusinessList"].has_key(businessID):
                                 tempDict=tempLangDict["BusinessList"][businessID]
                                 tempDict["pos"]=tempDict["pos"]+1
                                 tempLangDict["BusinessList"][businessID]=tempDict
                            else:
                                tempDict={"pos":1,"neg":0,"neu":0}
                                tempLangDict["BusinessList"].update({businessID:tempDict})

                        elif rating==1 or rating==2:
                            tempLangDict["NegCount"]=tempLangDict["NegCount"]+1
                            tempLangDict["ReviewIDNeg"].append(rID)
                            if tempLangDict["BusinessList"].has_key(businessID):
                                 tempDict=tempLangDict["BusinessList"][businessID]
                                 tempDict["neg"]=tempDict["neg"]+1
                                 tempLangDict["BusinessList"][businessID]=tempDict
                            else:
                                tempDict={"pos":0,"neg":1,"neu":0}
                                tempLangDict["BusinessList"].update({businessID:tempDict})
                        else:
                            tempLangDict["Neutral"]=tempLangDict["Neutral"]+1
                            tempLangDict["ReviewIDNeu"].append(rID)
                            if tempLangDict["BusinessList"].has_key(businessID):
                                 tempDict=tempLangDict["BusinessList"][businessID]
                                 tempDict["neu"]=tempDict["neu"]+1
                                 tempLangDict["BusinessList"][businessID]=tempDict
                            else:
                                tempDict={"pos":0,"neg":0,"neu":1}
                                tempLangDict["BusinessList"].update({businessID:tempDict})
                        outputDict[langCode]=tempLangDict
                else:
                   tempLangDict={}
                   tempLangDict.update({"LanguageName":key})
                   tempLangDict.update({"BusinessList":[businessID]})

                   if rating==5 or rating==4:
                            tempLangDict.update({"PosCount":1})
                            tempLangDict.update({"NegCount":0})
                            tempLangDict.update({"Neutral":0})
                            tempLangDict.update({"ReviewIDPos":[rID]})
                            tempLangDict.update({"ReviewIDNeg":[]})
                            tempLangDict.update({"ReviewIDNeu":[]})
                            tempLangDict.update({"BusinessList":{businessID:{"pos":1,"neg":0,"neu":0}}})
                   elif rating==1 or rating==2:
                            tempLangDict.update({"PosCount":0})
                            tempLangDict.update({"NegCount":1})
                            tempLangDict.update({"Neutral":0})
                            tempLangDict.update({"ReviewIDNeg":[rID]})
                            tempLangDict.update({"ReviewIDPos":[]})
                            tempLangDict.update({"ReviewIDNeu":[]})
                            tempLangDict.update({"BusinessList":{businessID:{"pos":0,"neg":1,"neu":0}}})
                   else:
                            tempLangDict.update({"PosCount":0})
                            tempLangDict.update({"NegCount":0})
                            tempLangDict.update({"Neutral":1})
                            tempLangDict.update({"ReviewIDNeu":[rID]})
                            tempLangDict.update({"ReviewIDPos":[]})
                            tempLangDict.update({"ReviewIDNeg":[]})
                            tempLangDict.update({"BusinessList":{businessID:{"pos":0,"neg":0,"neu":1}}})
                   outputDict.update({langCode:tempLangDict})
    end=time.clock()
    print "Total Time Taken ",(end-start)
    languageTable=db["languageData"]
    for key in outputDict:
        resultFile.write(str(outputDict[key]).encode("utf-8"))
        resultFile.write("\n")
        languageTable.insert(outputDict[key])
    print len(outputDict)," Record inserted in languageData"


getLangDistributionForAllCities()
#detectLanguageOfCities(15)

