<!--
Translation from English documentation
Original command: getfield
Translation date: 2026-02-04 22:50:00
-->

# getfield

The 脚本 命令 返回 该 值 的 一个 field 从 结构 input. 

**语法** |  **描述**  
---|---  
值= getfield(input, field);  |  返回 该 值 的 一个 ‘field’ 从 结构 ‘input’.   
  
###  示例 
    
    
    >x=结构体;
    >x.t=10;
    >?getfield(x,'t');
    result: 
    10 

###  参见 

[ isfield ](/hc/en-us/articles/360034932293-isfield) , [ setfield ](/hc/en-us/articles/360034932313-setfield)
