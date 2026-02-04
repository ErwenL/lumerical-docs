<!--
Translation from English documentation
Original command: dcht
Translation date: 2026-02-03 22:29:31
-->

# dcht

返回切比雪夫插值系数。系数的幅度指数衰减，最后一个系数提供了插值的相对精度估计。 

**Syntax** |  **Description**  
---|---  
coeff=dcht(f,option);  |  返回采样函数f的切比雪夫插值系数。函数f必须在切比雪夫根网格上采样。选项：如果选择option=1，向量x将不包含端点；如果选择option=2，向量x将包含端点。   
  
 **示例**

此示例展示如何从采样函数获取插值系数： 
    
    
    Nc = 15;         # Number of sample points
    xmin = 0;
    xmax = 1;
    x = chpts(xmin,xmax,Nc,1); # Returns Chebyshev roots grid on interval between xmin and xmax
    f = exp(1i*2*pi*x);    # Function sampling using Chebyshev grid
    coeff = dcht(f,1);     # Get interpolation coefficients
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

- [chpts](./chpts.md)
 - [chebin](./chebin.md)
- [icht](./icht.md)
- [chebpol](./chebpol.md)
- [chebpol1](./chebpol1.md)
