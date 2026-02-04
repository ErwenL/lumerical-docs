<!--
Translation from English documentation
Original command: getsweep
Translation date: 2026-02-04 22:50:00
-->

# getsweep

获取 一个 属性 从 一个 参数 sweep/optimization/Monte Carlo/S-参数 sweep item.

**语法** |  **描述**  
---|---  
getsweep("name", "property_name"); |  获取 一个 属性 从 一个 参数 sweep/optimization/Monte Carlo/S-参数 sweep item. "name" 是 该 absolute name 的 一个 分析 item. "property_name" 是 该 属性 showed 在 该 edit window. 返回 该 值 的 该 属性.  
?getsweep("name"); |  Lists 该 属性 该 是 available 从 该 分析 item.  
  
**示例**

This example shows 如何 到 获取 一个 属性 从 一个 参数 sweep. Please download 该 example 文件 从 该 [ Parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps) page Associate files.
    
    
    ?getsweep("thickness_sweep", "thickness");
    > Struct 使用 fields:
    > name
    > 参数
    > start
    > stop
    > 类型

**参见**

[ List of commands ](/hc/en-us/articles/360037228834) , [ deletesweep ](/hc/en-us/articles/360034930173-deletesweep) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034930413-addsweep) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034927973-setsetting), [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult)
