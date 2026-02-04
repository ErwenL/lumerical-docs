<!--
Translation Status: Completed
Source: docs/lsf-script/en/reshape.md
Last Updated: 2026-02-03
-->

# reshape

将矩阵A重塑为给定的大小i,j,k。指定维度的乘积i*j*k*...必须与原始矩阵A的乘积相同。

**语法** |  **说明**  
---|---  
out = reshape(A, [i,j,k, ...])  |  返回一个与A具有相同元素但重塑为大小i乘以j乘以k乘以...的数组   
  
**示例**

展示如何重塑2D矩阵的简单示例。
    
    
    ?A=[1,2,3;4,5,6];
    ?B=reshape(A,[2,3]); # 保持不变
    ?B=reshape(A,[3,2]); # 重塑为3行2列
    ?B=reshape(A,[1,6]); # 创建单行向量
    ?B=transpose(A);    # transpose函数，用于比较
    result: 
    1 2 3 
    4 5 6 
    result: 
    1 2 3 
    4 5 6 
    result: 
    1 5 
    4 3 
    2 6 
    result: 
    1 4 2 5 3 6 
    result: 
    1 4 
    2 5 
    3 6 

更高维度的矩阵也可以被重塑。
    
    
    A=matrix(2,3,4);
    A(1:2,1:3,1) = [1, 2, 3; 4, 5, 6];
    A(1:2,1:3,2) = [7, 8, 9; 10,11,12];
    A(1:2,1:3,3) = [13,14,15;16,17,18];
    A(1:2,1:3,4) = [19,20,21;22,23,24];
    ?A;
    ?B=reshape(A,[6,4]);    # 重塑为2D矩阵
    ?B=reshape(A,[1,2*3*4]); # 将所有数据重塑为单行向量
    B=permute(A,[2,1,3]);    # 转置第1和第2维度
    ?C=reshape(B,[1,2*3*4]); # 然后重塑为单行向量
    result(i,j,1):
    1 2 3 
    4 5 6 
    result(i,j,2):
    7 8 9 
    10 11 12 
    result(i,j,3):
    13 14 15 
    16 17 18 
    result(i,j,4):
    19 20 21 
    22 23 24 
    result: 
    1 7 13 19 
    4 10 16 22 
    2 8 14 20 
    5 11 17 23 
    3 9 15 21 
    6 12 18 24 
    result: 
    1 4 2 5 3 6 7 10 8 11 9 12 13 16 14 17 15 18 19 22 20 23 21 24 
    result: 
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 

**另请参见**

- [eig](./eig.md)
- [permute](./permute.md)
- [mult](./mult.md)
- [inv](./inv.md)
- [flip](./flip.md)
- [transpose](./transpose.md)
- [size](./size.md)
