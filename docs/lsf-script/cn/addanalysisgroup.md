<!--
Translation 从 English documentation
Original 命令: addanalysisgroup
Translation date: 2026-02-04 23:10:58
-->

# addanalysisgroup

添加 一个 [分析 group](/hc/en-us/articles/360034382454) 到 该 仿真 环境。 Analysis groups 是 容器 对象 该 可以 contain any 仿真 对象 和 associated 脚本 functions 该 可以 为 used 到 创建customize 数据 分析。

**语法** | **描述**
---|---
addanalysisgroup; | 添加 一个 分析 group 到 该 仿真 环境。 This 函数 does not 返回any 数据。
addanalysisgroup(struct_data); |  Adds an analysis group and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  

**示例**

添加 一个 分析 group 和 put 一个 时间 监视器 在 it。


    addanalysisgroup;
    设置("name","group");
    addtime;
    addtogroup("group");

To learn more about 如何 到 use 分析 groups go 到 此 page: [ Using Analysis Groups ](/hc/en-us/articles/360034382454-Analysis-Groups) 。

注意: To 添加 一个 pre-defined 分析 group 从 该 对象 library， use 该 [ addobject ](/hc/en-us/articles/360034404094-addobject) 命令。
---

**参见**

- [List 的 commands](。。/lsf-脚本-commands-alphabetical。md)
- [addtogroup](。/addtogroup。md)
- [adduserprop](。/adduserprop。md)
- [runanalysis](。/runanalysis。md)
- [getresult](。/getresult。md)
- [addobject](。/addobject。md)
