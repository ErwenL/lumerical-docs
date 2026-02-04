<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adduserprop -->

# adduserprop

**语法** | **描述**
---|---
adduserprop("property name", type, value); | Adds a user property to a selected structure group. The name is set to "property name". The type is an 整数 from 0 to 6. The corresponding 变量 types are 0 - 数字 1 - Text 2 - 长度 3 - Time 4 - 频率 5 - Material 6 - 矩阵 The 值 of the new user property is set to 值.

**示例**

Create a structure group. Add a user property named "radius" and set up the 脚本 in the structure group to add two circles to the group and set their radius to the 值 of the user property "radius". 注意 that the myscript 字符串 uses the escape character \n for new line and \" for double quotes within the 字符串.
    addstructuregroup;
    adduserprop("radius",2,0.5e-6);
    myscript =      "addcircle; \n";
    myscript = myscript + "copy(1e-6); \n";
    myscript = myscript + "selectall; \n";
    myscript = myscript + "set(\"radius\",radius);";
    set("name","dimer");
    set("脚本",myscript); 
An 示例 for analysis group
    addanalysisgroup;
    adduserprop("y span",2,5e-6);
    myscript =" #begin
    y_span = %y span%;
    addpower;
    set('x',0);
    set('y',0);
    set('z',0);
    set('y span',y_span);
    "; #end
    set('setup 脚本',myscript);

Create a structure group. Add a user property named "radius" and set up the 脚本 in the structure group to add two circles to the group and set their radius to the 值 of the user property "radius". 注意 that the myscript 字符串 uses the escape character \n for new line and \" for double quotes within the 字符串.
    addstructuregroup;
    adduserprop("radius",2,0.5e-6);
    myscript =      "addcircle; \n";
    myscript = myscript + "copy(1e-6); \n";
    myscript = myscript + "selectall; \n";
    myscript = myscript + "set(\"radius\",radius);";
    set("name","dimer");
    set("脚本",myscript); 
An 示例 for analysis group
    addanalysisgroup;
    adduserprop("y span",2,5e-6);
    myscript =" #begin
    y_span = %y span%;
    addpower;
    set('x',0);
    set('y',0);
    set('z',0);
    set('y span',y_span);
    "; #end
    set('setup 脚本',myscript);

**另请参阅**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ addstructuregroup ](/hc/en-us/articles/360034924093-addstructuregroup) , [ runsetup ](/hc/en-us/articles/360034928893-runsetup)
