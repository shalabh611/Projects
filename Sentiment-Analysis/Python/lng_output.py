import os
from pymongo import MongoClient

relativePath=os.getcwd()
file=open(relativePath+"\Resource\\ReviewID.txt","r")
file_de=open(relativePath+"\Resource\\ReviewDE_list.txt","w")
file_fr=open(relativePath+"\Resource\\ReviewFR_list.txt","w")
file_es=open(relativePath+"\Resource\\ReviewES_list.txt","w")
langList=['fr','es','de']


def output():
    client=MongoClient()
    db=client['yelp']
    reviewTable=db['reviewData']
    collection = db['converted_reviews']
    count=0
    for line in file:
        record={}
        arr=line.replace("\n","").split(':')
        id=str(arr[0])
        lng=str(arr[1])
        if lng in langList:
            count=count+1
            print count
            find={"review_id":id}
            for review in reviewTable.find(find):
                text=review["text"]
                text=text.encode('utf-8')
                if lng in 'fr':
                    file_fr.write(text.replace("\n",""))
                    file_fr.write("\n")
                elif lng in 'es':
                    file_es.write(text.replace("\n",""))
                    file_es.write("\n")
                elif lng in 'de':
                    file_de.write(text.replace("\n",""))
                    file_de.write("\n")




output()