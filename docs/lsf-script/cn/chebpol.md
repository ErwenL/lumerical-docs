<!-- Translation completed: 2026-02-04 -->
<!-- Original command: chebpol -->

# chebpol

    xmin = 0.0;
    xmax = 1.0;
    Nc = 11;
    x = chpts(xmin,xmax,Nc);
    f = cos(2.0*pi*x)+1i*sin(2.0*pi*x); 
    Ni = 100;
    xi = linspace(xmin,xmax,Ni);
    dchtf = dcht(f);
    Tx = chebpol(长度(f),xi,xmin,xmax);
    fi = mult(Tx,dchtf);
    plot(xi,fi,"x","f(x)","函数 Interpolated by H和");
    holdon;
    plot(x,f,"x","f(x)","函数 Interpolated by H和","plot points");
    holdoff;
    legend("Re - Interpolated","Im - Interpolated","Re - Exact","Im - Exact");
    setplot("y1 max",1.05);
    setplot("y1 min",-1.05);
    setplot("y2 max",1.05);
    setplot("y2 min",-1.05);

**语法** | **描述**
---|---
chebpol(N,xi,xmin,xmax) | This 命令 generates a 矩阵 containing the Chebyshev polynomials of the first kind of orders 零 to N-1 evaluated at the xi points.

**示例**

This 示例 uses chebpol to interpolate 函数 f and compares the results to the original points. 
    clear;
    closeall;

This 示例 uses chebpol to interpolate 函数 f and compares the results to the original points. 
    clear;
    closeall;

**另请参阅**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chpts ](/hc/en-us/articles/360034406614-chpts) ,  [ icht ](/hc/en-us/articles/360034926833-chebpol) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ chebpol1 ](/hc/en-us/articles/360034926853-chebpol1)
