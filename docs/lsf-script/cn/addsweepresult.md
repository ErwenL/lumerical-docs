<!--
Translation from English documentation
Original command: addsweepresult
Translation date: 2026-02-04 22:49:30
-->

# addsweepresult

添加 一个 result 到 一个 sweep/optimization/Monte Carlo item.

**语法** |  **描述**  
---|---  
addsweepresult("name", "result"); |  添加 一个 result 到 一个 sweep/optimization/Monte Carlo item. "name" 是 该 absolute name 的 一个 分析 item. "result" could 为 一个 字符串 (i.e. 创建 一个 result 使用 default 值) 或 一个 结构体 该 could contain results 和 operations. 返回 该 result name.  
  
**示例**

This example shows 如何 到 添加 一个 result 到 一个 existing optimization. This piece 的 脚本 命令 是 taken 从 该 example 文件  sweep_AR_coating_example_script.lsf  在 该 example page [ Optimization scripting commands ](/hc/en-us/articles/360034922973-Optimization-scripting-commands) .
    
    
    # 添加 一个 sweep
    addsweep(0);
    setsweep("sweep", "name", "thickness_sweep_script");
    setsweep("thickness_sweep_script", "类型", "Ranges");
    setsweep("thickness_sweep_script", "数字 的 points", 10); 
    # define 该 参数 thickness
    para = 结构体;
    para.Name = "thickness";
    para.Parameter = "::model::AR 结构::thickness";
    para.Type = "Length";
    para.Start = 0.05e-6;
    para.Stop = 0.15e-6;
    para.Units = "微米";
    # 添加 该 参数 thickness 到 该 sweep
    addsweepparameter("thickness_sweep_script", para);
    # define results
    result_1 = 结构体;
    result_1.Name = "R";
    result_1.Result = "::model::R::T";
    result_2 = 结构体;
    result_2.Name = "T";
    result_2.Result = "::model::T::T";
    # 添加 该 results R & T 到 该 sweep
    addsweepresult("thickness_sweep_script", result_1);
    addsweepresult("thickness_sweep_script", result_2);

**参见**

[ List of commands ](/hc/en-us/articles/360037228834) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034404254-addsphere) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034927973-setsetting), [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult) , [ Sweep scripting commands ](/hc/en-us/articles/360034922893-Sweep-scripting-commands) , [ Optimization scripting commands ](/hc/en-us/articles/360034922973-Optimization-scripting-commands) , [ Monte Carlo scripting commands ](/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
