<!--
Translation from English documentation
Original command: cwnorm
Translation date: 2026-02-04 22:49:48
-->

# cwnorm

Uses CW normalization. All 仿真 数据 将 为 normalized 到 该 injected 源 power. Most users prefer 到 do their 分析 在 该 CW normalization state, since it removes any effect caused 通过 该 finite pulse 长度 的 该 源. It also 转换 该 units 的 all electromagnetic fields 到 为 该 same as 在 该 时间 domain. 注意, 此 命令 works 在 both 该 Layout 和 Analysis mode.

This 函数 controls 该 checkbox located 在 Settings - Normalization state.

**语法** |  **描述**  
---|---  
cwnorm; |  Use CW normalization. Uses 该 first active 源 在 该 Object tree; This 函数 does not 返回 any 数据.  
cwnorm(norm_option) |  norm_option: 1 (first 源), 2 (average 的 all sources)  
  
**示例**

This example shows 如何 到 switch 到 该 cwnorm state.
    
    
    cwnorm; # normalized 到 该 first active 源  
      
    cwnorm(1); # normalized 到 该 first active 源  
    cwnorm(2); # normalized 到 该 average 的 all 该 sources

**参见**

[nonorm](/hc/en-us/articles/360034405434-nonorm), [Units 和 normalization](/hc/en-us/articles/360034397034), [Frequency Domain Normalization](/hc/en-us/articles/360034394234-Frequency-domain-normalization)
