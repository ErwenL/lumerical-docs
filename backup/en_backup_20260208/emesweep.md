# emesweep

When in Analysis mode using EME solver, runs either propagation sweep tool which sweeps the length of a cell group span or mode convergence sweep tool which sweeps the number of modes. . 

**Syntax** |  **Description**  
---|---  
emesweep;  emesweep("propagation sweep");  |  Run propagation sweep.   
emesweep("wavelength sweep");  |  Run wavelength sweep.   
emesweep("mode convergence sweep");  |  Run mode convergence sweep.   
  
**Examples**

This code will set up, run and collect the user s-matrix result from the propagation sweep tool in Analysis mode. The result from the propagation sweep is packaged in a dataset called "S". 
    
    
    # set propagation sweep settings  
    setemeanalysis("propagation sweep",1);  
    setemeanalysis("parameter","group span 2");  
    setemeanalysis("start",10e-6);  
    setemeanalysis("stop",200e-6);  
    setemeanalysis("number of points",10);  
      
    emesweep;  
      
    S = getemesweep('S');  
    
    # plot S21 vs group span  
    s21 = S.s21;  
    group_span = S.group_span_2;  
    plot(group_span,abs(s21)^2);

This code will set up, run and collect the user s-matrix result from the mode convergence sweep tool in Analysis mode. The result from the mode convergence sweep is packaged in a dataset called "S_mode_convergence_sweep". 
    
    
    # set mode convergence sweep settings  
    start_mode = 4; #set smaller number of modes for convergence test  
    mode_interval = 1; #set mode interval for convergence test  
    setnamed("EME","number of modes for all cell groups",25);   
    setemeanalysis("mode convergence sweep", 1);  
    setemeanalysis("start mode", start_mode);  
    setemeanalysis("mode interval", mode_interval);  
    
    # run mode convergence sweep tool  
    emesweep("mode convergence sweep");  
    
    # get mode convergence sweep result  
    S = getemesweep("S_mode_convergence_sweep");  
    
    # plot S21 vs number of modes  
    s21 = S.s21;  
    modes = S.modes;  
    plot(modes, abs(s21)^2);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ Spot size converter ](**%20to%20be%20defined%20**) , [ setemeanalysis ](/hc/en-us/articles/360034405114-emesweep) , [ getemesweep ](/hc/en-us/articles/360034405134-getemesweep)
