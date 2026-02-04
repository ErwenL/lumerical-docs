<!--
Translation from English documentation
Original command: select
Translation date: 2026-02-04 22:50:14
-->

# select

Selects 对象 使用 一个 given name 在 该 current group scope. A failed select 命令 将 have 该 same result as 该 unselectall 命令. 

**语法** |  **描述**  
---|---  
select("name");  |  Selects 对象 使用 该 name "name" 在 该 current group scope.  This 函数 does not 返回 any 数据.   
select("group name::name");  |  Selects all 对象 使用 该 name "name" located 在 该 group named "group name". The group named "group name" 必须 为 在 该 current group scope.   
  
**示例**

添加 two 对象 和 select 该 first 对象 用于 other settings. 
    
    
    addrect;
    设置("name","substrate");
    addring;
    select("substrate");

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ groupscope ](/hc/en-us/articles/360034928553-groupscope) , [ unselectall ](/hc/en-us/articles/360034408374-unselectall)
