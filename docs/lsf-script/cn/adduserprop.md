<!--
Translation from English documentation
Original command: adduserprop
Translation date: 2026-02-04 22:49:36
-->

# adduserprop

添加 一个 自定义 用户 属性 到 一个 结构 或 分析 group.

**语法** |  **描述**  
---|---  
adduserprop("属性 name", 类型, 值); |  添加 一个 用户 属性 到 一个 选中的 结构 group. The name 是 设置 到 "属性 name". The 类型 是 一个 integer 从 0 到 6. The 对应的 变量 types 是 0 - 数字 1 - Text 2 - Length 3 - Time 4 - Frequency 5 - Material 6 - Matrix The 值 的 该 新的 用户 属性 是 设置 到 值.  
  
**示例**

创建 一个 结构 group. 添加 一个 用户 属性 named "radius" 和 设置 up 该 脚本 在 该 结构 group 到 添加 two circles 到 该 group 和 设置 their radius 到 该 值 的 该 用户 属性 "radius". 注意 该 该 myscript 字符串 uses 该 escape character \n 用于 新的 line 和 \" 用于 double quotes within 该 字符串.
    
    
    addstructuregroup;
    adduserprop("radius",2,0.5e-6);
    myscript =      "addcircle; \n";
    myscript = myscript + "copy(1e-6); \n";
    myscript = myscript + "selectall; \n";
    myscript = myscript + "设置(\"radius\",radius);";
    设置("name","dimer");
    设置("脚本",myscript); 

An example 用于 分析 group
    
    
    addanalysisgroup;
    adduserprop("y跨度",2,5e-6);
    myscript =" #begin
    y_span = %y跨度%;
    addpower;
    设置('x',0);
    设置('y',0);
    设置('z',0);
    设置('y跨度',y_span);
    "; #end
    设置('setup 脚本',myscript);

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ addstructuregroup ](/hc/en-us/articles/360034924093-addstructuregroup) , [ runsetup ](/hc/en-us/articles/360034928893-runsetup)
