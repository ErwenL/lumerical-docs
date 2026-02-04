<!--
Translation from English documentation
Original command: amin
Translation date: 2026-02-04 22:49:36
-->

# amin

返回 该 minimum 值 在 一个 specified 维度 的 一个 矩阵. For complex numbers, only 该 real part 是 considered. 

**语法** |  **描述**  
---|---  
out = amin(x,n);  |  The minimum 值 在 该 specified 维度 n 的 矩阵 x.   
  
**示例**

Find 该 minimum 值 的 该 first 维度 的 一个 矩阵: 
    
    
    A = randmatrix(5,4);
    B = amin(A,1); # 向量 长度 4, B[i] = min(A(1:5,i))

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ min ](/hc/en-us/articles/360034925713-min) , [ max ](/hc/en-us/articles/360034925693-max) , [ abs ](/hc/en-us/articles/360034925553-abs) , [ mean ](/hc/en-us/articles/360034406314-mean) , [ amax ](/hc/en-us/articles/360034925733-amax)
