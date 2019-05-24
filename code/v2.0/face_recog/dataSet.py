from sklearn.model_selection import train_test_split
from keras.utils import np_utils
import random
import os
import cv2
import numpy as np

def read_all_file(path):
    img_list = []
    label_list = []
    dir_counter = 0
    IMG_SIZE = 128

    #对路径下的所有子文件夹中的所有jpg文件进行读取
    #并转化为大小为（128，128）的灰度图
    #并存入到一个list中
    #label_list表示的是图片对应标签，对应同一个人的图片有相同的编号
    for child_dir in os.listdir(path):
         child_path = path + "/" + child_dir

         for dir_image in  os.listdir(child_path):
            s = child_path + "/" + dir_image
            img = cv2.imread(child_path + "/" + dir_image)
            resized_img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            recolored_img = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
            img_list.append(resized_img)
            label_list.append(dir_counter)

         dir_counter += 1

    # 返回的img_list转成了 np.array的格式
    img_list = np.array(img_list)

    return img_list,label_list,dir_counter


#建立一个用于存储和格式化读取训练数据的类
class DataSet(object):
   def __init__(self,path):
       self.num_classes = None
       self.X_train = None
       self.X_test = None
       self.Y_train = None
       self.Y_test = None
       self.img_size = 128
       self.extract_data(path) #在这个类初始化的过程中读取path下的训练数据

   def extract_data(self,path):
        #根据指定路径读取出图片、标签和类别数
        imgs,labels,counter = read_all_file(path)

        #将数据集打乱随机分组
        #test_size表示数据集占的比例
        #X表示打乱后的imgs，y为相应的label
        X_train,X_test,y_train,y_test = train_test_split(imgs,labels,test_size=0.2,random_state=random.randint(0, 100))
        print("shape:",X_train.shape)
        print("size:",X_train.size)
        #重新格式化和标准化
        # 本案例是基于thano的，如果基于tensorflow的backend需要进行修改
        # X_train = X_train.reshape(X_train.shape[0], 1, self.img_size, self.img_size)/255.0
        # X_test = X_test.reshape(X_test.shape[0], 1, self.img_size, self.img_size) / 255.0

        # 基于tensorflow的backend
        X_train = X_train.reshape(X_train.shape[0], self.img_size, self.img_size,3)/255.0
        X_test = X_test.reshape(X_test.shape[0], self.img_size, self.img_size,3) / 255.0

        X_train = X_train.astype('float32')
        X_test = X_test.astype('float32')

        #将labels转成 binary class matrices
        #将labels转化成01矩阵，行数为原来y里数据个数，列数为num_classes,
        #label所属的那个类别为1外其他都为0
        #counter为种类个数
        Y_train = np_utils.to_categorical(y_train, num_classes=counter)
        Y_test = np_utils.to_categorical(y_test, num_classes=counter)

        #将格式化后的数据赋值给类的属性上
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test
        self.num_classes = counter

   def check(self):
       print('num of dim:', self.X_test.ndim)
       print('shape:', self.X_test.shape)
       print('size:', self.X_test.size)

       print('num of dim:', self.X_train.ndim)
       print('shape:', self.X_train.shape)
       print('size:', self.X_train.size)
