    此代码基于python3！


环境安装（win10&&Ubuntu）：
anaconda是一个开源的python发行版本。由于anaconda环境管理容易，因此我们用anaconda来配置python环境。
1.安装anaconda（下载python3版本）。
     win10:   参考教程：https://blog.csdn.net/ITLearnHall/article/details/81708148
     ubuntu:   参考教程：https://blog.csdn.net/qq_15192373/article/details/81091098
2. 在anaconda下创建新的python3环境，可选择python3.6
     win10:直接在anaconda界面创建新的环境。
     Ubuntu：conda create -n 环境名称 python==3.6

3. 打开新建环境的命令行窗口，切换工作目录到Fatigue-Detection-master/binary_thresholding文件夹下，输入以下语句安装所需依赖
    python -m pip install -r requirements.txt

    关于pip命令可参考：https://www.cnblogs.com/xueweihan/p/4981704.html

4.正常安装完成后，输入以下语句运行源文件。
    python detector_with_alarm.py

以上代码仅供参考，可自行选择编程语言完成工作。
建议先了解图像处理相关知识，熟悉opencv库常用函数。
dlib是和机器学习有关的库，但是也有和面部识别相关的东西。
先试着把环境搭好，把代码运行起来。然后自己去查阅相关的知识。
