# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
__author__ = 'Anup'
import os
import time
import MyTranslator

from microsofttranslator import Translator, TranslateApiException
from pymongo import MongoClient
#import goslate
#from googleapiclient.discovery import build

#from mstranslator import Translator
#from bing_translator import Bing
#from googletrans import translator

relativePath=os.getcwd()
file=open(relativePath+"\Resource\\ReviewID.txt","r")
file1=open(relativePath+"\Resource\\ReviewID_list.txt","w")
langList=['fr','es','de']
translator=None

def init(recordToSkip=0):
    global translator
    translator = Translator('shalabh', '6Af7+rQSZl+Jqb/y4W0/QP196VkT+fiSMyoKRXBp8Y8=')
    client=MongoClient()
    db=client['yelp']
    reviewTable=db['reviewData']
    collection = db['converted_reviews']
    count=0
    #gs = goslate.Goslate()
    for line in file:
        count+=1
        print count
        if count<=recordToSkip:
            continue
        record={}
        arr=line.replace("\n","").split(':')
        id=str(arr[0])
        lng=str(arr[1])
        if lng in langList:
                time.sleep(1)
                #print count
                find={"review_id":id}
                for review in reviewTable.find(find):
                        text=review["text"]
                        stars=review["stars"]
                        #print text.encode('utf-8')
                        time.sleep(1)
                        if(len(text)>546):
                            arr1=text.split(".")
                            translated_text=""
                            for item in arr1:
                                translated_text= translated_text+". "+MyTranslator.translate(item.replace("\n","").encode('utf-8'), "en", lng)
                        else:
                            translated_text= MyTranslator.translate(text.replace("\n","").encode('utf-8'), "en", lng)
                        print "==========================="
                        #translated_text= MyTranslator.translate(text.replace("\n","").encode('utf-8'), "en", lng)
                        time.sleep(1)
                        #print translated_text
                        record.update({'review_id':id})
                        record.update({'lng':lng})
                        record.update({'translation':translated_text})
                        record.update({'stars':stars})
                        collection.insert_one(record).inserted_id
                        print count," record inserted"
                        print "============================="






init(4473)

#translator = Translator('b3f55689-9fc1-4de6-964f-0961906b1c25', 'jGGRu2laIvYJ+lLNSR44lR2gDuUSc5cCfk0Z0V8I/24')
#t=translator.translate("Dieser Airport ist ein sehr angenehmer Platz, auch sehr sauber und gut Beschildert so das man alles sehr schnell findet. Auch toll sind die vielen Schaukelst�hle in und um das Atrium in denen man sch�n entspannen kann und dem Treiben im Airport gelassen zu sehen kann. Es gibt genug Restaurants und Shops, so das jeder etwas findet. Durch seine �berschaubare Gr��e hat man hier sehr schnell alles im griff. Wir machen hier gerne Zwischenstation.", "en")
#None