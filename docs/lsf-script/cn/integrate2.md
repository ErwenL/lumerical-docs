<!--
Translation from English documentation
Original command: integrate2
Translation date: 2026-02-04 22:50:01
-->

# integrate2

Very similar 到 该 standard integrate 函数, except 该 singleton dimensions 是 ignored. 

As described 在 该 integrate 函数 description, integrating over dimensions 使用 一个 single 值 (singleton dimensions) 返回 zero because 该 area under 一个 single point 是 zero. In some cases, particularly 当 you 是 not sure 该 dimensions 是 singleton, 此 behavior 可以 cause difficulties. The integrate2 函数 automatically ignores all dimensions 使用 一个 size 的 one, 该 avoids 该 problem 的 一个 zero valued integrals due 到 singleton dimensions. 

**语法** |  **描述**  
---|---  
out = integrate2(A, 1, x1);  |  Integrates A over 该 first 维度 在 该 矩阵.  x1 是 该 对应的 position 向量.   
out = integrate2(A, d, x1, x2, ...);  |  计算 该 integral 的 A over 该 specified 维度(s) d.  d 是 一个 向量 containing 该 dimensions over 该 到 integrate.  xi 是 该 position 向量 对应的 到 该 dimensions 的 A over 该 该 integration 是 occurring. If any 的 该 xi vectors only have 1 元素, integrate 返回 0.  For example 

  * power = integrate2(A,1:2,x,y) 将 integrate A over 一个 x-y surface. 

  
  
**示例**

In 该 following example, we compare 该 integrate 和 integrate2 commands 当 integrating over matrices 使用 singleton dimensions. 
    
    
    # 创建 3D 矩阵 的 results: 数据(x,y,z) 其中
    # there 是 50 'x' sample points, 1 'y' sample points
    # 和 40 'z' sample points. This 是 typical 的 数据
    # 从 一个 2D 监视器 oriented 在 该 XZ plane.
    x=linspace(-5,5,50);
    y=0;
    z=linspace(-3,3,40);
    X=meshgrid3dx(x,y,z);
    Z=meshgrid3dz(x,y,z);
    数据 = X^2 + Z^2;
    image(x,z,数据,"x","z","数据");
    ?integrate2(数据, [1,2,3], x,y,z); # Integrate2 ignores singleton 维度, giving non-zero result.
    ?integrate (数据, [1,2,3], x,y,z); # Result 是 zero because 的 该 singleton 维度
    ?integrate (数据, [1,3] , x,z ); # 获取 该 same result as integrate2 通过 integrating over x 和 z, but not y.
    > result: 
    > 680.653 
    > result: 
    > 0 
    > result: 
    > 680.653 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ integrate ](/hc/en-us/articles/360034405814-integrate) , [ conv2 ](/hc/en-us/articles/360034405854-conv2) , [ max ](/hc/en-us/articles/360034925693-max) , [ min ](/hc/en-us/articles/360034925713-min) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ find ](/hc/en-us/articles/360034405874-find) , [ pinch ](/hc/en-us/articles/360034405674-pinch) , [ round ](/hc/en-us/articles/360034406194-round) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ sum ](/hc/en-us/articles/360034405694-sum) , [ 长度 ](/hc/en-us/articles/360034925653-长度)
