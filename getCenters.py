import numpy as np
import cv2
from BluryDetect import isBloor

def getCenters(inName, delta = 10):
    def drawBox(img, bbox):
        x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
        cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),3,1)
        cv2.putText(img,"Tracking", (50,80),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),1)
    # show x,y coordinate:
    
        cv2.putText(img,"X =", (0,30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),1)
        cv2.putText(img,str(int(x)), (40,30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),1)
        cv2.putText(img,"Y =", (100,30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),1)
        cv2.putText(img,str(int(y)), (140,30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),1)

    #load video from camera
    path = inName
    cap = cv2.VideoCapture(path)
    height = int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT) )
    width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH) )
    #tracker for opencv
    #tracker = cv2.legacy.TrackerMOSSE_create()
    tracker = cv2.legacy.TrackerCSRT_create()
    success, img = cap.read()
    # print("success",success)
    bbox = cv2.selectROI("Tracking",img,False)
    tracker.init(img,bbox)

    centers = []
    cnt = -1
    while True:
        cnt += 1
        #timer = cv2.getTickCount()
    
        success1, img = cap.read()
        if cnt >=1 and centers[cnt-1][2] != True:
            success,bbox = tracker.update(img)   
        if success1 == False:
            break
        # if isBloor(img):
        #     continue
        
        if success:
            drawBox(img,bbox)
            #print(bbox)
            centers.append( (bbox[0], bbox[1], isBloor(img)) )
        else:
            centers.append((height/2, width/2, isBloor(img)))
            cv2.putText(img,"Lost", (50,80),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),1)
        if(cnt <= 0):
            continue
        a = centers[cnt-1][0]
        b = centers[cnt][0]
        c = centers[cnt -1][1]
        d = centers[cnt][1]

        if cnt  >= 1 and (a - b)**2 + (c-d)**2 >= delta**2:
            continue
            #tracker.update()
            tracker = cv2.legacy.TrackerCSRT_create()
            bbox = cv2.selectROI("Tracking",img,False)
            tracker.init(img, bbox)
            centers[cnt] = (bbox[0], bbox[1])
        if isBloor(img):
            continue
        #fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

        cv2.imshow("Tracking", img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        
    print("Correct!")
    return centers