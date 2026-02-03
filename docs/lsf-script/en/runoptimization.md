# runoptimization

Optimizes a property from a chosen element under specified condition.

**Syntax** |  **Description**  
---|---  
x=runoptimization(element, property, min, max, analyzer, result, ’target’, target, tolerance=1e-9, iterations=2000) |  Optimizes property from element until a target for an analyzer result is reached. Function returns an array with two columns, the firs column contains the property values and the second column contains the result values.  
x=runoptimization(element, property, min, max, analyzer, result, ’minimize’, tolerance=1e-9, iterations=2000) |  Optimizes property from element until a minimum value for an analyzer result is reached. Function returns an array with two columns, the firs column contains the property values and the second column contains the result values.  
x=runoptimization(element, property, min, max, analyzer, result, ’maximize’, tolerance=1e-9, iterations=2000) |  Optimizes property from element until a maximum value for an analyzer result is reached. Function returns an array with two columns, the firs column contains the property values and the second column contains the result values.  
  
**Example**

### The following script line optimizes the thermal noise for a PIN Photodetector for target
    
    
    x=runoptimization("PIN Photodetector","thermal noise",1e-20,1e-17,"Eye Diagram","measurement/Q factor","target",6,1e-2);

### The following script line searches the minimum cutoff frequency for a LP Bessel Filter
    
    
    x=runoptimization("LP Bessel Filter","cutoff frequency",1e+09,1e+10,"Eye Diagram","measurement/log of BER","minimize");

### The following script line searches the maximum cutoff frequency for a LP Bessel Filter
    
    
    x=runoptimization("LP Bessel Filter","cutoff frequency",1e+09,1e+10,"Eye Diagram","measurement/Q factor","maximize");
