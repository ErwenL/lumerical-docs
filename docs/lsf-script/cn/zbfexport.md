<!--
Translation from English documentation
Original command: zbfexport
Translation date: 2026-02-04 22:50:32
-->

# zbfexport

Exports 数据 从 一个 频率 field 或 field 和 power 监视器 到 Zemax *.zbf 文件. This 命令 可以 为 also used 到 export 数据 从 一个 d-card 到 Zemax 文件. The 返回 值 的 此 命令 是 该 origin (x, y 和 z coordinates) 的 该 监视器 exported 到 该 *.zbf 文件.

**语法** |  **描述**  
---|---  
output = zbfexport("monitorname"); |  Export 数据 从 monitorname. By default, 该 first 频率 point 是 exported. This 函数 返回 该 origin 的 该 监视器 exported 到 该 *.zbf 文件, 在 该 format 的 一个 数组 使用 该 x, y 和 z coordinates 的 该 监视器 origin.  
zbfexport("monitorname",f); |  Exports 该 频率 point specified 通过 该 index f.  
zbfexport("monitorname",f,"文件名"); |  Exports 到 该 specified "文件名" without opening 该 文件 browser window.  
[[注意:]] The Zemax zbf 文件 需要 该 数据 到 为 saved 在 一个 uniform grid 的 dimensions 使用 一个 power 的 2 (使用 \\(2^n \times 2^m\\) points). The dataset 将 为 interpolated 在 一个 grid 使用 \\(n\\) 和 \\(m\\) defined so 该 mesh step 是 equal 到 或 less than 该 smallest mesh step 在 该 original 数据.  
---  
  
### 示例 #1

Export 数据 从 监视器 "beam_profile" 到 一个 .zbf 文件 用于 Zemax. The 监视器 had more than one 频率 point, so we elected 到 export 该 third 频率 point.
    
    
    ?zbfexport("beam_profile",3,"test_export.zbf");
    result:
    1e-07
    3e-07
    0

### 示例 #2

Export 数据 从 dcard named "global_mode1" 到 一个 .zbf 文件 用于 Zemax. The d-card has one 频率 point, so we use f index =1.
    
    
    zbfexport("global_mode1",1,"testfileDcard.zbf");

**参见**

[ zbfload ](/hc/en-us/articles/360034928273-zbfload) , [ zbfread ](/hc/en-us/articles/360034408154-zbfread) , [ zbfwrite ](/hc/en-us/articles/360034928293-zbfwrite) , [ List 的 commands ](/hc/en-us/articles/360037228834)
