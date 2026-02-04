# !

是逻辑 NOT 运算符。如果值为 0，则 NOT 返回 1。对于所有其他值，NOT 返回 0。NOT(A) 等价于 A==0，其中 == 是比较运算符。

**语法** | **描述**
---|---
out = !a; | 对 a 应用逻辑 NOT 运算符
out = ~a; | 对 a 应用逻辑 NOT 运算符

**示例**

此示例展示"!"和"~"运算符的用法。

```powershell
a=1;
?!a; #not 运算符的输出
结果：
0
a=0;
?~a; #not 运算符的输出
结果：
1
a=3;
?~a; #not 运算符的输出
结果：
0
if (!fileexists("filename.fsp")) {
 save("filename.fsp");
}
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[==](./equals.md)、[!=](./exclamationequals.md)、[=](./equals.md)、[&](./ampersand.md)、[and](./and.md)、[|](./pipe.md)、[or](./or.md)、[!](./exclamation.md)、[~](./tilde.md)
