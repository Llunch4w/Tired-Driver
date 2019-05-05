[toc]
# 图片操作

```
img = cv2.imread("filepath")  //读入路径内图片并返回一个句柄
cv2.namedWindow('windowName') //给窗口命名为windowName
cv2.imshow('windowName',img) //在名字为windowName的窗口上显示img句柄控制的图像
cv2.setMouseCallback('windowName',function) //给此窗口名指向的窗口添加回调函数
k = cv2.waitKey(sec)  // 等有键输入或者sec ms后自动将窗口消除，0表示只用键输入结束窗口
ord('m') // 可返回一个int数值，判断这个值是否和上述k相等来判断是否按键为m
// 其他字母同理，“Esc"键的值为27
cv2.destroyAllWindows()  // 可以轻易删除任何我们建立的窗口
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  // 将src图片转换成灰度图
cv2.imwrite("output.png", gray) //将上述转化得到的gray写入output.png
new_image = image.copy()  // 复制image图片
dst = cv2.bitwise_not(image) //按位取反，白变黑，黑变白
h,w,ch = img.shape // 图像的高，宽，通道数目
height,width = image.shape[:n] //返回数组下标为0-n的元素(不包括n)
```

# 图像变换

```
// 图像偏移：M = np.array([[1, 0, tx], [0, 1, ty]])
// [放大倍数，倾斜角度，偏移像素]
rows, cols = image.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(image, M, (cols, rows))
// 将图像相对于中心逆时针旋转90度，而不进行任何缩放。旋转中心，角度，缩放比率
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
/*
在仿射变换中，原始图像中的所有平行线在输出图像中仍然是平行的
为了找到变换矩阵，我们需要输入图像中的三个点以及它们在输出图像中的相应位置。
*/
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv.getAffineTransform(pts1, pts2)
dst = cv.warpAffine(img, M, (cols, rows))
/*
透视转化 对于透视变换，您需要一个3x3变换矩阵。 即使在改造之后，直线仍将保持直线
要找到这个变换矩阵，您需要输入图像上的4个点和输出图像上的对应点。 在这4点中，其中3个不应该在线
然后可以通过函数cv2.getPerspectiveTransform找到变换矩阵
然后将cv2.warpPerspective应用于这个3x3转换矩阵
*/
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))
```

# 视频操作        
```
capture = cv2.VideoCapture(0)    
/* 参数可以是设备的索引号，或者是一个视频文件(没有声音)。
设备索引号就是在指定要使用的摄像头。 一般的笔记本电脑都有内置摄像头。所以参数就是 0。
你可以通过设置成 1 或 者其他的来选择别的摄像头
返回设备或视频文件的操作索引 */
ret, frame = capture.read() //获取相机图像，返回ret(结果为True/False)，和每一帧图片
frame = cv2.flip(frame, 1)  // 将图片水平翻转，竖直翻转为0
c = cv2.waitKey(50) 
// 如果你用的是64位系统，你需要将k = cv.waitKey(0)这行改成 k = cv.waitKey(0)&0xFF           
type(capture) //视频类型
capture.get(propId) // 获得视频的一些参数信息
capture.set(propId,value) // 修改，value 就是 你想要设置成的新值
fourcc = cv2.VideoWriter_fourcc('D', 'I','V', 'X')
/* FourCC 就是一个 4 字节码，用来确定视频的编码格式
可用的编码列表 可以从fourcc.org查到。这是平台依赖的
在Windows上常用的是DIVX。FourCC码以cv.VideoWriter_fourcc('D', 'I','V', 'X')形式传给程序*/
out = cv2.VideoWriter("output.avi", fourcc, 50.0, (640, 480))
// 输出视频名称，编码格式，播放频率，帧的大小
out.release() //类似于关闭文件
```

# 回调函数        
```
def myCallback(event,x,y,flags,param):
// event--触发事件时自动传入的事件
// x,y--鼠标此时的坐标
// flags--是否按下
// param--传入的参数表
```

# 事件判断        
```
event == cv.EVENT_LBUTTONDOWN  //鼠标左键是否被按下
event == cv.EVENT_LBUTTONUP //鼠标左键是否没被按下
flags == cv.EVENT_FLAG_LBUTTON //是否按下
```

# 时间相关        
```
t = cv2.getTickCount()  // 获取当前电脑时钟滴答数
f = cv2.getTickFrequency() // 获取当前电脑时钟滴答频率
time = (t2-t1)/f*1000 // 经过的毫秒数
```

# 颜色       
```
b, g, r = cv.split(image)  // b通道提取时，对该通道颜色保留，其余通道置为0
merge_image = cv.merge([b, g, r]) // 合并三个通道
```

# 像素操作        
```
dst = cv2.add(m1, m2) //像素相加
dst = cv2.subtract(m1, m2) //像素相减
dst = cv2.divide(m1, m2) //像素相除
dst = cv2.multiply(m1, m2) //像素相乘
M1 = cv2.mean(m1) //对像素做均值
dst = cv2.bitwise_not(image) //非运算
dst = cv2.addWeighted(image, c, blank, 1-c, b) //图像混合，c, 1-c为这两张图片的权重
```

# 模糊操作
## 噪声
- 椒盐噪声（Salt & Pepper）：含有随机出现的黑白亮度值。
- 脉冲噪声：只含有随机的正脉冲和负脉冲噪声。
- 高斯噪声：含有亮度服从高斯或正态分布的噪声。高斯噪声是很多传感器噪声的模型，如摄像机的电子干扰噪声

## 滤波器
### 线性滤波器
使用连续窗函数内像素加权和来实现滤波，同一模式的权重因子可以作用在每一个窗口内，即线性滤波器是空间不变的。
如果图像的不同部分使用不同的滤波权重因子，线性滤波器是空间可变的。因此可以使用卷积模板来实现滤波。      
线性滤波器对去除高斯噪声有很好的效果。常用的线性滤波器有均值滤波器和高斯平滑滤波器          
- 均值滤波器：最简单均值滤波器是局部均值运算，即每一个像素只用其局部邻域内所有值的平均值来置换.
- 高斯平滑滤波器是一类根据高斯函数的形状来选择权值的线性滤波器。 高斯平滑滤波器对去除服从正态分布的噪声是很有效的。

### 非线性滤波器
-  中值滤波器:均值滤波和高斯滤波运算主要问题是有可能模糊图像中尖锐不连续的部分。            
中值滤波器的基本思想使用像素点邻域灰度值的中值来代替该像素点的灰度值，它可以去除脉冲噪声、椒盐噪声同时保留图像边缘细节。
中值滤波不依赖于邻域内与典型值差别很大的值，处理过程不进行加权运算。        
中值滤波在一定条件下可以克服线性滤波器所造成的图像细节模糊，而对滤除脉冲干扰很有效。              
-  边缘保持滤波器:由于均值滤波：平滑图像外还可能导致图像边缘模糊和中值滤波：去除脉冲噪声的同时可能将图像中的线条细节滤除。边缘保持滤波器是在综合考虑了均值滤波器和中值滤波器的优缺点后发展起来的，它的特点是：滤波器在除噪声脉冲的同时，又不至于使图像边缘十分模糊。            
过程：分别计算[i，j]的左上角子邻域、左下角子邻域、右上角子邻域、右下角子邻域的灰度分布均匀度V；
然后取最小均匀度对应区域的均值作为该像素点的新灰度值。分布越均匀，均匀度V值越小。v=<(f(x, y) - f_(x, y))^2


# 模板匹配
```
def template_demo():
    tpl = cv.imread("rabbit.jpg")
    target = cv.imread("CrystalLiu22.jpg")
    cv.imshow("template", tpl)
    cv.imshow("target", target)

    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]  # 三种模板匹配方法
    th, tw = tpl.shape[:2]

    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)  # 得到匹配结果
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:  # cv.TM_SQDIFF_NORMED最小时最相似，其他最大时最相似
            tl = min_loc
        else:
            tl = max_loc

        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)  # tl为左上角坐标，br为右下角坐标，从而画出矩形
        cv.imshow("match-"+np.str(md), target)
```