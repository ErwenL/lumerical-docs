<!--
Translation Status: Completed
Source: docs/lsf-script/en/round.md
Last Updated: 2026-02-03
-->

# round

将数字四舍五入到最接近的整数。

**语法** |  **说明**  
---|---  
out = round(x);  |  将x四舍五入到最接近的整数。   
  
**示例**

round函数的示例输出。
    
    
    ?x=[1.49,-1.49,1.5,1.55,-1.55];
    ?round(x);
    result: 
    1.49  -1.49  1.5  1.55  -1.55  
    result: 
    1  -1  2  2  -2   

此示例展示如何使用round函数来实现mod函数。
    
    
    mod_dividend= 10;
    mod_divisor = 3;
    mod_temp1=mod_dividend/mod_divisor;
    mod_temp2=round(mod_temp1);
    if (mod_temp1 >= mod_temp2) {
     mod_remainder= round( (mod_temp1 - mod_temp2)*mod_divisor );
    } else {
     mod_remainder= round( (1+mod_temp1 - mod_temp2)*mod_divisor );
    } 
    ?mod_remainder;
    result: 
    1       

**另请参见**

- [floor](./floor.md)
- [ceil](./ceil.md)
- [mod](./mod.md)
