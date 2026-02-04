# precision

将数字截断到用户指定的精度。精度由舍入时使用的有效数字位数指定。

**语法** | **描述**
---|---
out = precision (y,p); | 将 y 截断到用户定义的精度 p。其中 p 是有效数字的位数。

### 示例

根据用户定义的精度显示不同的"π"值。

```powershell
?pi;
结果：
3.14159
?precision(pi,2);
结果：
3.1
?precision(pi,3);
结果：
3.14
?precision(pi,4);
结果：
3.142
?precision(pi/100,4);
结果：
0.03142
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[round](./round.md)
