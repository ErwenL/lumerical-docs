# setemeanalysis

Sets calculation parameters in MODE' EME analysis window.

| Syntax                             | Description                                          |
| ---------------------------------- | ---------------------------------------------------- |
| ?setemeanalysis;                   | Lists all the parameters in the EME analysis window. |
| setemeanalysis("property", value); | Sets the parameter named "property" to value.        |

**Examples**

This code will display the properties that can be set, and set the group spans column in
the EME analysis window's EME setup section.

```
# display properties that can be set using setemeanalysis command  
?setemeanalysis;  

# set group spans property to 1 micron (for 3 cell groups)  
setemeanalysis("group spans",[1e-6;1e-6;1e-6]);
```

This code will set up, run and collect the user s-matrix result from the propagation
sweep tool in Analysis mode.

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
```

This code will set up, run and export the user s-matrix result from the wavelength sweep
tool in Analysis mode to a file named "s_param".

```
# set wavelength sweep settings  
setemeanalysis("wavelength sweep", 1);  
setemeanalysis("start wavelength", 1.5e-6);  
setemeanalysis("stop wavelength", 1.6e-6);  
setemeanalysis("number of wavelength points", 31);  
setemeanalysis("calculate group delays", 1);  

# run wavelength sweep tool  
emesweep("wavelength sweep");  

# export the wavelength sweep result  
exportemesweep("s_param");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ Spot size converter ](**%20to%20be%20defined%20**) ,
[ getemeanalysis ](./getemeanalysis.md) , [ emesweep ](./emesweep.md) ,
[ exportemesweep ](https://optics.ansys.com/hc/en-us/articles/360037198114)
