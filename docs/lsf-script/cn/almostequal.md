<!--
Translation from English documentation
Original command: almostequal
Translation date: 2026-02-04 22:49:36
-->

# almostequal

Performs 一个 almost-equal comparison. When 使用 floating point numbers (rather than integers), two 值 该 是 meant 到 为 equal 可能 not 为 exactly equal due 到 rounding errors 该 是 always present 在 floating point calculations. In such cases, 该  almostequal  函数 可以 为 useful. For complex numbers, A 和 B, almostequal  函数 返回 true only 当 both 该 real 和 imaginary parts, evaluated separately, 是 true.

**语法** |  **描述**  
---|---  
out = almostequal(A, B); |  返回 1 如果 |A - B| 是 less than 或 equal 到 |A + B|/2*1e-15. 返回 0 otherwise.  
out = almostequal(A, B, relative diff); |  返回 1 如果 |A - B| 是 less than 或 equal 到 |A + B|/2 times relative diff. 返回 0 otherwise.  
out = almostequal(A, B, relative diff, absolute diff); |  返回 1 如果 |A - B| 是 less than 或 equal 到 |A + B|/2 times relative diff 或 如果 |A - B| 是 less than 或 equal 到 absolute diff. 返回 0 otherwise.  
  
**示例**

This example shows 该 usage 的 该  almostequal  函数.
    
    
    A=[1,2];
    B=[1,1];
    ?almostequal(A,B);
    result: 
    1 0 
    ?almostequal(A,B,0.01,2);
    result: 
    1 1 
     
    ?almostequal(1,2,1);
    result: 
    1   

**参见**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ = ](https://optics.ansys.com/hc/en-us/articles/360034929513--) , [ == ](https://optics.ansys.com/hc/en-us/articles/360034930893--) , [ != ](https://optics.ansys.com/hc/en-us/articles/360034930913--) , [ <= ](https://optics.ansys.com/hc/en-us/articles/360034410314--) , [ >= ](https://optics.ansys.com/hc/en-us/articles/360034930933--) , [ < ](https://optics.ansys.com/hc/en-us/articles/360034410334--) , [ > ](https://optics.ansys.com/hc/en-us/articles/360034930953--) , [ & ](https://optics.ansys.com/hc/en-us/articles/360034930973--) , [ and ](https://optics.ansys.com/hc/en-us/articles/360034410354-and) , [ | ](https://optics.ansys.com/hc/en-us/articles/360034410374--) , [ or ](https://optics.ansys.com/hc/en-us/articles/360034930993-or) , [ ! ](https://optics.ansys.com/hc/en-us/articles/360034931013--) , [ ~ ](https://optics.ansys.com/hc/en-us/articles/360034931033--)
