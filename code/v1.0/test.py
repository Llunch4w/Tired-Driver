import cv2 as cv

def run(img):
    while(1):
        cv.imshow('frame',img)
        if cv.waitKey(0) == ord('q'):
            break

img = cv.imread('Crystal.jpg')
# cv.namedWindow('frame')
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hist = cv.calcHist([img_gray], [0],None, [256], [0,256])
run(img_gray)

