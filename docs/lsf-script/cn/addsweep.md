<!--
Translation from English documentation
Original command: addsweep
Translation date: 2026-02-04 22:49:30
-->

# addsweep

添加 一个 参数 sweep/optimization/Monte Carlo/S-参数 sweep item as 该 top-most 分析 item.

**语法** |  **描述**  
---|---  
addsweep(类型); |  添加 一个 参数 sweep/optimization/Monte Carlo/S-参数 sweep item as 该 top-most 分析 item. '类型' = 0 用于 参数 sweep '类型' = 1 用于 optimization '类型' = 2 用于 Monte Carlo 分析 '类型' = 3 用于 S-参数 矩阵 sweep 在 FDTD 和 MODE 求解器 '类型' = 4 用于 Corner sweep 分析 在 INTERCONNECT If 类型 是 not provided, 通过 default 类型 0 将 为 applied 到 添加 一个 sweep.  
  
**示例**

Type = 0, 用于 adding 一个 **参数 sweep** 分析:
    
    
    addsweep(0);
    ?setsweep("sweep");
    > Result:
    name
    类型  
    求解器
    数字 的 points
    resave files after 分析

Type = 1, 用于 adding 一个 **optimization** 分析:
    
    
    addsweep(1);
    ?setsweep("optimization");
    > Result:
    name  
    algorithm  
    maximum generations  
    reset random generator  
    类型  
    generation size  
    tolerance  
    first generation 脚本  
    next generation 脚本  
    use figure 的 merit 脚本  
    figure 的 merit 脚本

Type = 2, 用于 adding 一个 **Monte Carlo** 分析:
    
    
    addsweep(2);  
    ?setsweep("Monte Carlo 分析");
    > Result:
    name  
    数字 的 trials  
    variation  
    seed  
    启用 seed  
    individual trial  
    启用 individual trial  
    启用 spatial correlations

Type = 3, 用于 adding 一个 **S-参数 sweep** 分析 在 FDTD:
    
    
    addsweep(3);  
    ?setsweep("s-参数 sweep");
    > Result:
    name  
    excite all ports  
    计算 group delay  
    invert sign  
    map 从  
    active  
    端口  
    mode  
    map 向量  
    auto symmetry  
    export setup

Type = 3, 用于 adding 一个 **S-参数 sweep** 分析 在 MODE:
    
    
    addsweep(3);  
    ?setsweep("s-参数 sweep");
    > Result:
    name  
    数字 的 points  
    计算 group delay  
    group delay 波长  
    参数 label  
    start 波长  
    stop 波长  
    include group delay

Type = 4, 用于 adding 一个 **Corner sweep** 分析 在 INTERCONNECT:
    
    
    addsweep(4);  
    ?getsweep("Corner sweep");  
    > Result:  
    name  
    resave files after 分析

**参见**

[ List of commands ](/hc/en-us/articles/360037228834) , [ deletesweep ](/hc/en-us/articles/360034930173-deletesweep) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034930473-setsweep), [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult)
