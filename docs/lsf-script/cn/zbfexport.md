<!-- Translation completed: 2026-02-04 -->
<!-- Original command: zbfexport -->

# zbfexport

**语法** | **描述**
---|---
output = zbfexport("monitorname"); | 导出 data from monitorname. By default, the first 频率 point is exported. This 函数 返回 the origin of the 监视器 exported to the *.zbf 文件, in the 格式 of an 数组 with the x, y and z coordinates of the 监视器 origin.
zbfexport("monitorname",f); | Exports the 频率 point specified by the index f.
zbfexport("monitorname",f,"filename"); | Exports to the specified "文件名" without opening the 文件 browser window.

**示例**

导出 data from 监视器 "beam_profile" to a .zbf 文件 for Zemax. The 监视器 had more than one 频率 point, so we elected to 导出 the third 频率 point.
    ?zbfexport("beam_profile",3,"test_export.zbf");
    result:
    1e-07
    3e-07
    0

导出 data from dcard named "global_mode1" to a .zbf 文件 for Zemax. The d-card has one 频率 point, so we use f index =1.
    zbfexport("global_mode1",1,"testfileDcard.zbf");

导出 data from dcard named "global_mode1" to a .zbf 文件 for Zemax. The d-card has one 频率 point, so we use f index =1.
    zbfexport("global_mode1",1,"testfileDcard.zbf");

**另请参阅**

[ zbfload ](/hc/en-us/articles/360034928273-zbfload) , [ zbfread ](/hc/en-us/articles/360034408154-zbfread) , [ zbfwrite ](/hc/en-us/articles/360034928293-zbfwrite) , [ List of commands ](/hc/en-us/articles/360037228834)
