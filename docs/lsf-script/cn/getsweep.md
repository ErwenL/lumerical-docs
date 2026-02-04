<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getsweep -->

# getsweep

**语法** | **描述**
---|---
getsweep("name", "property_name"); | Gets a property from a 参数 sweep/optimization/Monte Carlo/S-参数 sweep item. "name" is the absolute name of an analysis item. "property_name" is the property showed in the edit window. 返回 the 值 of the property.
?getsweep("name"); | Lists the properties that are available from the analysis item.

**示例**

This 示例 shows how to get a property from a 参数 sweep. Please download the 示例 文件 from the [ 参数 sweeps ](/hc/en-us/articles/360034922873-参数-sweeps) page Associate files.
    ?getsweep("thickness_sweep", "thickness");
    > Struct with fields:
    > name
    > 参数
    > start
    > stop
    > type

This 示例 shows how to get a property from a 参数 sweep. Please download the 示例 文件 from the [ 参数 sweeps ](/hc/en-us/articles/360034922873-参数-sweeps) page Associate files.
    ?getsweep("thickness_sweep", "thickness");
    > Struct with fields:
    > name
    > 参数
    > start
    > stop
    > type

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ deletesweep ](/hc/en-us/articles/360034930173-deletesweep) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034930413-addsweep) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034927973-setsetting), [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult)
