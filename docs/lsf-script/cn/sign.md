<!--
Translator: Claude
Translation Date: 2026-02-03
Status: Completed
-->
# sign

返回数字的符号。

**语法** | **描述**
---|---
out = sign(data); | 如果data为实数：<br>sign = 0（当data=0）<br>sign = 1（当data>0）<br>sign =-1（当data<0）<br>如果data为复数：<br>sign = 0（当data=0+0i）<br>sign = data/abs(data)（当data不为零）

**示例**

sign函数的示例输出。

```
# 实数
数据 = [2; 0; -2];
?sign(数据);
# 复数
数据 = [2+2i; 0+0i; -2+0i];
?sign(数据);
?abs( sign(数据) );
结果：
1 
0 
-1 
结果：
0.707107+0.707107i 
0+0i 
-1+0i 
结果：
1 
0 
1 
```

**另请参阅**

[ 命令列表 ](command-list.html) , [ floor ](floor.html) , [ ceil ](ceil.html)
