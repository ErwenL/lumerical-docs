<!-- Translated: 2026-02-03 -->
<!-- Original: tilde -->

# ~

逻辑非运算符。如果值为 0，则 NOT 返回 1。对于所有其他值，NOT 返回 0。NOT(A) 等价于 A==0，其中 == 是比较运算符。

**语法** | **描述**
---| ---
out = !a; | 对 a 应用逻辑非运算符
out = ~a; | 对 a 应用逻辑非运算符

**示例**

此示例展示了 "!" 和 "~" 运算符的用法。

```lsf
a=1;
?!a; #output of not operator
result:
0
a=0;
?~a; #output of not operator
result:
1
a=3;
?~a; #output of not operator
result:
0
if (!fileexists("filename.fsp")) {
 save("filename.fsp");
}
```

**另见**

[命令列表](./list-of-commands.md)、[==](./eq.md)、[!=](./neq.md)、[=](./assign.md)、[&](./and.md)、[and](./and.md)、[|](./or.md)、[or](./or.md)、[!](./not.md)、[~](./tilde.md)
