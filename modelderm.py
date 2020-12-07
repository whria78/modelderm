###
### Model Dermatology (http://t.modelderm.com) REST API
### Han Seung Seog (whria78@gmail.com) 
### 
### 2020-12-6
###


###### Example of Result 
###
### Error : <error>0</error> 
### Metadata converted : <race>1</race> <sex>1</sex> <age>70</age> <loc>arm</loc> <pruritus>o</pruritus> <pain>o</pain> <onset>w</onset> 
### Metadata used or not : <meta_used>1</meta_used> 
### Number of photos analyzed : <no_photo>1</no_photo> 
### Top outputs : <disease>Insect bite,0.2728,Melanocytic nevus,0.2456,Xerotic eczema,0.0761,Hemangioma,0.0704,Folliculitis,0.0561,Cherry Hemangioma,0.0379,Skin tag,0.0357,Dysplastic nevus,0.0356,Inflammed cyst,0.0240,Nonspecific (normal),0.0157</disease> 
### Malignancy output : <malignancy_output>4</malignancy_output>

 
import os
img_root=os.path.join(os.getcwd(),'examples')

import requests
import sys
import random
import string
import cv2   
import numpy as np
import time
 
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
 
def get_server_status(url,unique_id):
    result_=requests.get('%s?%s' % (url,unique_id))
    if result_.status_code!=200:
        print (result_.status_code)
        sys.exit(1)
    return result_.text.split(',') #currentusers_,message_


def modelderm(url,unique_id,image_path):
    args1_=unique_id
    args2_='<race>3</race><birth>1978</birth><sex>m</sex><location>arm</location><pruritus>x</pruritus><pain>x</pain><onset>y</onset>'
    
    ### race : skin_type (1~6) 
    ### birth : year 
    ### sex : m or f 
    ### location : <optional text>
    ### pruritus, pain : x = None; o = mild~morderate; v = severe 
    ### onset : d = < 1 week; w = < 1 month; m = < 1 year; y = > 1 year or congenital  
    
    
    ## Attach up to 5 files ; ignore after >5 photos
    file_=[('file',(custom_filename(os.path.basename(image_path)),open(image_path,'rb').read(),'Content-Type:image'))]
    
    data_={'args1':args1_,'args2':args2_}

    res=requests.post(url,files=file_,data=data_)

    return res.content

### Server List ### 
server_url='https://t.modelderm.com/api'


###
### GENERATE UNIQUE ID FOR CHECKING STATUS
###
unique_id=get_random_alphanumeric_string(8)


###
### GET SERVER STATUS
###
currentusers_,message_=get_server_status(server_url,unique_id)
print("Current users : %s" % (currentusers_))
print(message_)

###
### PREPARE IMAGE LIST
###

if len(sys.argv)>1:     img_root=str(sys.argv[1])

img_root=os.path.abspath(img_root)
   
img_list=[]
if os.path.isdir(img_root):
    for root,dirs,files in os.walk(img_root):
        for fname in files:
            ext=(os.path.splitext(fname)[-1]).lower()
            if ext == ".jpg" or ext == ".jpeg" or ext == ".png" or ext == ".webp": 
                img_path=os.path.join(root,fname)
                img_list+=[img_path]
else:
    img_list=[img_root]
    img_root=os.path.dirname(img_list[0])

print("### Image Source folder  : ",img_root)
f_result=open('api_modelderm.txt','a')

if len(img_list)==0:
    print("No file exist at %s" % img_root)
    sys.exit(0)
print("### %d files are found at %s." % (len(img_list),img_root))

start_=time.time()
for img_no,img_path in enumerate(img_list):
    print("Processing (%d/%d) : %s" % (img_no+1,len(img_list),img_path))

    ###
    ### RUN ONLINE MODEL ###
    ###    
    result_raw=modelderm(server_url,unique_id,img_path).decode('unicode_escape')
    print(result_raw)
    f_result.write(result_raw+'\n')
    
f_result.close()
print("Execute Time : ",time.time()-start_)
print("FINISHED")    
