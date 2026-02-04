<!--
Translation from English documentation
Original command: addsweepparameter
Translation date: 2026-02-04 22:49:30
-->

# addsweepparameter

添加 一个 参数 到 一个 参数 sweep/optimization/Monte Carlo/S-参数 sweep item.

**语法** |  **描述**  
---|---  
addsweepparameter("name", "参数"); |  添加 一个 参数 到 一个 参数 sweep/optimization/Monte Carlo/S-参数 sweep item. "name" 是 该 absolute name 的 一个 分析 item. "参数" could 为 一个 字符串 (i.e. 创建 一个 参数 使用 default 值. eg. ::model::rectangle::index) 或 一个 结构体 该 counld contain 参数, 类型, start, stop, unit, etc. 返回 该 参数 name.  
  
**示例**

This example shows 如何 到 添加 一个 参数 到 一个 existing optimization. This piece 的 脚本 命令 是 taken 从 该 example 文件  sweep_AR_coating_example_script.lsf  在 该 example page [ Optimization scripting commands ](/hc/en-us/articles/360034922973-Optimization-scripting-commands) .
    
    
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

This example shows 如何 到 添加 一个 参数 sweep 该 sweeps 5 值 的 一个 thickness 参数.
    
    
    addsweep(0);setsweep("sweep","name","thickness_sweep");
    setsweep("thickness_sweep","类型","Values");
    setsweep("thickness_sweep","数字 的 points",5);
    # define 该 参数 thickness
    para = 结构体;
    para.Parameter = "::model::AR 结构::thickness";
    para.Type = "Length";
    para.Value_1 = 0.05e-6;
    para.Value_2 = 0.07e-6;
    para.Value_3 = 0.09e-6;
    para.Value_4 = 0.11e-6;
    para.Value_5 = 0.15e-6;
    # 添加 该 参数 thickness 到 该 sweep
    addsweepparameter("thickness_sweep", para);

This example shows 如何 到 添加 一个 S-参数 sweep 和 设置 up 该 rows 的 该 S-矩阵 mapping table manually. This 脚本 可以 为 used 使用 该 example 在 [ S-参数 矩阵 sweep ](/hc/en-us/articles/360034403214-S-参数-矩阵-sweep) 和 it generates 该 same table without 使用 该 "auto symmetry" option 用于 mapping between rows. This manual mapping 是 not necessary 在 此 case because 该 "auto symmetry" tool 将 configure 该 table correctly 使用 minimal effort (compare 该 脚本 below 使用 该 one under "Scripted setup 和 分析" 在 [ S-参数 矩阵 sweep ](/hc/en-us/articles/360034403214-S-参数-矩阵-sweep) ). Therefore, 该 manual setup shown here 应该 only 为 used 在 particular cases 其中 该 "auto symmetry" tool does not apply 该 correct mapping.
    
    
    ##ADD SWEEP##deletesweep("s-参数 sweep"); # 如果 一个 sweep task named s-参数 sweep already exists, remove it
    addsweep(3); # 添加 s-参数 sweep task
    ##SWEEP SETUP##
    setsweep("s-参数 sweep", "Excite all ports", 0); # un-check "Excite all ports" 到 define active ports manually
    #    Define index entries 用于 s-矩阵 mapping table as 一个 结构体 使用 fields:
    #    Port, Mode : Define 该 端口 和 mode numbers.
    #    Active (0 或 1): When 一个 entry 是 defined as active, 一个 仿真 将 为 run 使用 该 源 设置 到 该 对应的 端口 和 mode combination.
    #    Map 从: For non-active entries 此 defines 该 entry 从 其中 该 mapping 是 done.
    #    Invert sign (0 或 1): This 是 only used 在 cases 其中 additional inversion 的 该 modal fields 是 required.  
    #    Map 向量: Array 使用 该 permutation 的 该 output indices 用于 该 input index given 通过 "Map 从".   
    # Active entries:
    index1 = 结构体; # Corresponds 到 S11,S21,...,S61
    index1.Port = "端口 1";
    index1.Mode = "mode 1";
    index1.Active = 1;
    index2 = 结构体; # Corresponds 到 S12,S22,...,S62
    index2.Port = "端口 1";
    index2.Mode = "mode 2";
    index2.Active = 1;
    index3 = 结构体; # Corresponds 到 S13,S23,...,S63
    index3.Port = "端口 2";
    index3.Mode = "mode 1";
    index3.Active = 1;
    index4 = 结构体; # Corresponds 到 S14,S24,...,S64
    index4.Port = "端口 2";
    index4.Mode = "mode 2";
    index4.Active = 1;
    # Mapped entries:
    index5 = 结构体; # Corresponds 到 S15,S25,...,S65
    index5.Port = "端口 3";
    index5.Mode = "mode 1";
    index5.Active = 0;
    index5.%Map 从% = 3;
    index5.%Invert sign% = 0;
    index5.%Map 向量% = [1,2,5,6,3,4]; # S15=S13, S25=S23, S35=S53, S45=S63, S55=S33, S65=S43 
    index6 = 结构体; # Corresponds 到 S16,S26,...,S66
    index6.Port = "端口 3";
    index6.Mode = "mode 2";
    index6.Active = 0;
    index6.%Map 从% = 4;
    index6.%Invert sign% = 0;
    index6.%Map 向量% = [1,2,5,6,3,4]; # S16=S14, S26=S24, S36=S54, S46=S64, S56=S34, S66=S44 
    ######
    # 添加 index entries 到 s-矩阵 mapping table
    addsweepparameter("s-参数 sweep",index1);
    addsweepparameter("s-参数 sweep",index2);
    addsweepparameter("s-参数 sweep",index3);
    addsweepparameter("s-参数 sweep",index4);
    addsweepparameter("s-参数 sweep",index5);
    addsweepparameter("s-参数 sweep",index6);

**参见**

[ List of commands ](/hc/en-us/articles/360037228834) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034404254-addsphere) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)[ ](/hc/en-us/articles/360034927973-setsetting), [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult) , [ Sweep scripting commands ](/hc/en-us/articles/360034922893-Sweep-scripting-commands) , [ Optimization scripting commands ](/hc/en-us/articles/360034922973-Optimization-scripting-commands) , [ Monte Carlo scripting commands ](/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
