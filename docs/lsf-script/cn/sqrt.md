<!--
Translation from English documentation
Original command: sqrt
Translation date: 2026-02-04 22:50:15
-->

# sqrt

计算 该 square root 的 一个 数字. Input 可以 为 complex 或 negative. 

**语法** |  **描述**  
---|---  
out = sqrt(x);  |  The square root 的 x. The square root 是 chosen so 该 real(sqrt(x))≥0 用于 any complex 数字 x. The imaginary part, imag(sqrt(x)), 可以 为 positive 或 negative but 如果 real(sqrt(x))=0 那么 imag(sqrt(x))≥0.   
  
**示例**

计算 该 square root 的 一个 数字. 
    
    
    ?sqrt(4);
    result: 
    2 

The square root 函数 的 z = x + iy 在 该 complex plane has 一个 branch cut at (-∞,0], as shown 在 该 following example. 
    
    
    x = linspace(-1,1,100);
    y = linspace(-1,1,100);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    image(x,y,real(sqrt(X+1i*Y)),"x", "y","Real part 的 sqrt(x+iy)");
    image(x,y,imag(sqrt(X+1i*Y)),"x", "y","Imaginary part 的 sqrt(x+iy)");

|   
---|---  
  
**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ ^ ](/hc/en-us/articles/360034410274--)
