<!-- Translation completed: 2026-02-04 -->
<!-- Original command: asapexport -->

# asapexport

**语法** | **描述**
---|---
asapexport( "monitorname"); | 导出 data from monitorname. By default, the first 频率 point is exported.  This 函数 does not 返回 any data.
asapexport( "monitorname", f); | Exports the 频率 point specified by the index f.
asapexport( "monitorname", f, "filename"); | Exports to the specified "文件名" without opening a 文件 browser window.

**示例**

导出 data from 监视器 透射 to a .fld 文件 for ASAP. The 监视器 had more than one 频率 point, so the first point was exported by default. 
    asapexport("透射");
    警告: prompt line 1: in asapexport: no 频率 point was specified and the d-card has more than one. The first is used by default.

导出 data from 监视器 透射 to a .fld 文件 for ASAP. The 监视器 had more than one 频率 point, so the first point was exported by default. 
    asapexport("透射");
    警告: prompt line 1: in asapexport: no 频率 point was specified and the d-card has more than one. The first is used by default.

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ asapload ](/hc/en-us/articles/360034931973-asapload) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ addimportedsource ](/hc/en-us/articles/360034924433-addimportedsource)
