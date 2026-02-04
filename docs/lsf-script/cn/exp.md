<!-- Translation completed: 2026-02-04 -->
<!-- Original command: exp -->

# exp

计算自然指数函数。输入可以是复数。

**语法** | **描述**
---|---
out = exp(x); | x的自然指数。

**示例**

要计算e，使用exp(1)：

```lsf
?exp(1);
result: 
2.71828 
```

将1+1i乘以30度：

```lsf
x=1+1i;
?x * exp(1i*pi/6);
result: 
0.366025+1.36603i 
```

**另请参阅**

[命令列表](List_of_commands.md)、[log](log.md)、[^](caret.md)
