<!--
Translation from English documentation
Original command: pinch
Translation date: 2026-02-04 22:50:14
-->

# pinch

Removes singleton dimensions 从 一个 矩阵.

**语法** |  **描述**  
---|---  
out = pinch(x); |  Removes all singleton dimensions. For example, 如果 x 是 一个 矩阵 的 维度 1x1x1xM, 那么

  * y=pinch(x);

将 返回 一个 Mx1 矩阵 其中

  * y(i) = x(1,1,1,i);

  
pinch(x,i); |  Removes 一个 specified 维度. If x 是 一个 NxMxKxP 矩阵 那么

  * y=pinch(x,2);

将 返回 一个 NxKxP 矩阵 其中

  * y(i,j,k) = x(i,1,j,k)

  
pinch(x,i,j); |  Removes 一个 specified 维度 but keeps 一个 specific index 用于 该 维度 being removed. If x 是 一个 NxMxKxP 矩阵 那么

  * y=pinch(x,2,4);

将 返回 一个 NxKxP 矩阵 其中

  * y(i,j,k) = x(i,4,j,k)

  
  
**示例**

This example shows 如何 pinch 可以 为 used 到 remove singleton dimensions 从 一个 矩阵. The 矩阵 命令 是 used 到 创建 一个 6x1x4x1 矩阵. Applying 该 pinch 函数 到 此 矩阵 将 remove 该 two singleton dimensions, resulting 在 一个 6x4 矩阵.
    
    
    x=矩阵(6,1,4,1);
    ?size(x);
    result: 
    6 1 4 1 
    ?size(pinch(x));
    result: 
    6 4 

Suppose 该 power 监视器 named "field" 是 一个 2D 监视器 在 该 XY plane 设置 到 record multiple 频率 points between 200THz 和 300THz. In 此 case, 该 变量 Ex 将 为 一个 4D 矩阵, 其中 该 dimensions 是 长度(X) 通过 长度(Y) 通过 长度(Z) 通过 长度(F). Since 此 是 一个 2D 监视器 在 该 XY plane, there 将 为 only one Z position, 该 means 该 长度 的 该 third 维度 (Z) 将 为 1.

With 该 pinch 和 find commands, we 可以 select 一个 particular 频率 到 为 imaged. First, 该 find 命令 是 used 到 determine 该 index 的 该 频率 值 closest 到 250THz. Next, 该 pinch 命令 是 used 到 select 该 数据 在 Ex 对应的 到 该 频率. A second pinch 命令 是 used 到 remove 该 singleton Z 维度. The end result 是 该 2D 矩阵 Ex(x,y) at 一个 specific 值 的 z 和 f.
    
    
    m="field";      # 监视器 name
    x=getdata(m,"x");  # 获取 监视器 数据
    y=getdata(m,"y");
    z=getdata(m,"z");
    f=getdata(m,"f");
    Ex=getdata(m,"Ex");
    fi=find(f,250e12);  # find 该 index 该 corresponds 到 f=250THz
    Ex=real(Ex);     # take real part 的 Ex    
    ?"Size 的 x: "+num2str(长度(x)); # print 该 矩阵 size 到 该 screen
    ?"Size 的 y: "+num2str(长度(y));
    ?"Size 的 z: "+num2str(长度(z));
    ?"Size 的 f: "+num2str(长度(f));
    ?"Size 的 Ex: "+num2str(size(Ex));
    to_plot=pinch(Ex,4,fi);   # select 频率. Size 将 为 长度(x) 通过 长度(y) 通过 长度(z)
    to_plot=pinch(to_plot);   # remove singleton z 维度. Size 将 为 长度(x) 通过 长度(y)
    image(x*1e6,y*1e6,to_plot, "x (um)","y (um)","Ex at "+num2str(f(fi)/1e12)+ " THz" ); 

**参见**

[ List 的 commands](/hc/en-us/articles/360037228834), [ find](/hc/en-us/articles/360034405874-find), [ size](/hc/en-us/articles/360034405654-size), [ flip](/hc/en-us/articles/360034925833-flip)
