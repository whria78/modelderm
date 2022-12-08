###
### Model Dermatology REST API
### Han Seung Seog (whria78@gmail.com) 
### 
### 2022-12-08
###

# Please be sure to use rectangle image as an input image.
 
import os
import requests
import sys
import random
import string
import cv2   
import numpy as np
import time
import re
from datetime import datetime

# for python2 python3 compatibility
try:
    import urllib.parse as myurl
except ImportError:
    import urllib as myurl
from io import BytesIO

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(length)))
 
# for unicode support
def custom_filename(x):return myurl.quote(x)
 
def get_server_status(url,api_key):
    result_=requests.get('%s?%s' % (url,api_key))
    if result_.status_code!=200:
        print (result_.status_code)
        sys.exit(1)
    return result_.text.split(',') #currentusers_,message_


def modelderm(url,api_key,image_path,imencoded,meta_):
    url=url+'?json_format=1'
    args1_=api_key # API KEY
    args2_='<id></id><race></race><birth></birth><sex></sex><location></location><pruritus></pruritus><pain></pain><onset></onset>'
    
    file_=[]
    file_+=[('file',(custom_filename(os.path.basename(image_path)),imencoded,'Content-Type:image'))]
   
    data_={'args1':args1_,'args2':args2_}

    res=requests.post(url,files=file_,data=data_)

    return res.content

### Server List ### 
server_url='https://t.modelderm.com/api'


###
### GENERATE UNIQUE ID FOR CHECKING STATUS
###
api_key=""

###
### GET SERVER STATUS
###
currentusers_,message_=get_server_status(server_url,api_key)
print("Current users : %s" % (currentusers_))
print(message_)

img_list=[]
img_root='./images'
for root,dirs,files in os.walk(img_root):
    for fname in files:
        ext=(os.path.splitext(fname)[-1]).lower()
        if ext == ".jpg" or ext == ".jpeg" or ext == ".png" or ext == ".webp": 
            img_path=os.path.join(root,fname)
            img_list+=[img_path.replace('\\','/')]

#img_list=[img_list[0]]

if len(img_list)==0:
    print("No file exist at %s" % img_root)
    sys.exit(0)
print("### %d files are found at %s." % (len(img_list),img_root))

for processed_,img_path in enumerate(img_list):
    print("Processing (%d/%d) : %s" % (processed_+1,len(img_list),img_path))
    
    img_org=cv2.imread(img_path,cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)

    def get_center(img_org):
        w,h,_=img_org.shape
        if (w>h):
            x1=int((w-h)/2)
            x2=x1+h
            y1=0
            y2=h
        else:
            x1=0
            x2=w
            y1=int((h-w)/2)
            y2=y1+w
        crop_img=img_org[x1:x2,y1:y2]
        return crop_img

    crop_img=get_center(img_org) ## RECTANGULAR IMAGE
    imencoded = cv2.imencode(".webp", crop_img)[1].tobytes()    
    
    result_raw=modelderm(server_url,api_key,img_path,imencoded,None).decode('unicode_escape')
    print(result_raw) 

print("FINISHED")    

