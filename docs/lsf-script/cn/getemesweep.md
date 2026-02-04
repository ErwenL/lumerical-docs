<!--
Translation from English documentation
Original command: getemesweep
Translation date: 2026-02-04 22:50:00
-->

# getemesweep

获取 该 用户 s-矩阵 result 从 一个 propagation sweep, mode convergence sweep, 或 perturbative 波长 sweep.

**语法** |  **描述**  
---|---  
getemesweep("S"); |  获取 该 用户 s-矩阵 result 从 一个 EME propagation sweep named "S".  
getemesweep("S_mode_convergence_sweep"); |  获取 该 用户 s-矩阵 result 从 一个 EME mode convergence sweep named "S_mode_convergence_sweep".  
getemesweep("S_wavelength_sweep"); |  获取 该 用户 s-矩阵 result 从 一个 EME 波长 convergence sweep named "S_wavelength_sweep".  
  
**示例**

This code 将 设置 up, run 和 collect 该 用户 s-矩阵 result 从 该 propagation sweep tool 在 Analysis mode. The result 从 该 propagation sweep 是 packaged 在 一个 dataset called "S".
    
    
    # 设置 propagation sweep settings  
    setemeanalysis("propagation sweep",1);  
    setemeanalysis("参数","group span 2");  
    setemeanalysis("start",10e-6);  
    setemeanalysis("stop",200e-6);  
    setemeanalysis("数字 的 points",10);  
    
    # run propagation sweep tool  
    emesweep;  
    
    # 获取 propagation sweep result  
    S = getemesweep('S');  
    
    # plot S21 vs group span  
    s21 = S.s21;  
    group_span = S.group_span_2;  
    plot(group_span,abs(s21)^2);

This code 将 设置 up, run 和 collect 该 用户 s-矩阵 result 从 该 mode convergence sweep tool 在 Analysis mode. The result 从 该 mode convergence sweep 是 packaged 在 一个 dataset called "S_mode_convergence_sweep".
    
    
    # 设置 mode convergence sweep settings  
    start_mode = 4; #设置 smaller 数字 的 modes 用于 convergence test  
    mode_interval = 1; #设置 mode interval 用于 convergence test  
    setnamed("EME","数字 的 modes 用于 all 单元格 groups",25);   
    setemeanalysis("mode convergence sweep", 1);  
    setemeanalysis("start mode", start_mode);  
    setemeanalysis("mode interval", mode_interval);  
    
    # run mode convergence sweep tool  
    emesweep("mode convergence sweep");  
    
    # 获取 mode convergence sweep result  
    S_mode = getemesweep("S_mode_convergence_sweep");  
    
    # plot S21 vs 数字 的 modes  
    s21 = S_mode.s21;  
    modes = S_mode.modes;  
    plot(modes, abs(s21)^2);

This code 将 设置 up, run 和 collect 该 用户 s-矩阵 result 从 该 perturbative 波长 convergence sweep tool 在 Analysis mode. The result 从 该 波长 convergence sweep 是 packaged 在 一个 dataset called "S_wavelength_sweep".
    
    
    # 设置 波长 convergence sweep settings  
    start_lam = 1.5e-6; #设置 start 波长 [m]  
    end_lam = = 1.6e-6; #设置 end 波长 [m]  
    lam_res = 100; #设置 波长 用于 convergence test  
    setnamed("EME","数字 的 modes 用于 all 单元格 groups",25);   
    setemeanalysis("波长 sweep",1);  
    setemeanalysis("start 波长",start_lam);   
    setemeanalysis("stop 波长",end_lam);
    setemeanalysis("数字 的 波长 points",lam_res);
      
     # run 波长 convergence sweep tool  
    emesweep("波长 sweep");  
      
     # 获取 mode convergence sweep result  
    S_lambda = getemesweep("S_wavelength_sweep");  
      
    # plot S21 vs 数字 的 波长  
    s21 = S_lambda.s21;  
    lambda = S_lambda.波长;  
    plot(lambda, abs(s21)^2);

**参见**

[ List of commands ](/hc/en-us/articles/360037228834) , [ Spot size converter ](**%20to%20be%20defined%20**) , [ setemeanalysis ](/hc/en-us/articles/360034405134-getemesweep) , [ emesweep, ](/hc/en-us/articles/360034405114-emesweep) [ fast broadband EME ](https://kx.lumerical.com/t/new-fast-broadband-eme-feature/15326)
