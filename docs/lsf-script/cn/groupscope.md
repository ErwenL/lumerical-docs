<!--
Translation from English documentation
Original command: groupscope
Translation date: 2026-02-03 10:49:27
-->

# groupscope

更改组范围。添加或修改仿真对象的脚本命令使用 groupscope 属性来确定在对象树中的操作位置。例如，如果要删除特定组内的所有内容，请将 groupscope 设置为该组（即 ::model::my_group）。如果要删除仿真中的所有对象，请将组范围设置为根级别（即 ::model）。

**语法** |  **描述**  
 ---|---  
 ?groupscope;  |  返回当前组范围   
 groupscope("group_name");  |  更改组范围   
 
**示例**

创建一个包含场监视器和折射率监视器的分析组。
    
    
    #创建新的 FDTD 仿真
    newproject;
    addanalysisgroup;
    set("name","Field_Index");
    #更改组范围并向组中添加监视器
    groupscope("Field_Index"); # 等同于 groupscope("::model::Field_Index");
    addpower; set("name","field");
    addindex; set("name","index");
    selectall;
    set("monitor type","3D");
    set("spatial interpolation","nearest mesh cell");
    set("x",0); set("y",0); set("z",0);
    set("x span",1e-6); set("y span",1e-6); set("z span",1e-6);
    # 将组范围更改回模型
    groupscope("::model");
    # 复制该方框
    select("Field_Index");
    copy(2e-6,0,0);

**另请参阅**

[ 操作对象 ](/hc/en-us/articles/360037228834) 、[ delete ](/hc/en-us/articles/360034928573-delete) 、[ selectall ](/hc/en-us/articles/360034408354-selectall) 、[ select ](/hc/en-us/articles/360034928593-select)
