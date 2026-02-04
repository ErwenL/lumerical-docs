<!--
Translation from English documentation
Original command: getresult
Translation date: 2026-02-04 22:50:00
-->

# getresult

获取 results 从 仿真 对象. Results 将 为 returned as datasets.

**语法** |  **描述**  
---|---  
?getresult("monitor_name"); |  返回 该 names 的 all 该 results 用于 该 监视器. All 该 dataset 和 scalar 矩阵 results 将 为 returned 在 此 case.  
R = getresult("monitor_name","T"); |  返回 该 result T 从 该 监视器. T 是 一个 dataset.  
  
**示例**

This example shows 如何 到 获取 该 electric field dataset 从 一个 监视器. We 那么 apply 一个 数字 的 operations 到 该 dataset, such as finding 该 maximum |E|^2 值, viewing 该 dataset 使用 该 visualizer, 和 creating 一个 plot 的 Ex at 该 first 频率 point.

注意 该 E 是 一个 dataset, rather than 一个 simple 矩阵 based 变量. Data within 该 dataset 可以 为 accessed 使用 该 '.' operator, as shown below.
    
    
    # 获取 Electric field dataset
    E=getresult("监视器","E");
    # output dataset 值 到 prompt
    ?E;
    # check size 的 position vectors 和 数据 matrices
    ?size(E.f);
    ?size(E.Ex);
    # find maximum |E|^2 值 
    ?max(E.E2);
    # view dataset 使用 visualizer
    visualize(E);
    # select first 频率 point 的 Ex 数据, 那么 创建 plot
    Ex = pinch(E.Ex,4,1); 
    image(E.x*1e6,E.y*1e6,Ex,"x (um)","y (um)","Ex");
     E vs x, y, z, lambda/f
     result: 
     5 1 
     result: 
     343 255 1 5 
     result: 
     3.223651 

**参见**

[ List 的 commands](/hc/en-us/articles/360037228834), [ haveresult](/hc/en-us/articles/360034409894-haveresult), [ Dataset introduction](/hc/en-us/articles/360034409554-Datasets), [ "." operator](/hc/en-us/articles/360034925773-dot), [ visualize](/hc/en-us/articles/360034410514-visualize), [ getdata](/hc/en-us/articles/360034409834-getdata), [ rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [ matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [ getattribute](/hc/en-us/articles/360034409534-getattribute), [ addattribute](/hc/en-us/articles/360034409494-addparameter), [ splitstring ](/hc/en-us/articles/360034926093-splitstring)
