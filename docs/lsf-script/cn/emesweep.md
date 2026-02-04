<!--
Translation from English documentation
Original command: emesweep
Translation date: 2026-02-03 23:48:58
-->

# emesweep

当使用EME求解器处于分析模式时，运行传播扫描工具（扫描电池组跨距的长度）或模式收敛扫描工具（扫描模式数量）。 

**Syntax** |  **Description**  
---|---  
emesweep;  emesweep("propagation sweep");  |  运行传播扫描。   
emesweep("wavelength sweep");  |  运行波长扫描。   
emesweep("mode convergence sweep");  |  运行模式收敛扫描。   
  
 **示例**

此代码将在分析模式中设置、运行并从传播扫描工具收集用户s矩阵结果。传播扫描的结果被打包在一个名为"S"的数据集中。
    
    
     #设置传播扫描参数
    setemeanalysis("propagation sweep",1);  
    setemeanalysis("parameter","group span 2");  
    setemeanalysis("start",10e-6);  
    setemeanalysis("stop",200e-6);  
    setemeanalysis("number of points",10);  
      
    emesweep;  
      
    S = getemesweep('S');  
    
     #绘制S21与组跨距的关系
    s21 = S.s21;  
    group_span = S.group_span_2;  
    plot(group_span,abs(s21)^2);

此代码将在分析模式中设置、运行并从模式收敛扫描工具收集用户s矩阵结果。模式收敛扫描的结果被打包在一个名为"S_mode_convergence_sweep"的数据集中。 
    
    
     #设置模式收敛扫描参数
     start_mode = 4; #设置较小的模式数以进行收敛测试
     mode_interval = 1; #设置收敛测试的模式间隔
    setnamed("EME","number of modes for all cell groups",25);   
    setemeanalysis("mode convergence sweep", 1);  
    setemeanalysis("start mode", start_mode);  
    setemeanalysis("mode interval", mode_interval);  
    
     #运行模式收敛扫描工具
    emesweep("mode convergence sweep");  
    
     #获取模式收敛扫描结果
    S = getemesweep("S_mode_convergence_sweep");  
    
     #绘制S21与模式数的关系
    s21 = S.s21;  
    modes = S.modes;  
    plot(modes, abs(s21)^2);

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [setemeanalysis](./setemeanalysis.md)
- [getemesweep](./getemesweep.md)
