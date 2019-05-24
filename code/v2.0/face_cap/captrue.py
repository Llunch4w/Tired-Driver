import os
import cv2
import time

def readImgs(path):
    try:
        images = os.listdir(path)
        resultArray = []

        for img in images:
            document = path + "/" + img
            print(document)
            img = cv2.imread(document)
            resultArray.append(img)

    except IOError:
        print("Error")

    else:
        print("读取成功")
        return resultArray

def pickFace(src,des):
    if os.path.exists(des) == False:
        os.mkdir(des)
    resultArray = readImgs(src)
    print(len(resultArray))
    count = 1
    face_cascade = cv2.CascadeClassifier('D:\python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

    for img in resultArray:
        if type(img) != str:
            try:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            except Exception:
                print("erro")
                continue
            
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            print(faces)
            for (x, y, w, h) in faces:
                listStr = [str(int(time.time())), str(count)]  #以时间戳和读取的排序作为文件名称
                fileName = ''.join(listStr)

                f = cv2.resize(gray[y:(y + h), x:(x + w)], (200, 200))
                cv2.imwrite(des+"/"+'%s.jpg' % fileName, f)
                print("count:",count)
                count += 1

if __name__ == "__main__":
    names = ["赵丽颖","杨紫","郑爽","王俊凯","罗云熙"]
    for i in range(0,5):
        pickFace("../scrap/images/p"+str(i+1),"images/p"+str(i+1))