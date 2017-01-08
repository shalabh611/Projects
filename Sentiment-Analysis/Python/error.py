
import langdetect
from pymongo import MongoClient
from langdetect import detect
import os
import codecs
import time

relativePath=os.getcwd()+"\Resource"
unMappedLanguageFile=codecs.open("C:\\Users\\Shalabh\\PycharmProjects\\Sentiment_Analysis\\ResourceunMappedLanguage.txt","r",encoding="utf-8")
errorFile=open(relativePath+"\error.txt","a")
with unMappedLanguageFile as entry:
    count=0
    for line in entry:
        lng="lol"
        try:
            lng=detect(line)
        except(UnicodeDecodeError,langdetect.lang_detect_exception.LangDetectException):
            lng=codecs.decode(line,'utf-8')
        count=count+1
        #errorFile.write(count)
        errorFile.write(lng)
        errorFile.write("=========>")
        errorFile.write(line.encode("utf-8"))
        errorFile.write("\n")
        #print "count=",count,"line=",line.encode("utf-8")
        #print lng
        #print "line=",line.encode("utf-8")
        #print "==============================="