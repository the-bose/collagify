#!/usr/bin/env

import requests
import json
from PIL import Image
from urllib.request import Request, urlopen
from random import randint

#GLOBALS
headers = {'User-Agent': 'Mozilla/5.0'}

#Function that creates the collage
def createCollage(img, size, bgc=(255,255,255)):
    s=sorted(size,reverse=True)
    nWidth=s[0][0]+s[1][0]
    s=sorted(size,key=lambda x:x[1],reverse=True)
    nHeight=s[0][1]+s[0][1]

    print('GENERATING COLLAGE...\n')
    collage=Image.new('RGB',(nWidth,nHeight),color=bgc)

    for ind,i in enumerate(img):
        offset=randint(-50,50)
        x=y=max([nWidth,nHeight])
        #Fit in canvas
        while (x+i.size[0])>collage.size[0] or (y+i.size[1])>collage.size[1]:
            x=randint(0,nWidth)
            y=randint(0,nHeight)
        collage.paste(i,(offset+x,offset+y))

    imgurl.clear()
    img.clear()
    size.clear()

    return collage


#Function that chooses the images to be added to the collage
def imagePicker(imgurl,img,size,hits):
    ct=1
    for x in range(min(randint(3,5),len(hits)-1)):
        i=randint(0,len(hits)-1)
        print('Getting image '+str(ct)+'(INDEX:'+str(i)+')... ',end='')
        ct+=1
        imgurl.append(hits[i]["webformatURL"])
        imgreq = Request(imgurl[-1],headers=headers)
        img.append(Image.open(urlopen(imgreq)))
        size.append((hits[i]["webformatWidth"],hits[i]["webformatHeight"]))
        print('DONE')

#User input for keyword
query=input("Enter search term: ")
q=query.replace(" ","+")

#Query variables
key= #Enter your api_key here
url='https://pixabay.com/api/?key='+key+'&q='+q+'&image_type=photo&per_page=200'
request = Request(url,headers=headers)
resp = urlopen(request).read()
res = json.loads(resp)
hits = res["hits"]

print('Total Hits: '+str(res['totalHits'])+'\t')

#Lists for collage
imgurl=[]
img=[]
size=[]

#Initiate process of creating collages if enough hits are obtained
if len(hits)>0:
    for i in range(3):
        imagePicker(imgurl,img,size,hits)
        clg = createCollage(img,size,(randint(0,255),randint(0,255),randint(0,255)))
        clg.show()
        clg.save('./outputs/'+query+'_'+str(i)+'.jpg')
else:
    print("NO PICS FOUND")
