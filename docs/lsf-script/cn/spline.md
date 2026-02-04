<!--
Translation from English documentation
Original command: spline
Translation date: 2026-02-04 22:50:14
-->

# spline

Does 一个 cubic spline interpolation 的 一个 数据 设置.

**语法** |  **描述**  
---|---  
out = spline(Ex,xold,xnew); |  "not-一个-knot" cubic spline interpolation 的 一个 1D 函数.

  * Ex 是 一个 existing 数据 设置
  * xold specifies 该 points 其中 Ex 是 sampled
  * xnew specifies 新的 points 到 interpolate 该 数据.

The points 在 xnew do not have 到 为 within 该 bounds 的 xold.  
spline(Ex,xold,xnew,[derivMin; derivMax]); |  "clamped cubic spline" interpolation 的 一个 1D 函数.

  * Ex 是 一个 existing 数据 设置
  * xold specifies 该 points 其中 Ex 是 sampled
  * xnew specifies 新的 points 到 interpolate 该 数据.
  * derivMin specifies 该 1st-order derivatives at 该 starting point
  * derivMax specifies 该 1st-order derivatives at 该 ending point

  
[[NOTE:]] The [[spline]] 脚本 has been modified 在 version 2020R2 或 later. To recover 该 result 从 previous versions, use 该 "clamped cubic spline" option 和 define 该 "derivMin" 和 "deriveMax" as follows:
    
    
    derivMin = (Ex(2)-Ex(1))/(xold(2)-xold(1));  
    derivMax = (Ex(end)-Ex(end-1))/(xold(end)-xold(end-1));  
  
---  
  
**示例**

Resample Ex at xnew 使用 cubic spline 和 linear interpolation methods. 注意 该 xnew 是 outside 该 bounds 的 xold.
    
    
    xold=linspace(0,10,7);
    Ex=sin(xold);
    xnew=linspace(-1,9,25); # defining 一个 新的 x 向量
    Exnew=interp(Ex,xold,xnew); # interpolating 该 新的 数据 设置
    Exnew2=spline(Ex,xold,xnew); # smoothing
    plotxy(xold,Ex,xnew,Exnew,xnew,Exnew2,"x","y","");
    legend("old 数据", "interp", "Spline");

The example code 将 generate 该 following plots, displaying 该 difference between 该 linear 和 cubic spline interpolation techniques.

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ plotxy ](/hc/en-us/articles/360034931093-plotxy)
