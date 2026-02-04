<!--
Translation from English documentation
Original command: chebpol
Translation date: 2026-02-04 22:49:36
-->

# chebpol

Generates 该 Chebyshev polynomials 的 该 first kind. This 命令 可以 为 used 在 combination 使用 dcht 到 计算 该 Chebyshev interpolation. Compared 到 该 chebin 命令, 使用 chebpol 用于 该 interpolation offers additional control over 该 interpolation process as it allows 该 用户 到 specify 该 polynomial order. 

**语法** |  **描述**  
---|---  
chebpol(N,xi,xmin,xmax)  |  This 命令 generates 一个 矩阵 containing 该 Chebyshev polynomials 的 该 first kind 的 orders zero 到 N-1 evaluated at 该 xi points.   
  
**示例**

This example uses chebpol 到 interpolate 函数 f 和 compares 该 results 到 该 original points. 
    
    
    clear;
    closeall;
    # Sample 函数 在 Chebyshev grid 
    xmin = 0.0;
    xmax = 1.0;
    Nc = 11;
    x = chpts(xmin,xmax,Nc);
    f = cos(2.0*pi*x)+1i*sin(2.0*pi*x); 
    Ni = 100;
    xi = linspace(xmin,xmax,Ni);
    # Chebyshev interpolation done 通过 hand
    dchtf = dcht(f);
    Tx = chebpol(长度(f),xi,xmin,xmax);
    fi = mult(Tx,dchtf);
    plot(xi,fi,"x","f(x)","Function Interpolated 通过 Hand");
    holdon;
    plot(x,f,"x","f(x)","Function Interpolated 通过 Hand","plot points");
    holdoff;
    legend("Re - Interpolated","Im - Interpolated","Re - Exact","Im - Exact");
    setplot("y1 max",1.05);
    setplot("y1 min",-1.05);
    setplot("y2 max",1.05);
    setplot("y2 min",-1.05);

**参见**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chpts ](/hc/en-us/articles/360034406614-chpts) ,  [ icht ](/hc/en-us/articles/360034926833-chebpol) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ chebpol1 ](/hc/en-us/articles/360034926853-chebpol1)
