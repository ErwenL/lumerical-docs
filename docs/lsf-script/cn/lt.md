# <（小于）- 脚本运算符

执行逻辑小于比较。忽略 x 和 y 的虚部。

**语法** | **描述**
---|---
out = y < x; | 小于。

**示例**

此示例演示 "<" 运算符的用法。

```
x=[1+3i, 2+5i];
y=[0.5+4i, 3+10i];
?x < y;

     Warning: prompt line 3: in expression A < B, imaginary parts of A and B are ignored
     result:
     0 1
```

**另请参阅**

- [命令列表](./命令列表.md)
- [==](./==.md)
- [!=](./!=.md)
- [<=](./<=.md)
- [>=](./>=.md)
- [almostequal](./almostequal.md)
- [>](./>.md)
- [&](./&.md)
- [and](./and.md)
- [|](./|.md)
- [or](./or.md)
- [!](./!.md)
- [~](./~.md)
