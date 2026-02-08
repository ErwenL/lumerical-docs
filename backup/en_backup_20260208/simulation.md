# simulation

The script command simulation returns bandwidth related simulation properties. The time domain simulator will try to accommodate the current channels into non-overlapping simulation bandwidths. Simulation properties include the center frequency, sample rate, number of samples, frequency grid spacing, lower and upper frequency limits. If a single bandwidth is listed, this means all channels fit in the same bandwidth, otherwise multiple bandwidths are required to accommodate all channels with the current sample rate. 

The command also returns the list of source channels in the current simulation before the simulation estimate the simulation bandwidths. This list includes the overlapped bandwidths. Simulation properties include the center frequency, sample rate, number of samples, frequency grid spacing, lower and upper frequency limits. If a single bandwidth is listed, this means all channels fit in the same bandwidth, otherwise multiple bandwidths are required to accommodate all channels with the current sample rate. 

This function is valid during analysis or run-time mode only. 

**Syntax** |  **Description**  
---|---  
out = simulation(“bandwidth”);  |  Returns bandwidth related simulation properties.   
out = simulation(“channels”);  |  Returns the list of source channels in the current simulation before the simulation estimate the simulation bandwidths.   
out = simulation(“single”);  |  Returns the recommended setting for simulation using a single band (total field) that will make sure all channels are merged into one simulation bandwidth.   
  
###  Example 

Access simulation properties while the simulation is running, the circuit contains four laser sources. 
    
    
    #list number of simulated channels
    ?simulation("bandwidth");
    result: 
    1.9315e+014 1.6e+011 1024 1.5625e+008 1.9307e+014 1.9323e+014 
    1.9335e+014 1.6e+011 1024 1.5625e+008 1.9327e+014 1.9343e+01
    #list number of available channel sources
    ?simulation("channels");
    result: 
    1.931e+014 1.6e+011 1024 1.5625e+008 1.9302e+014 1.9318e+014 
    1.932e+014 1.6e+011 1024 1.5625e+008 1.9312e+014 1.9328e+014 
    1.933e+014 1.6e+011 1024 1.5625e+008 1.9322e+014 1.9338e+014 
    1.934e+014 1.6e+011 1024 1.5625e+008 1.9332e+014 1.9348e+014
    #list recommended setting for single bandwidth
    ?simulation("single");
    result: 
    1.9325e+014 3.2e+011 2048 1.5625e+008 1.9309e+014 1.9341e+014

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834)
