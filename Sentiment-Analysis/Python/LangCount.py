import codecs
import re
import langdetect
from langdetect import detect
from pymongo import MongoClient
import os


relativePath=os.getcwd()
reviewwrite=open(relativePath+"\Resource\\review.txt","a")
reviewread=codecs.open(relativePath+"\Resource\\review.txt","r",encoding="utf-8")

client=MongoClient()
db=client['yelp']
#errorCount=40
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



#def detectLanguage(text):
def detectLanguage():
     print "here"
     dict1={}
     with reviewread as entry:
         for line in entry:
             sent=splitReview(line)
             #sent=splitReview(text.encode("utf-8"))
             print "sent=",sent
             language=detect(sent.decode("utf-8"))
             #language=detect(sent)
             print "language=",language
             if any(dict1)==False:
                 dict1.update({language:1})
             else:
                 flag=0
                 for key in dict1:
                     if language in key:
                         flag=1
                         dict1[language]=dict1[language]+1
                         break
                 if flag==0:
                    dict1.update({language:1})
     print dict1

"""



def getReviewCount():
    global errorCount
    reviewTable=db['reviewData']
    find={}
    for review in reviewTable.find(find):
        text=review["text"]
        print text
        #if errorCount<0:
        #    break
        detectLanguage(text)

"""

def getReviewCount():
    global errorCount
    reviewTable=db['reviewData']
    find={}
    count=100
    for review in reviewTable.find(find):
        if count>0:
            text=review["text"]
            decodedText=codecs.encode(text,encoding='utf-8')
            print text
            #text.encode('utf-8')
            reviewwrite.write(text.encode('utf-8'))
            reviewwrite.write("\n")
            count=count-1
            #detectLanguage(text)
        else:
            reviewwrite.close()
            break;



getReviewCount()
detectLanguage()