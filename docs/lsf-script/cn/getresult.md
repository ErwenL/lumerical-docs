<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getresult -->

# getresult

    E=getresult("监视器","E");
    ?E;
    ?大小(E.f);
    ?大小(E.Ex);
    ?max(E.E2);
    visualize(E);
    Ex = 压缩(E.Ex,4,1); 
    image(E.x*1e6,E.y*1e6,Ex,"x (um)","y (um)","Ex");
     E vs x, y, z, lambda/f
     result: 
     5 1 
     result: 
     343 255 1 5 
     result: 
     3.223651 

**语法** | **描述**
---|---
?getresult("monitor_name"); | 返回 the names of all the results for the 监视器. All the 数据集 and scalar 矩阵 results will be returned in this case.
R = getresult("monitor_name","T"); | 返回 the result T from the 监视器. T is a 数据集.

**示例**

This 示例 shows how to get the electric 场 数据集 from a 监视器. We then apply a 数字 of operations to the 数据集, such as finding the 最大值 |E|^2 值, viewing the 数据集 with the visualizer, and creating a plot of Ex at the first 频率 point.
注意 that E is a 数据集, rather than a simple 矩阵 based 变量. Data within the 数据集 can be accessed with the '.' 运算符, as shown below.

This 示例 shows how to get the electric 场 数据集 from a 监视器. We then apply a 数字 of operations to the 数据集, such as finding the 最大值 |E|^2 值, viewing the 数据集 with the visualizer, and creating a plot of Ex at the first 频率 point.
注意 that E is a 数据集, rather than a simple 矩阵 based 变量. Data within the 数据集 can be accessed with the '.' 运算符, as shown below.

**另请参阅**

[ List of commands](/hc/en-us/articles/360037228834), [ haveresult](/hc/en-us/articles/360034409894-haveresult), [ Dataset introduction](/hc/en-us/articles/360034409554-Datasets), [ "." operator](/hc/en-us/articles/360034925773-dot), [ visualize](/hc/en-us/articles/360034410514-visualize), [ getdata](/hc/en-us/articles/360034409834-getdata), [ rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [ matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [ getattribute](/hc/en-us/articles/360034409534-getattribute), [ addattribute](/hc/en-us/articles/360034409494-addparameter), [ splitstring ](/hc/en-us/articles/360034926093-splitstring)
