<!-- Translation completed: 2026-02-04 -->
<!-- Original command: chebpol1 -->

# chebpol1

    xmin = 0.0;
    xmax = 1.0;
    Nc = 11;
    x = chpts(xmin,xmax,Nc);
    f = cos(2.0*pi*x)+1i*sin(2.0*pi*x); # 函数 和
    fp = -2.0*pi*sin(2*pi*x)+1i*2.0*pi*cos(2.0*pi*x); # its derivative
    Ni = 100;
    xi = linspace(xmin,xmax,Ni);
    dchtf = dcht(f);
    Txp = chebpol1(长度(f),xi,xmin,xmax);
    fip = mult(Txp,dchtf);
    plot(xi,fip,"x","f'(x)","函数 Derivative");
    holdon;
    plot(x,fp,"x","f'(x)","函数 Derivative","plot points");
    holdoff;
    legend("Re - Interpolated","Im - Interpolated","Re - Exact","Im - Exact");
    setplot("y1 max",8);
    setplot("y1 min",-8);
    setplot("y2 max",8);
    setplot("y2 min",-8);

**语法** | **描述**
---|---
chebpol1(N,xi,xmin,xmax) | This 命令 generates a 矩阵 containing the Chebyshev polynomials of the first kind of orders 零 to N-1 evaluated at the xi points.

**示例**

This 示例 uses chebpol1 to 计算 the first derivative of a 函数 f sampled on a Chebishev grid. 
    clear;
    closeall;

This 示例 uses chebpol1 to 计算 the first derivative of a 函数 f sampled on a Chebishev grid. 
    clear;
    closeall;

**另请参阅**

[ dcht ](/hc/en-us/articles/360034406734-dcht) ,  [ chpts ](/hc/en-us/articles/360034406614-chpts) ,  [ icht ](/hc/en-us/articles/360034926853-chebpol1) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ chebpol ](/hc/en-us/articles/360034926833-chebpol)
