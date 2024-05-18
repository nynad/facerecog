import cv2
import time 
import numpy as np 

vid=cv2.VideoCapture('sanrio.mp4') 
time.sleep(1)
bg=0
c=0 

for i in range(60):
    flag, bg = vid.read() 
    if flag==False: 
        continue

bg=np.flip(bg,axis=1)

while vid.isOpened(): 
    return_value, img = vid.read()
    # now 
    if not return_value: 
        break 
    c=c+1 
    print(c)
    img=np.flip(img,axis=1) 

    hsvimg=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowred=np.array([100,40,40])
    upred=np.array([100,255,255])
    mask1=cv2.inRange(hsvimg,lowred,upred)
    lowred=np.array([155,40,40])
    upred=np.array([180,255,255])
    mask2=cv2.inRange(hsvimg,lowred,upred)

    mask=mask1+mask2

    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask=cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=1)
    masktwo=cv2.bitwise_not(mask)

    result1=cv2.bitwise_and(bg,bg,mask=mask)
    result2=cv2.bitwise_and(img,img,mask=masktwo)

    finalimage=cv2.addWeighted(result1,1,result2,1,0)

    cv2.imshow("Sanrio",finalimage)
    if cv2.waitKey(10)==27:
        break 













