# havesweepresult

Checks whether a parameter parameter sweep/optimization/Monte Carlo/S-parameter sweep has results. Similar to  haveresult  . 

**Syntax** |  **Description**  
---|---  
?havesweepresult;  |  Returns 1 if any sweeps or optimizations, Monte Carlo analysis, or S-parameter sweeps have results. Returns 0 if data is not available.   
?havesweepresult("name");  |  Returns 1 if the specified sweep, optimization, Monte Carlo, or S-parameter sweep has results.   
?havesweepresult("name","data");  |  Returns 1 if the sweep, optimization, Monte Carlo, or S-parameter sweep named "name" has the specified result "data".   
  
**Examples**

The following example shows the output of  getsweepresult  and  havesweepdata  . Please download the example file from the [ Parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps) page Associate files. 
    
    
    ?getsweepresult;
    ?havesweepresult("thickness_optimization","fom trend");
    > thickness_sweep
    > thickness_optimization
    > result: 
    1   

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ runsweep ](/hc/en-us/articles/360034931413-runsweep) , [ getsweepresult ](/hc/en-us/articles/360034409814-getsweepresult) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ haveresult ](/hc/en-us/articles/360034409894-haveresult)
