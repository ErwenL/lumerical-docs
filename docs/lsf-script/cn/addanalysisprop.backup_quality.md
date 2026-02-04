<!--
Translation from English documentation
Original command: addanalysisprop
Translation date: 2026-02-04 22:46:39
-->

# addanalysisprop

添加 a user defined custom analysis 属性 to the setup user defined in 结构 and analysis groups.

**语法** |  **描述**  
---|---  
addanalysisprop("属性 name", type, 值); |  添加 an analysis 属性 to a selected 对象 group. The name is 设置 to "属性 name". The type is an integer from 0 to 8. The corresponding variable types are: 0 - Number 1 - String 2 - Length 3 - Time 4 - Frequency 5 - Material 6 - Matrix 7 - Cell 8 - Struct The 值 of the new user 属性 is 设置 to 值.  
  
**示例**

添加 a length variable called "Pname" as an analysis 属性 for the analysis group
    
    
    addanalysisgroup;
    设置("name","group");
    addanalysisprop("Pname", 2, 1e-6); # 2 represents Length

**参见**

- [Manipulating 对象](../lsf-脚本-commands-alphabetical.md)
- [addstructuregroup](./addstructuregroup.md)
- [runsetup](./runsetup.md)
- [addanalysisgroup](./addanalysisgroup.md)
- [addanalysisresult](./addanalysisresult.md)
