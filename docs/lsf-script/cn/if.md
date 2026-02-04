<!--
Translation from English documentation
Original command: if
Translation date: 2026-02-03
-->

# if

开始 if 语句。脚本语言支持以下形式的 if 语句：

**语法** |  **描述**
---|---
if(x < 5) { y = x^2; }  |  单行简单 if 语句。
if(x < 5) {  y = x^2;  }  |  多行 if 语句。
if(x < 5) {  y = x^2;  } else {  y = x^3;  }  |  if else 语句。
if(x < 5) {  if(x > 0) {y = x^2;}  } else {  y = x^3;  }  |  带 else 的嵌套 if 语句。
if(x < 5) {  y = x^2;  } else if ( x > 10 ) {  y = 2*x;  }  |  链式 if else if 语句。

**示例**

此示例展示简单的 if、OR、AND 逻辑语句

    clear;
    a=1;
    b=2;
    d=3;
    if((a==1)|(b==2)&(d==3)){
    ?"correct";}
    else{
    ?"not correct";}

**相关命令**

- [List of commands](./List-of-commands.md)
- [for](./for.md)
- [==](./Equal.md)
- [almostequal](./almostequal.md)
- [?](./Question.md)
