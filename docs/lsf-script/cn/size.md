<!--
Translator: Claude
Translation Date: 2026-02-03
Status: Completed
-->
# size

返回矩阵的大小。

**语法** | **描述**
---|---
y = size(x); | y是一个显示x维度的矩阵。
y = size(x,n); | n是一个可选参数，用于获取矩阵在特定维度的大小

**示例**

检查矩阵的维度。

```
x=matrix(2,3,3);
?y=size(x);
结果：
2 3 3 
?size(x,2);
结果：
3 
```

**另请参阅**

[ 命令列表 ](command-list.html) , [ length ](length.html) , [ flip ](flip.html) , [ transpose ](transpose.html)
