<!--
Translation from English documentation
Original command: eig
Translation date: 2026-02-03 23:46:10
-->

# eig

查找矩阵的特征值和/或特征向量。矩阵必须是方阵。 

**Syntax** |  **Description**  
---|---  
out = eig(A);  out = eig(A, 1);  |  返回矩阵A的特征值。   
out = eig(A, 2);  |  返回矩阵A的特征向量。   
out = eig(A, 3);  |  返回矩阵A的特征值和特征向量。   
  
 **示例**

一个简单示例，展示特征值计算结果的不同选项。
    
    
    A = [ 1, 2; 2, 4];
    ?eig(A);
    result: 
    0 
    5 
    ?eig(A,1);
    result: 
    0 
    5 
    ?eig(A,2);
    result: 
    -0.894427 -0.447214 
    0.447214 -0.894427 
    ?eig(A,3);
    result(i,j,1):
    0 0 
    0 5 
    result(i,j,2):
    -0.894427 -0.447214 
    0.447214 -0.894427 
     

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [=](./eq.md)
- [==](./equalsequals.md)
- [!=](./notequals.md)
- [<=](./lte.md)
- [>=](./gte.md)
- [<](./lt.md)
- [>](./gt.md)
- [&](./and.md)
- [and](./and.md)
- [|](./or.md)
- [or](./or.md)
- [!](./not.md)
- [~](./not.md)
- [mult](./mult.md)
- [permute](./permute.md)
- [reshape](./reshape.md)
- [inv](./inv.md)
