<!--
Translation from English documentation
Original command: dcht
Translation date: 2026-02-04 22:49:48
-->

# dcht

返回 该 Chebyshev interpolation coefficients. The amplitude 的 该 coefficients decreases exponentially 和 该 last coefficient offers 一个 estimate 的 该 relative accuracy 的 该 interpolation. 

**语法** |  **描述**  
---|---  
coeff=dcht(f,option);  |  返回 该 Chebyshev interpolation coefficients 的 一个 sampled 函数 f. The 函数 f 必须 为 sampled 在 一个 Chebyshev roots grid.  Option:  If option=1 是 选中的, 该 向量 x 将 not include 该 endpoints  If option=2 是 选中的, 该 向量 x 将 include 该 endpoints   
  
**示例**

This example shows 如何 到 obtain interpolation coefficients 从 一个 sampled 函数: 
    
    
    Nc = 15;         # Number 的 sample points
    xmin = 0;
    xmax = 1;
    x = chpts(xmin,xmax,Nc,1); # 返回 Chebyshev roots grid 在 interval between xmin 和 xmax
    f = exp(1i*2*pi*x);    # Function sampling 使用 Chebyshev grid
    coeff = dcht(f,1);     # 获取 interpolation coefficients
    ?abs(coeff);
    result: 
    0.304242  
    0.569231  
    0.970868  
    0.666917  
    0.302849  
    0.104282  
    0.0290919  
    0.00684063  
    0.00139224  
    0.000250007  
    4.01899e-005  
    5.85025e-006  
    7.78278e-007  
    9.53372e-008  
    1.094e-008      

**参见**

[ chpts ](/hc/en-us/articles/360034406614-chpts) ,  [ chebin ](/hc/en-us/articles/360034406634-chebin) ,  [ icht ](/hc/en-us/articles/360034406734-dcht) ,  [ chebpol ](/hc/en-us/articles/360034926833-chebpol) ,  [ chebpol1 ](/hc/en-us/articles/360034926853-chebpol1)
