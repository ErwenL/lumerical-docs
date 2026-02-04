<!--
Translation from English documentation
Original command: var
Translation date: 2026-02-04 22:50:15
-->

# var

返回 该 variance 的 all entries 的 该 矩阵 specified. The variance 的 一个 设置 的 N numbers X = [x  1  ,...,x  N  ] 是 defined as 

$$ \text{var}=\frac{1}{N}\sum_{i=1}^N(x_i-\mu)^2 $$ 

其中  μ  是 该 mean 的 X. 

**语法** |  **描述**  
---|---  
out = var(A);  |  Will 返回 variance 的 all 的 矩阵 A, over all dimensions.   
  
**示例**

These 是 some simple examples showing 如何 到 use 此 命令. 
    
    
    一个 =[1,2,3,4,5];
    ?var(一个);
    result: 
    2 
    b =[1,2,3,4,5; 5,4,3,2,1; 1,4,2,5,8];
    ?var(b);
    ?sum((b-mean(b))^2)/长度(b); # Compare 使用 equivalent calculation 使用 sum 和 mean
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

**参见**

[ std ](/hc/en-us/articles/360034406374-std) , [ mean ](/hc/en-us/articles/360034406314-mean) , [ sum ](/hc/en-us/articles/360034405694-sum) , [ 长度 ](/hc/en-us/articles/360034925653-长度)
