[toc]
# 安装requirements中的库
readme.txt是基于anaconda的安装过程，由于我已经有了vs code，所以并不想再下一个anaconda，所以直接在vs code的环境里安装了requirements.txt文件中的依赖库，以下是安装过程中遇到的错误和解决办法

**访问超时**        
当执行**python -m pip install -r requirements.txt**的时候出现了**Read time out**的错误和显示**pip**指令需要升级的错误  

知道错误后对症下药即可      
**pip指令升级**     
1. 以管理员权限运行cmd
2. 执行命令
```
python -m pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip
/* 
https://mirrors.aliyun.com/pypi/simple/是国内镜像，
用-i指令指定从此地址下载，因为直接访问默认的国外镜像源
太慢了，会导致Read time out 超时
*/
```
其中有个小插曲，更新的常规操作是
1. 删除原版本pip
2. 安装新版本pip   

但是我删完原版本pip时程序因为什么错误终止了，
所以都没来得及装上新版本pip，导致此时使用pip命令会显示**没有pip模块**的错误。   
用命令
```
python -m ensurepip
```
可重新使pip有效，然后再执行一次上述的更新操作即可       
还有几个可用的国内镜像源（我未亲测）
- 豆瓣的："https://pypi.doubanio.com/simple/"
- 清华的："https://pypi.tuna.tsinghua.edu.cn/simple/"

**解决Read time out错误**       
其实第一个问题就已经给出了答案
```
python -m pip install -i https://mirrors.aliyun.com/pypi/simple/ \
pip install -r requirements.txt
// 上面中的\是换行标志
```

**Assertion failed错误**        
这个错误是因为老师给的源码文件里有一个地方的路径
应该改成自己电脑中的文件路径        
其实就是找到那几个xml文件的位置         
我电脑上改成如下这样就对了
```
face_cascade = cv2.CascadeClassifier(r'D:\python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
```

# 安装tensorflow
安装语句
```
python -m pip install tensorflow
```

安装成功后执行**import tensorflow**时出现了这样的错误
```
ModuleNotFoundError: No module named 'numpy.core._multiarray_umath' ImportError:
numpy.core.multiarray failed to import
```

参考[论坛](https://stackoverflow.com/questions/54665842/when-importing-tensorflow-i-get-the-following-error-no-module-named-numpy-cor)
发现原来是numpy版本不对，于是解决方案：
```
python -m pip install numpy --upgrade
```