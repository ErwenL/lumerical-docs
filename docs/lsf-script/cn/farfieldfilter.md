<!--
Translation from English documentation
Original command: farfieldfilter
Translation date: 2026-02-04 22:49:48
-->

# farfieldfilter

设置 或 获取 该 filter width 用于 far field filter 该 是 used 到 remove ripples 在 该 far field projection due 到 clipping 的 该 near fields. It 应该 为 used 当 该 near fields at 该 edge 的 该 监视器 是 small but not precisely zero. 

The bumpy blue line 的 该 figure shows 该 near field electric field 该 将 为 used 用于 一个 far field projection. In 此 case, 该 field does not go 到 zero at 该 edge 的 该 监视器, 该 将 lead 到 ripples 在 该 far field projection. The green line shows 该 spatial filter 该 将 为 applied 到 该 fields, ensuring they go 到 zero. The filter 参数 defines 该 width 的 该 filter 通过 该 following formula: α=(一个)/(一个+b). 

**语法** |  **描述**  
---|---  
out = farfieldfilter;  |  获取 该 current far field filter setting.   
farfieldfilter(α);  |  设置 该 current far field filter setting. α=(一个)/(一个+b). The far field filter has 一个 single input 参数, 该 是 一个 数字 between 0 和 1. By default, it 是 0, 该 turns 该 filter off. This filter 是 applied 到 all far field projections.   
  
注意: Periodic structures  The far field filter option 应该 not 为 used 用于 periodic structures. 设置 it 到 zero 当 使用 该 'assume periodic' option.   
---  
  
**示例**

[ Far field projection - spatial filtering ](/hc/en-us/articles/360034394314-FFP-Spatial-filtering)

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d)
