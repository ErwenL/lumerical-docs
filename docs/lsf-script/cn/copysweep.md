<!--
Translation from English documentation
Original command: copysweep
Translation date: 2026-02-04 22:49:48
-->

# copysweep

Copies 一个 sweep/optimization/Monte Carlo 分析 item 到 clipboard.

**语法** |  **描述**  
---|---  
copysweep("name"); |  Copies 一个 sweep/optimization/Monte Carlo 分析 item 到 clipboard. "name" 是 该 absolute name 的 一个 sweep/optimization/Monte Carlo 分析 (eg. ::optimization::sweep1)  
  
**示例**

This example copies 该 sweep "thickness_sweep" 到 该 clipboard 和 pastes it back 到 该 "Optimizations 和 Sweeps" tab again. Please download 该 example 文件 从 该 [ Parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps) page Associate files.
    
    
    copysweep("thickness_sweep");
    pastesweep("");

**参见**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addsweep ](/hc/en-us/articles/360034930413-addsweep) , [ deletesweep ](/hc/en-us/articles/360034930173-deletesweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034404254-addsphere) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034927973-setsetting), [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult)
