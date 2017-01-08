__author__ = 'Anup'
from pylab
import os

relativePath=os.getcwd()
consolidatedResult=open(relativePath+"\Resource\\"+"consolidatedResult"+".csv")
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

count=0
label=[]
value=[]
for line in consolidatedResult:

    if count==0:
        count+=1
        continue
    if "Bisuness Category" in line:
        arr=line.replace(" ","").replace("\n","").split(",")
        label=arr[1:]
        continue

    arr=line.split(",")
    topic=arr[0]
    value[:]=[]
    for i in range(1,len(arr)):

        value.append(float(arr[i]))

    pie(value, explode=None, labels=label,
    colors=label,
    autopct=None, pctdistance=0.6, shadow=False,
    labeldistance=1.1, startangle=None, radius=None)
    title(topic, bbox={'facecolor':'0.8', 'pad':5})
    show()


