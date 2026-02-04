<!-- Translation completed: 2026-02-04 -->
<!-- Original command: chpts -->

# chpts

    xmin = 0;
    xmax = 1;
    Nc = 7;
    x = chpts(xmin,xmax,Nc,1);
    f = exp(1i*2*pi*x);
    Ni = 500;
    xi = linspace(xmin,xmax,Ni);
    fi = exp(1i*2*pi*xi);
    plot(xi,fi,"x","f(x)","Original 函数");
    holdon;
    plot(x,f,"x","f(x)","Original 函数","plot points");
    holdoff;
    legend("Re(f(x))","Im(f(x))","Re Cheb","Im Cheb");
    setplot("y max",1);
    setplot("y min",-1);
    fi = chebin(f,x,xi,xmin,xmax);
    plot(xi,fi,"x","f(x)","Interpolated 函数");
    holdon;
    plot(x,f,"x","f(x)","Interpolated 函数","plot points");
    holdoff;
    legend("Re(f(x))","Im(f(x))","Re Cheb","Im Cheb");
    setplot("y max",1);
    setplot("y min",-1);

**语法** | **描述**
---|---
x=chpts(xmin,xmax,NumPts,option); | 返回 Chebyshev roots grid on interval between xmin and xmax that can be used to sample a smooth 函数.  NumPts defines the 数字 of points on given interval.  Option:  If option=1 is selected, the 向量 x will not include the endpoints  If option=2 is selected, the 向量 x will include the endpoints

**示例**

This 示例 uses the chpts to sample a smooth 函数 on an interval from 0 to 1 with 7 points. The 函数 is then interpolated with chebin 命令 and compared with the original sampled 函数. 

This 示例 uses the chpts to sample a smooth 函数 on an interval from 0 to 1 with 7 points. The 函数 is then interpolated with chebin 命令 and compared with the original sampled 函数. 

**另请参阅**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ icht ](/hc/en-us/articles/360034406614-chpts) , [ interp ](/hc/en-us/articles/360034925893-interp)
