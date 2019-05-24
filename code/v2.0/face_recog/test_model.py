from dataSet import read_all_file
from train_model import Model
import cv2
import os

#读取训练数据集的文件夹，把他们的名字返回给一个list
def read_name_list(path):
    name_list = []
    for child_dir in os.listdir(path):
        name_list.append(child_dir)
    return name_list

def test_onePicture(path):
    model= Model()
    model.load()
    img = cv2.imread(path)
    img = cv2.resize(img, (64, 64))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    picType,prob = model.predict(img)
    if picType != -1:
        name_list = read_name_list('../face_cap/images')
        print(name_list[picType],prob)
    else:
        print(" Don't know this person")

#读取文件夹下子文件夹中所有图片进行识别
def test_onBatch(path):
    model= Model()
    model.load()
    index = 0
    name_list = read_name_list('../face_cap/images')
    img_list, label_list, counter = read_all_file(path)
    correct = 0
    for i in range(len(img_list)):
        picType,prob = model.predict(img_list[i])
        if picType != -1:
            index += 1
            if label_list[i] == picType:
                # print(label_list[i],picType)
                correct += 1
                
            print("实际:p" + str(label_list[i]+1),"真实：" + name_list[picType],"概率：" + str(prob))
        else:
            print(" Don't know this person")

    print("测试正确率：",str(correct) + "/" + str(index))

if __name__ == '__main__':
    test_onBatch('../test')



