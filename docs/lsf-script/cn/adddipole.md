<!--
Translation from English documentation
Original command: adddipole
Translation date: 2026-02-04 22:49:04
-->

# adddipole

添加 一个 [dipole 源](/hc/en-us/articles/360034382794) 到 该 仿真 环境. In MODE 该 命令 需要 一个 active varFDTD 求解器 region 在 该 对象 tree.

**语法** |  **描述**  
---|---  
adddipole; |  添加 一个 dipole 源 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
adddipole(struct_data); |  Adds a dipole source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands 将 添加 一个 dipole 源 到 该 FDTD 仿真 环境 和 设置 its position.
    
    
    adddipole;
    设置("x",0);
    设置("y",-1e-6);
    设置("z",5e-6);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ addplane ](/hc/en-us/articles/360034924413-addplane) , [ addgaussian ](/hc/en-us/articles/360034404434-addgaussian) , [ addtfsf ](/hc/en-us/articles/360034404454-addtfsf)
