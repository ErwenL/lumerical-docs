<!--
Translation from English documentation
Original command: equalsequals
Translation date: 2026-02-04 01:08:16
-->

# ==

执行逻辑比较。此运算符可用于复数和字符串。 

**Syntax** |  **Description**  
---|---  
out = y == x;  |  如果x和y相等则返回1，否则返回0。   
  
 **示例**

此示例展示"=="运算符的用法。
    
    
    a=1:5;
    b=1:5;
    b(4)=5;
    ?out=a==b;
    result: 
    1 
    1 
    1 
    0 
    1  

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [=](./equals.md)
- [almostequal](./almostequal.md)
- [!=](./notequals.md)
- [<=](./lte.md)
- [>=](./gte.md)
- [<](./lt.md)
- [>](./gt.md)
- [&](./and.md)
- [and](./and.md)
- [|](./or.md)
- [or](./or.md)
- [!](./not.md)
- [~](./not.md)
