<!--
Translation from English documentation
Original command: addstructuregroup
Translation date: 2026-02-04 22:49:30
-->

# addstructuregroup

添加 一个 结构 group 到 该 仿真 环境. Structure groups 是 very convenient 当 you want 到 parametrize your design. You 可以 define different 参数 用于 该 结构 group 和 use 该 "setup" 脚本 到 创建 your geometry (along 使用 monitors 和/或 sources) according 到 那些 参数 值.

**语法** |  **描述**  
---|---  
addstructuregroup; |  添加 一个 结构 group 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addstructuregroup(struct_data); |  Adds a structure group and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

添加 一个 结构 group 和 put 一个 rectangle 在 it.
    
    
    addstructuregroup;
    设置("name","group");
    addrect;
    addtogroup("group");

创建 一个 结构 group. 添加 一个 用户 属性 named "radius" 和 设置 up 该 脚本 在 该 结构 group 到 添加 two circles 到 该 group 和 设置 their radius 到 该 值 的 该 用户 属性 "radius".
    
    
    addstructuregroup;
    adduserprop("radius",2,0.5e-6);
    myscript =      "addcircle; \n";
    myscript = myscript + "copy(1e-6); \n";
    myscript = myscript + "selectall; \n";
    myscript = myscript + "设置(\"radius\",radius);";
    设置("name","dimer");
    设置("脚本",myscript); 

NOTE: The "myscript" 字符串 在 该 脚本 above uses 该 escape character \n 用于 新的 line 和 \" 用于 double quotes within 该 字符串. 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ addtogroup ](/hc/en-us/articles/360034408454-addtogroup) , [ adduserprop ](/hc/en-us/articles/360034928733-adduserprop) , [ addgroup ](/hc/en-us/articles/360034924073-addgroup) , [ addanalysisgroup ](/hc/en-us/articles/360034404074-addanalysisgroup) , [ 设置 ](/hc/en-us/articles/360034928773-设置)
