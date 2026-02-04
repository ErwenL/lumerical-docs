<!-- Translation completed: 2026-02-04 -->
<!-- Original command: var -->

# var

**语法** | **描述**
---|---
out = var(A); | Will 返回 variance of all of 矩阵 A, over all 维度.

**示例**

These are some simple 示例 showing how to use this 命令. 
    a =[1,2,3,4,5];
    ?var(a);
    result: 
    2 
    b =[1,2,3,4,5; 5,4,3,2,1; 1,4,2,5,8];
    ?var(b);
    ?求和((b-平均值(b))^2)/长度(b); # Compare with equivalent calculation using 求和 and 平均值
    result: 
    3.55556
    result: 
    3.55556 
    d = randmatrix(3,3,3);
    ?d;
    result(i,j,1):
    0.345988 0.84698 0.271889 
    0.471725 0.316874 0.982971 
    0.374981 0.456099 0.2978 
    result(i,j,2):
    0.739189 0.761315 0.5009 
    0.567278 0.839442 0.890164 
    0.19599 0.397656 0.0274667 
    result(i,j,3):
    0.994629 0.531327 0.626759 
    0.572588 0.194067 0.657613 
    0.0505081 0.843043 0.197851 
    ?var(d);
    result: 
    0.0753581

These are some simple 示例 showing how to use this 命令. 
    a =[1,2,3,4,5];
    ?var(a);
    result: 
    2 
    b =[1,2,3,4,5; 5,4,3,2,1; 1,4,2,5,8];
    ?var(b);
    ?求和((b-平均值(b))^2)/长度(b); # Compare with equivalent calculation using 求和 and 平均值
    result: 
    3.55556
    result: 
    3.55556 
    d = randmatrix(3,3,3);
    ?d;
    result(i,j,1):
    0.345988 0.84698 0.271889 
    0.471725 0.316874 0.982971 
    0.374981 0.456099 0.2978 
    result(i,j,2):
    0.739189 0.761315 0.5009 
    0.567278 0.839442 0.890164 
    0.19599 0.397656 0.0274667 
    result(i,j,3):
    0.994629 0.531327 0.626759 
    0.572588 0.194067 0.657613 
    0.0505081 0.843043 0.197851 
    ?var(d);
    result: 
    0.0753581

**另请参阅**

[ std ](/hc/en-us/articles/360034406374-std) , [ mean ](/hc/en-us/articles/360034406314-mean) , [ sum ](/hc/en-us/articles/360034405694-sum) , [ length ](/hc/en-us/articles/360034925653-length)
