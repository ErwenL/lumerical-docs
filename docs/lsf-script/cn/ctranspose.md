<!--
Translation from English documentation
Original command: ctranspose
Translation date: 2026-02-03 10:49:39
-->

# ctranspose

转置一维或二维矩阵并取每个元素的复共轭。结果矩阵是共轭转置或Hermitian转置。 

**Syntax** |  **Description**  
---|---  
y = ctranspose(x);  |  如果 x 是 N x M 矩阵，则 y 将是 M x N，其中元素 y(j,i)=x(i,j) 的共轭。   
  
**Example**

如何求二维复矩阵的共轭转置的简单示例。 
    
    
    ?B = [1+3i,2,3+7i;4,5+2i,6];
    ?BCT = ctranspose(B); # conjugate transpose of A
    result:
    1+3i  2+0i  3+7i  
    4+0i  5+2i  6+0i  
    result: 
    1-3i  4+-0i  
    2+-0i  5-2i  
    3-7i  6+-0i  

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [transpose](../en/transpose.md)
