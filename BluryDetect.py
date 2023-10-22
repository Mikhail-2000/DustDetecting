# import the necessary packages
from imutils import paths
import argparse
import cv2
# def BluryDetect(frame):
#     def variance_of_laplacian(image):
#         return cv2.Laplacian(image, cv2.CV_64F).var()
#     # construct the argument parse and parse the arguments
#     ap = argparse.ArgumentParser()
#     # method
#     image = frame
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     fm = variance_of_laplacian(gray)
#     # if the focus measure is less than the supplied threshold,
#     # then the image should be considered "blurry"
#     if fm < args["threshold"]:
#         return True
#     else:
#         return False
#     key = cv2.waitKey(0)

def isBloor(imagePath, threshold = 100):
    def variance_of_laplacian(frame):
        return cv2.Laplacian(frame, cv2.CV_64F).var()
    #image = cv2.imread(imagePath)
    image = imagePath
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    #fm = 1
    #threshold = 200
    # text = "Not Blurry"
    # if fm < threshold:
    #     text = "Blurry"
    # cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    # cv2.imshow("Image", image)
    if fm < threshold:
        #cv2.imshow(imagePath)
        return True
    return False