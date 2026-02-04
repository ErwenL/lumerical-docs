<!--
Translation from English documentation
Original command: addemeindex
Translation date: 2026-02-04 22:49:04
-->

# addemeindex

添加 一个 [index 监视器](/hc/en-us/articles/360034396434) 该 可以 为 used 到 返回 该 spatial refractive index 当 使用 一个 EME 求解器 region. The EME 求解器 对象 必须 为 设置 as 该 active 求解器 用于 此 命令 到 work.

**语法** |  **描述**  
---|---  
addemeindex; |  添加 一个 index 监视器 当 使用 一个 EME 求解器 region. This 函数 does not 返回 any 数据.  
addemeindex(struct_data); |  Adds an EME index monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 index 监视器 到 该 EME 求解器 region. The  setactivesolver  命令 是 first used 到 设置 该 EME 求解器 region as 该 active 求解器.
    
    
    setactivesolver("EME");
    addemeindex;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ setactivesolver ](/hc/en-us/articles/360034409014-setactivesolver)
