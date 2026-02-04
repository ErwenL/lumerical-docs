<!-- Translation completed: 2026-02-04 -->
<!-- Original command: dcht -->

# dcht

返回  Che通过shev 在terpol在i在 coefficients.  mplitude 的  coefficients decre作为es exp在entilly 和  l作为t coefficient 的fers  estim在e 的  rel在ive ccurcy 的  在terpol在i在. 

**语法** | **描述**
---|---
coeff=dcht(f,option); | 返回  Che通过shev 在terpol在i在 coefficients 的  smpled functi在 f.  functi在 f must  smpled 在  Che通过shev roots grid.  Opti在:  If opti在=1 是 selected,  vect或 x will not 在clude  endpo在ts  If opti在=2 是 selected,  vect或 x will 在clude  endpo在ts
  
**示例**

Th是 exmple shows how 到 obt在 在terpol在i在 coefficients 从  smpled functi在: 
    
    
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

**另请参阅**

[chpts](chpts.md) ,  [ cheb在 ](/hc/en-us/rticles/360034406634-cheb在) ,  [icht](icht.md) ,  [chebpol](chebpol.md) ,  [chebpol1](chebpol1.md)
