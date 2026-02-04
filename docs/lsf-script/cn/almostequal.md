<!-- Translation completed: 2026-02-04 -->
<!-- Original command: almostequal -->

# almostequal

**语法** | **描述**
---|---
out = almostequal(A, B); | 返回 1 if
out = almostequal(A, B, relative diff); | 返回 1 if
out = almostequal(A, B, relative diff, absolute diff); | 返回 1 if

**示例**

This 示例 shows the usage of the  almostequal  函数.
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

This 示例 shows the usage of the  almostequal  函数.
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

**另请参阅**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ = ](https://optics.ansys.com/hc/en-us/articles/360034929513--) , [ == ](https://optics.ansys.com/hc/en-us/articles/360034930893--) , [ != ](https://optics.ansys.com/hc/en-us/articles/360034930913--) , [ <= ](https://optics.ansys.com/hc/en-us/articles/360034410314--) , [ >= ](https://optics.ansys.com/hc/en-us/articles/360034930933--) , [ < ](https://optics.ansys.com/hc/en-us/articles/360034410334--) , [ > ](https://optics.ansys.com/hc/en-us/articles/360034930953--) , [ & ](https://optics.ansys.com/hc/en-us/articles/360034930973--) , [ and ](https://optics.ansys.com/hc/en-us/articles/360034410354-and) , [ | ](https://optics.ansys.com/hc/en-us/articles/360034410374--) , [ or ](https://optics.ansys.com/hc/en-us/articles/360034930993-or) , [ ! ](https://optics.ansys.com/hc/en-us/articles/360034931013--) , [ ~ ](https://optics.ansys.com/hc/en-us/articles/360034931033--)
