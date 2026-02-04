<!--
Translation from English documentation
Original command: chebpol1
Translation date: 2026-02-04 22:49:36
-->

# chebpol1

返回 该 first derivative 的 该 Chebyshev polynomials 的 该 first kind. 

**语法** |  **描述**  
---|---  
chebpol1(N,xi,xmin,xmax)  |  This 命令 generates 一个 矩阵 containing 该 Chebyshev polynomials 的 该 first kind 的 orders zero 到 N-1 evaluated at 该 xi points.   
  
**示例**

This example uses chebpol1 到 计算 该 first derivative 的 一个 函数 f sampled 在 一个 Chebishev grid. 
    
    
    clear;
    closeall;
    # Sample 函数 在 Chebyshev grid 
    xmin = 0.0;
    xmax = 1.0;
    Nc = 11;
    x = chpts(xmin,xmax,Nc);
    f = cos(2.0*pi*x)+1i*sin(2.0*pi*x); # 函数 和
    fp = -2.0*pi*sin(2*pi*x)+1i*2.0*pi*cos(2.0*pi*x); # its derivative
    Ni = 100;
    xi = linspace(xmin,xmax,Ni);
    # Function derivative 从 Chebyshev transform
    dchtf = dcht(f);
    Txp = chebpol1(长度(f),xi,xmin,xmax);
    fip = mult(Txp,dchtf);
    plot(xi,fip,"x","f'(x)","Function Derivative");
    holdon;
    plot(x,fp,"x","f'(x)","Function Derivative","plot points");
    holdoff;
    legend("Re - Interpolated","Im - Interpolated","Re - Exact","Im - Exact");
    setplot("y1 max",8);
    setplot("y1 min",-8);
    setplot("y2 max",8);
    setplot("y2 min",-8);

**参见**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chpts ](/hc/en-us/articles/360034406614-chpts) ,  [ icht ](/hc/en-us/articles/360034926853-chebpol1) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ chebpol ](/hc/en-us/articles/360034926833-chebpol)
