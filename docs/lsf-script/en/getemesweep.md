# getemesweep

Gets the user s-matrix result from a propagation sweep, mode convergence sweep, or
perturbative wavelength sweep.

| **Syntax**                               | **Description**                                                                                    |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------- |
| getemesweep("S");                        | Gets the user s-matrix result from an EME propagation sweep named "S".                             |
| getemesweep("S_mode_convergence_sweep"); | Gets the user s-matrix result from an EME mode convergence sweep named "S_mode_convergence_sweep". |
| getemesweep("S_wavelength_sweep");       | Gets the user s-matrix result from an EME wavelength convergence sweep named "S_wavelength_sweep". |

**Examples**

This code will set up, run and collect the user s-matrix result from the propagation
sweep tool in Analysis mode. The result from the propagation sweep is packaged in a
dataset called "S".

```
# set propagation sweep settings  
setemeanalysis("propagation sweep",1);  
setemeanalysis("parameter","group span 2");  
setemeanalysis("start",10e-6);  
setemeanalysis("stop",200e-6);  
setemeanalysis("number of points",10);  

# run propagation sweep tool  
emesweep;  

# get propagation sweep result  
S = getemesweep('S');  

# plot S21 vs group span  
s21 = S.s21;  
group_span = S.group_span_2;  
plot(group_span,abs(s21)^2);
```

This code will set up, run and collect the user s-matrix result from the mode
convergence sweep tool in Analysis mode. The result from the mode convergence sweep is
packaged in a dataset called "S_mode_convergence_sweep".

```
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
S_mode = getemesweep("S_mode_convergence_sweep");  

# plot S21 vs number of modes  
s21 = S_mode.s21;  
modes = S_mode.modes;  
plot(modes, abs(s21)^2);
```

This code will set up, run and collect the user s-matrix result from the perturbative
wavelength convergence sweep tool in Analysis mode. The result from the wavelength
convergence sweep is packaged in a dataset called "S_wavelength_sweep".

```
# set wavelength convergence sweep settings  
start_lam = 1.5e-6; #set start wavelength [m]  
end_lam = = 1.6e-6; #set end wavelength [m]  
lam_res = 100; #set wavelength for convergence test  
setnamed("EME","number of modes for all cell groups",25);   
setemeanalysis("wavelength sweep",1);  
setemeanalysis("start wavelength",start_lam);   
setemeanalysis("stop wavelength",end_lam);
setemeanalysis("number of wavelength points",lam_res);
  
 # run wavelength convergence sweep tool  
emesweep("wavelength sweep");  
  
 # get mode convergence sweep result  
S_lambda = getemesweep("S_wavelength_sweep");  
  
# plot S21 vs number of wavelength  
s21 = S_lambda.s21;  
lambda = S_lambda.wavelength;  
plot(lambda, abs(s21)^2);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ Spot size converter ](**%20to%20be%20defined%20**) ,
[ setemeanalysis ](./getemesweep.md) , [ emesweep, ](./emesweep.md)
[ fast broadband EME ](https://kx.lumerical.com/t/new-fast-broadband-eme-feature/15326)
