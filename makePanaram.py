import cv2
frame_number = 3#284
images = []
for i in range(frame_number):
    img = cv2.imread("frames\\" + "frame" + str(i) + ".jpg")
    images.append(img)
#print(images)
stitcher = cv2.Stitcher.create()
(dummy, output) = stitcher.stitch(images)
if dummy != cv2.STITCHER_OK:
    print(output)
    print("something went wrong")
else:
    print("success")
cv2.imshow('final', output)
cv2.waitKey(0)