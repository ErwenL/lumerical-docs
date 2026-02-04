<!--
Translation from English documentation
Original command: chpts
Translation date: 2026-02-04 22:49:48
-->

# chpts

Samples 函数 在 一个 Chebyshev grid. Chebyshev interpolation 是 useful 用于 accurately interpolating 一个 smooth 函数 使用 一个 very small 数字 的 samples. The key requirement 用于 此 类型 的 interpolation 到 work 是 该 该 函数 是 sampled 在 该 Chebyshev roots grid, 该 可以 为 done 通过 使用 此 命令. 

**语法** |  **描述**  
---|---  
x=chpts(xmin,xmax,NumPts,option);  |  返回 Chebyshev roots grid 在 interval between xmin 和 xmax 该 可以 为 used 到 sample 一个 smooth 函数.  NumPts defines 该 数字 的 points 在 given interval.  Option:  If option=1 是 选中的, 该 向量 x 将 not include 该 endpoints  If option=2 是 选中的, 该 向量 x 将 include 该 endpoints   
  
**示例**

This example uses 该 chpts 到 sample 一个 smooth 函数 在 一个 interval 从 0 到 1 使用 7 points. The 函数 是 那么 interpolated 使用 chebin 命令 和 compared 使用 该 original sampled 函数. 
    
    
    # Sample 函数 在 Chebyshev grid
    xmin = 0;
    xmax = 1;
    Nc = 7;
    x = chpts(xmin,xmax,Nc,1);
    f = exp(1i*2*pi*x);
    ###############################################################
    # Interpolation 和 comparison 到 该 original sampled 函数
    # Fine sampling 用于 display
    Ni = 500;
    xi = linspace(xmin,xmax,Ni);
    fi = exp(1i*2*pi*xi);
    # Plot 函数 和 its samples 在 该 Chebyshev grid
    plot(xi,fi,"x","f(x)","Original Function");
    holdon;
    plot(x,f,"x","f(x)","Original Function","plot points");
    holdoff;
    legend("Re(f(x))","Im(f(x))","Re Cheb","Im Cheb");
    setplot("y最大值",1);
    setplot("y最小值",-1);
    # Chebyshev interpolation
    fi = chebin(f,x,xi,xmin,xmax);
    # Plot 函数 和 its samples 在 该 Chebyshev grid
    plot(xi,fi,"x","f(x)","Interpolated Function");
    holdon;
    plot(x,f,"x","f(x)","Interpolated Function","plot points");
    holdoff;
    legend("Re(f(x))","Im(f(x))","Re Cheb","Im Cheb");
    setplot("y最大值",1);
    setplot("y最小值",-1);

**参见**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ icht ](/hc/en-us/articles/360034406614-chpts) , [ interp ](/hc/en-us/articles/360034925893-interp)
