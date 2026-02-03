<!--
Translation from English documentation
Original command: addanalysisgroup
Translation date: 2026-02-03
-->

# addanalysisgroup

向仿真环境添加一个[分析组](/hc/en-us/articles/360034382454)。分析组是容器对象，可以包含任何仿真对象和相关的脚本函数，用于创建自定义数据分析。

**Syntax** | **Description**
---|---
addanalysisgroup; | 向仿真环境添加一个分析组。此函数不返回任何数据。
addanalysisgroup(struct_data); | 添加一个分析组，并使用包含"property"和值对的结构体设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。

**Example**

添加一个分析组，并将时间监视器放入其中。

    addanalysisgroup;
    set("name","group");
    addtime;
    addtogroup("group");

要了解更多关于如何使用分析组的信息，请访问此页面：[使用分析组](/hc/en-us/articles/360034382454-Analysis-Groups)。

注意：要从对象库添加预定义的分析组，请使用[addobject](/hc/en-us/articles/360034404094-addobject)命令。

---

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [addtogroup](./addtogroup.md)
- [adduserprop](./adduserprop.md)
- [runanalysis](./runanalysis.md)
- [getresult](./getresult.md)
- [addobject](./addobject.md)