# exist

根据命令中使用的字符串类型返回一个数字。

**语法** | **描述**
---|---
exist("x") | 返回<br>0 如果在当前脚本路径中没有变量、运算符、内置函数或脚本文件 (x.lsf)<br>1 如果 x 是一个变量，例如：x=5; ?exist("x");<br>2 如果 x 是一个运算符或内置关键字，例如：?exist("*") 或 ?exist("for");<br>3 如果 x 是当前脚本路径中名为"x.lsf"的脚本文件。

**示例**

以下简单示例展示 exist 命令的用法。

```powershell
a = 1:10;
?exist("a");
结果：
1
?exist("farfield3d");
结果：
2
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[newproject](./newproject.md)、[fileexists](./fileexists.md)
