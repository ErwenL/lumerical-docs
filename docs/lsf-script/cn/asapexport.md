<!--
Translation from English documentation
Original command: asapexport
Translation date: 2026-02-04 22:49:36
-->

# asapexport

Exports 该 desired 监视器 到 一个 文件 用于 interfacing 使用 BRO's ASAP. These files have 该 .fld extension. The 监视器 必须 为 一个 频率 power 或 一个 频率 profile 监视器. 

**语法** |  **描述**  
---|---  
asapexport( "monitorname");  |  Export 数据 从 monitorname. By default, 该 first 频率 point 是 exported.  This 函数 does not 返回 any 数据.   
asapexport( "monitorname", f);  |  Exports 该 频率 point specified 通过 该 index f.   
asapexport( "monitorname", f, "文件名");  |  Exports 到 该 specified "文件名" without opening 一个 文件 browser window.   
  
**示例**

Export 数据 从 监视器 transmission 到 一个 .fld 文件 用于 ASAP. The 监视器 had more than one 频率 point, so 该 first point was exported 通过 default. 
    
    
    asapexport("transmission");
    警告: prompt line 1: 在 asapexport: no 频率 point was specified 和 该 d-card has more than one. The first 是 used 通过 default.

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ asapload ](/hc/en-us/articles/360034931973-asapload) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ addimportedsource ](/hc/en-us/articles/360034924433-addimportedsource)
