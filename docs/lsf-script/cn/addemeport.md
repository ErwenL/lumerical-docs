<!--
Translation from English documentation
Original command: addemeport
Translation date: 2026-02-04 22:49:04
-->

# addemeport

添加 一个 [端口](/hc/en-us/articles/360034396374) 到 一个 EME 求解器 region/对象. The EME 求解器 对象 必须 为 设置 as 该 active 求解器 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addemeport; |  添加 一个 端口 到 该 active EME 求解器 region. This 函数 does not 返回 any 数据.  
addemeport(struct_data); |  Adds a port to the active EME solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 端口 到 该 EME 求解器 region. The  setactivesolver  命令 是 first used 到 设置 该 EME 求解器 region as 该 active 求解器.
    
    
    setactivesolver("EME");
    addemeport;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ setactivesolver ](/hc/en-us/articles/360034409014-setactivesolver)
