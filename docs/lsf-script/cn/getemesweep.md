<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getemesweep -->

# getemesweep

    setemeanalysis("传播 sweep",1);  
    setemeanalysis("参数","group span 2");  
    setemeanalysis("start",10e-6);  
    setemeanalysis("stop",200e-6);  
    setemeanalysis("数字 of points",10);  
    emesweep;  
    S = getemesweep('S');  
    s21 = S.s21;  
    group_span = S.group_span_2;  
    plot(group_span,abs(s21)^2);
This code will set up, run 和 collect the 使用r s-矩阵 result from the 模式 convergence sweep tool in Analysis 模式. The result from the 模式 convergence sweep is packaged in a 数据集 called "S_mode_convergence_sweep".
    start_mode = 4; #set smaller 数字 of 模式 for convergence test  
    mode_interval = 1; #set 模式 interval for convergence test  
    setnamed("EME","数字 of 模式 for all cell groups",25);   
    setemeanalysis("模式 convergence sweep", 1);  
    setemeanalysis("start 模式", start_mode);  
    setemeanalysis("模式 interval", mode_interval);  
    emesweep("模式 convergence sweep");  
    S_mode = getemesweep("S_mode_convergence_sweep");  
    s21 = S_mode.s21;  
    模式 = S_mode.模式;  
    plot(模式, abs(s21)^2);
This code will set up, run 和 collect the 使用r s-矩阵 result from the perturbative 波长 convergence sweep tool in Analysis 模式. The result from the 波长 convergence sweep is packaged in a 数据集 called "S_wavelength_sweep".
    start_lam = 1.5e-6; #set start 波长 [m]  
    end_lam = = 1.6e-6; #set end 波长 [m]  
    lam_res = 100; #set 波长 for convergence test  
    setnamed("EME","数字 of 模式 for all cell groups",25);   
    setemeanalysis("波长 sweep",1);  
    setemeanalysis("start 波长",start_lam);   
    setemeanalysis("stop 波长",end_lam);
    setemeanalysis("数字 of 波长 points",lam_res);
    emesweep("波长 sweep");  
    S_lambda = getemesweep("S_wavelength_sweep");  
    s21 = S_lambda.s21;  
    lambda = S_lambda.波长;  
    plot(lambda, abs(s21)^2);

**语法** | **描述**
---|---
getemesweep("S"); | Gets the user s-矩阵 result from an EME 传播 sweep named "S".
getemesweep("S_mode_convergence_sweep"); | Gets the user s-矩阵 result from an EME 模式 convergence sweep named "S_mode_convergence_sweep".
getemesweep("S_wavelength_sweep"); | Gets the user s-矩阵 result from an EME 波长 convergence sweep named "S_wavelength_sweep".

**示例**

This code will set up, run and collect the user s-矩阵 result from the 传播 sweep tool in Analysis 模式. The result from the 传播 sweep is packaged in a 数据集 called "S".

This code will set up, run and collect the user s-矩阵 result from the 传播 sweep tool in Analysis 模式. The result from the 传播 sweep is packaged in a 数据集 called "S".

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ Spot size converter ](**%20to%20be%20defined%20**) , [ setemeanalysis ](/hc/en-us/articles/360034405134-getemesweep) , [ emesweep, ](/hc/en-us/articles/360034405114-emesweep) [ fast broadband EME ](https://kx.lumerical.com/t/new-fast-broadband-eme-feature/15326)
