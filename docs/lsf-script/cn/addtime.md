<!--
Translation from English documentation
Original command: addtime
Translation date: 2026-02-04 22:49:36
-->

# addtime

添加 一个 时间 监视器 到 该 仿真 环境. The 时间 监视器 provides 时间-domain information 用于 field components over 该 course 的 该 仿真

**语法** |  **描述**  
---|---  
addtime; |  添加 一个 时间 监视器 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addtime(struct_data); |  Adds a time monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 point 时间 监视器 到 该 仿真 region 和 设置 its position.
    
    
    addtime;  
    
    设置("name","time_1");  
    设置("监视器 类型",1);  # point  
    设置("x",0);  
    设置("y",0);  
    设置("z",10e-6);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置)
