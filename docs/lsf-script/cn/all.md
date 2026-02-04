<!-- Translation completed: 2026-02-04 -->
<!-- Original command: all -->

# all

如果指定矩阵的所有元素均为非零值，则返回1，否则返回0。

**语法** | **描述**
---|---
out = all(A); | 如果矩阵A的所有元素均为非零值，则返回1，否则返回0。
out = all(A,n); | n是一个可选参数，用于分析特定维度中的元素

**示例**

以下是一个简单的示例，展示如何使用此命令。

```lsf
a = [1,4,3,0.5];
b = [1,3;6,0];
?all(a);
?all(b);
result:
1
result: 
0  
?all(b,2);
result: 
1  
0   
```

**另请参阅**

[命令列表](List_of_commands.md)、[any](any.md)、[almostequal](almostequal.md)
