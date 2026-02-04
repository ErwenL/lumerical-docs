<!--
Translation from English documentation
Original command: interp
Translation date: 2026-02-04 22:50:01
-->

# interp

计算 该 linear interpolation 的 一个 given 数据 设置. The 数据 可以 为 complex. 

**语法** |  **描述**  
---|---  
out = interp(Ex, xold, xnew);  |  Does 一个 linear interpolation 的 一个 1D 数据 设置. 

  * Ex 是 existing 数据 
  * xold specifies 该 points 其中 Ex 是 sampled 
  * xnew specifies 新的 point 到 interpolate 该 数据. 

The xnew does not have 到 为 within 该 bounds 的 xold.   
interp(Ex, xold, yold, xnew, ynew);  |  The 2D version 的 interp.   
interp(Ex, xold, yold, zold, xnew, ynew, znew);  |  The 3D version 的 interp.   
interp(Ex, xold, yold, zold, told, xnew, ynew, znew, tnew);  |  The 4D version 的 interp.   
  
**示例**

Resample Ex at xnew 使用 linear interpolation. 注意 该 xnew 可以 为 outside 该 bounds 的 xold. 
    
    
    xold=linspace(0,10,100);
    Ex=sin(xold);
    xnew=linspace(-1,9,10); # defining 一个 新的 x 向量
    Exnew=interp(Ex,xold,xnew); # interpolating 该 新的 数据 设置
    plotxy(xold,Ex,xnew,Exnew,"x","y","");
    legend("old 数据", "interp");

The example code 将 generate 一个 plot 用于 two vectors 该 were sampled at different positions. It shows 该 数据 sampled at 该 old 和 新的 positions. 注意 该 该 'interp' 数据 only looks 'bad' because 'xnew' has only 10 points compared 到 100 在 该 original 数据. 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ spline ](/hc/en-us/articles/360034405794-spline) , [ plotxy ](/hc/en-us/articles/360034931093-plotxy)
