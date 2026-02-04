<!--
Translation from English documentation
Original command: real
Translation date: 2026-02-03
-->

# real

返回数字或矩阵的实部。

**语法** | **描述**
---|---
out = real(x); | 返回 x 的实部。

**示例**

计算数组中数字的实部。

```lsf
?x=linspace(0, 2+1i,2);
```
结果：
```
0+0i
2+1i
```

```lsf
?real(x);
```
结果：
```
0
2
```

**另请参见**

- [命令列表](./command_list.md)
- [imag](./imag.md)
