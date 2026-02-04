# !=

执行逻辑"不等于"比较。如果值不相等，则返回 1。如果值相等，则返回 0。此运算符可用于矩阵操作。此运算符可与复数一起使用。

**语法** | **描述**
---|---
out = a!=b; | 如果 a 不等于 b，则 out 等于 1。否则 out 等于 0。

**示例**

此示例展示"!="比较的用法。

```powershell
a=1:5;
b=1:5;
b(4)=5;
?out = a!=b;
结果：
0
0
0
1
0
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[==](./equals.md)、[almostequal](./almostequal.md)、[=](./equals.md)、[&](./ampersand.md)、[and](./and.md)、[|](./pipe.md)、[or](./or.md)、[!](./exclamation.md)、[~](./tilde.md)
