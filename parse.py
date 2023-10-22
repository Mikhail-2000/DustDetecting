import cv2
import numpy as np
import time
from getCenters import getCenters
from BluryDetect import isBloor
def parse(inName, outName): #void
    def polarize(source, center):
        #source = cv2.imread(filename, 1)
        img = source.astype(np.float32)
        x = img.shape[0]
        y = img.shape[1]
        #center = (y/2, x/2)
        #value = np.sqrt(((x / 2.0) ** 2.0) + ((y / 2.0) ** 2.0))
        r = min(center[0], center[1], abs(y - center[0]), abs(x - center[1]))
        polar_image = cv2.linearPolar(img, center, r, 8) #16 или 8
        polar_image = polar_image.astype(np.uint8)
        #cv2.imwrite(filename, polar_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        return polar_image


    
    centers = getCenters(inName)
    #print(centers)
    #inName = "Endoscope video (1).mp4"
    #inName = "stable_video.mp4"
    #outName = "Endoscope video polirized (1).avi"
    cap = cv2.VideoCapture(inName)
    height = int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT) )
    width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH) )
    frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #print(len(centers), frame_number)
    #print(height, width)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(outName, fourcc, 20.0, (height, width))
    cnt = -1
    while True:
        cnt += 1
        if cnt == len(centers):
            break
        ret, frame = cap.read()
        # if isBloor(frame):
        #     continue
        
        if ret == 0:
            break
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        polar = polarize(frame, (centers[cnt][0], centers[cnt][1]))
        #time.sleep(0.1)
        
        cv2.imshow('video feed', polar)
        out.write(polar)
        cv2.imwrite('frames/frame' + str(cnt) + ".jpg", polar)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Im a Parser!")
    parse("Endoscope video (1).mp4", "res1.mp4")