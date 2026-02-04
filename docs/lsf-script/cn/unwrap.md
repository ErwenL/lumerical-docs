<!-- Translation: unwrap -->
<!-- Date: 2026-02-03 -->
<!-- Original: unwrap -->

# unwrap

从1D数组中移除超过2π的变化。在angle(x)之后使用它可以查看没有间断的相位。

unwrap函数主要用于1D数组。在将其应用于多维矩阵时必须小心。

**语法** | **说明**
---|---
out = unwrap(x); | 返回x的值，没有间断。

**示例**

对1D数组应用unwrap函数。


    vec=linspace(0,10,100);
    A=cos(vec) + sin(vec)*1i;
    B=angle(A);
    C=unwrap(B);
    plot(vec,real(A),B,C);
    legend("cos(x)","angle", "unwrap");

将生成以下图形：

对2D矩阵应用unwrap函数。unwrap函数会将2D矩阵视为1D向量（即连接每一行），这意味着第2行的展开相位将从第一行末端的相位开始。注意矩阵D的所有5行的值都是相同的，但在应用unwrap函数后，线条相互"堆叠"。这是因为unwrap将矩阵视为一个大的1D数组，而不是独立处理每一行。


    vec=linspace(0,10,100);
    A=cos(vec) + sin(vec)*1i; # 创建复数正弦波
    B=1:5;          # 从1到5的向量
    C=meshgridx(A,B);     # 具有5个正弦波副本的2D矩阵
    D=angle(C);        # 获取矩阵的角度
    image(vec,B,D,"vec","5 copies","angle");  # 矩阵的图像图
    plot(vec,D,"vec","angle");         # 线图（所有5条线相同）
    legend("row 1","row 2","row 3","row 4","row 5");
    plot(vec,unwrap(D),"vec","unwrap angle"); # unwrap。现在线条堆叠在一起
    legend("row 1","row 2","row 3","row 4","row 5");

要以2D方式（而不是将其视为单个大的1D向量）将unwrap函数应用于2D相位数据，请参见以下示例。必须一次将unwrap函数应用于一行，然后一次应用于一列。

注意：2D展开操作是非平凡的。此示例代码在某些情况下有效，但并非总是如此。请进行一些测试以确定它是否适用于您的应用。


    x=linspace(-5,5,100); y=x;
    nx=length(x); ny=length(y);
    data = exp( 1i* (meshgridx(x,y)+meshgridy(x,y)) );
    phase = angle(data); 
    image(x,y,phase,"x","y","raw phase (rad)");
    # 在两个维度上展开
    for (i=1:nx) {
     phase(i,1:ny) = unwrap( pinch(phase,1,i) );
    }
    for (j=1:ny) {
     phase(1:nx,j) = unwrap( pinch(phase,2,j) );
    }
    image(x,y,phase,"x","y","unwrapped phase (rad)"); 

**参见**

[命令列表](./360037228834.md), [real](./real.md), [imag](./imag.md), [angle](./angle.md)
