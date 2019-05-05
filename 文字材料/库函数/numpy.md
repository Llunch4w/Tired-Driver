[toc]

这是一个比较全的快速了解numpy的网站[numpy tutorial of quickStart](https://www.numpy.org/devdocs/user/quickstart.html)，下面是我看这个教程后做的概括 


# numpy基础
- 主要对象：多维数组
- numpy中的维度称为axes，具体维度为axis
```
三维： axes 3
第一维： axis 1
```
- array中的array只有一维，而numpy中的array可以有多维
- numpy中的array也可以叫做ndarray

静态函数|功能|
|---|---|
ndarray.ndim|数组维度数目
ndarray.shape|数组维度
ndarray.size|数组元素总数
ndarray.dtype|元素类型
ndarray.itemsize|每个元素所占字节数
ndarray.data|