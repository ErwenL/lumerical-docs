<!--
Translation from English documentation
Original command: interp
Translation date: 2026-02-03
-->

# interp

计算给定数据集的线性插值。数据可以是复数。

**语法** |  **描述**
---|---
out = interp(Ex, xold, xnew);  |  对 1D 数据集进行线性插值。

  * Ex 是现有数据
  * xold 指定 Ex 被采样的点
  * xnew 指定要插值数据的新点

xnew 不必在 xold 的范围内。
interp(Ex, xold, yold, xnew, ynew);  |  interp 的 2D 版本。
interp(Ex, xold, yold, zold, xnew, ynew, znew);  |  interp 的 3D 版本。
interp(Ex, xold, yold, zold, told, xnew, ynew, znew, tnew);  |  interp 的 4D 版本。

**示例**

使用线性插值在 xnew 处对 Ex 进行重新采样。请注意，xnew 可以在 xold 的范围之外。

    xold=linspace(0,10,100);
    Ex=sin(xold);
    xnew=linspace(-1,9,10); # defining a new x vector
    Exnew=interp(Ex,xold,xnew); # interpolating the new data set
    plotxy(xold,Ex,xnew,Exnew,"x","y","");
    legend("old data", "interp");

示例代码将为在不同位置采样的两个向量生成一个图形。它显示了在旧位置和新位置采样的数据。请注意，"interp" 数据看起来"糟糕"只是因为 "xnew" 只有 10 个点，而原始数据有 100 个点。

**相关命令**

- [List of commands](./List-of-commands.md)
- [spline](./spline.md)
- [plotxy](./plotxy.md)
