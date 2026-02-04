<!--
Translation from English documentation
Original command: addanalysisgroup
Translation date: 2026-02-04 22:46:12
-->

# addanalysisgroup

添加 an [analysis group](/hc/en-us/articles/360034382454) to the 仿真 environment. Analysis groups are container 对象 that can contain any 仿真 对象 and associated 脚本 functions which can be used to 创建 customize 数据 analysis.

**语法** |  **描述**  
---|---  
addanalysisgroup; |  添加 an analysis group to the 仿真 environment. This 函数 does not 返回 any 数据.  
addanalysisgroup(struct_data); |  Adds an analysis group and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

添加 an analysis group and put a time 监视器 in it.
    
    
    addanalysisgroup;
    设置("name","group");
    addtime;
    addtogroup("group");

To learn more about how to use analysis groups go to this page: [ Using Analysis Groups ](/hc/en-us/articles/360034382454-Analysis-Groups) .

注意: To 添加 a pre-defined analysis group from the 对象 library, use the [ addobject ](/hc/en-us/articles/360034404094-addobject) 命令.  
---  
  
**参见**

- [List of commands](../lsf-脚本-commands-alphabetical.md)
- [addtogroup](./addtogroup.md)
- [adduserprop](./adduserprop.md)
- [runanalysis](./runanalysis.md)
- [getresult](./getresult.md)
- [addobject](./addobject.md)
