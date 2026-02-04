<!--
Translation from English documentation
Original command: integrate
Translation date: 2026-02-04 22:50:01
-->

# integrate

返回 该 integral over 该 specified 维度 的 一个 矩阵. 

Integrals over singleton dimensions 将 返回 zero (i.e. 该 area under 一个 single point 是 zero). See integrate2 用于 一个 alternate behavior. 

**语法** |  **描述**  
---|---  
out = integrate(A, n, x1);  |  Integrates A over 该 nth 维度 在 该 矩阵.  x1 是 该 对应的 position 向量 用于 该 维度.   
out = integrate(A, d, x1, x2, ...);  |  计算 该 integral 的 A over 该 specified list 的 维度(s) d.  d 是 一个 向量 containing 该 dimensions over 该 到 integrate.  xi 是 该 position vectors 对应的 到 该 dimensions 的 A over 该 该 integration 是 occurring.  For example 

  * power = integrate(A,1:2,x,y) 将 integrate A over 一个 x-y surface. 

  
  
**示例**

In 该 following example, 该 integrate 命令 是 used 到 integrate y=x^2 从 0 到 3, 其中 该 函数 是 sampled at 该 points x=0,1,2,3. The integrate 函数 将 determine dx 从 该 position 向量 x. For reference, 该 值 的 此 integral 用于 该 continuous 函数 y=x^2 (as opposed 到 该 discrete samples 在 此 example) 是 9. Reducing dx 将 make 此 discrete integral approach 该 continuous result. 

Advanced note: The actual calculation 在 此 very simple example 将 为 0.5*0 + 1*1 + 1*4 + 0.5*9 = 9.5, as illustrated 在 该 figure below. It 是 interesting 到 note 该 该 first 和 last points have 一个 factor 的 0.5*dx because they 是 at 该 edge 的 该 integration range. Without 该 factor 的 0.5 applied 到 那些 points, 该 integral would effectively 为 calculated 从 x=-0.5 到 x=3.5 
    
    
    ?x=0:3;
    y=x^2;
    ?integrate(y,1,x);
    result: 
    0 
    1 
    2 
    3 
    result: 
    9.5 

Next, we demonstrate 该 该 integrate 函数 correctly treats non-uniform sampling. The portion 的 该 函数 从 0 到 2 是 evaluated 使用 一个 dx=1, while 一个 dx 的 0.2 是 used 从 2 到 3. In 此 case, 该 integrate 函数 将 计算 0.5*0 + 1*1 + 0.6*4 + 0.2*4.84 + 0.2*5.76 + 0.2*6.76 + 0.2*7.84 + 0.1*9; 
    
    
    ?x=[[0:1]; [2:0.2:3]];
    y=x^2;
    ?integrate(y,1,x);
    result: 
    0 
    1 
    2 
    2.2 
    2.4 
    2.6 
    2.8 
    3 
    result: 
    9.34 

Lastly, 此 example shows 如何 到 计算 该 power transmitted through 一个 y-normal 监视器 通过 integrating 该 Poynting 向量. To 获取 transmitted power, we want 到 integrate 该 real part 的 该 normal component 的 该 poynting 向量 (Py). The Py 数据 矩阵 将 have size N  x  x N  y  x N  z  x N  f  , 其中 Nx, Ny, Nz 是 该 数字 的 mesh point 在 each direction. If 该 监视器 是 Y-normal, Ny=1. Nf 是 该 数字 的 频率 points collected 通过 该 监视器. After integrating over 该 X 和 Z direction, we 是 basically left 使用 一个 1D 函数 的 该 transmitted power vs 频率. 
    
    
    Py = getdata("Monitor1","Py");
    x = getdata("Monitor1","x");
    y = getdata("Monitor1","y");
    z = getdata("Monitor1","z");
    f = getdata("Monitor1","f");
    power = 0.5 * integrate( real(Py), [1,3], x,z );

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ integrate2 ](/hc/en-us/articles/360034405834-integrate2) , [ conv2 ](/hc/en-us/articles/360034405854-conv2) , [ max ](/hc/en-us/articles/360034925693-max) , [ min ](/hc/en-us/articles/360034925713-min) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ find ](/hc/en-us/articles/360034405874-find) , [ pinch ](/hc/en-us/articles/360034405674-pinch) , [ round ](/hc/en-us/articles/360034406194-round) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ sum ](/hc/en-us/articles/360034405694-sum) , [ 长度 ](/hc/en-us/articles/360034925653-长度)
