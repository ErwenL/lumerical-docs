# havedata

Used to see a simulation object (such as a monitor) has any data. This command is very similar to haveresult, but is intended to be used with the getdata command, rather than getresult. 

**Syntax** |  **Description**  
---|---  
havedata;  |  Returns 1 if any simulation objects have raw data, and 0 if none have any raw data.   
havedata("name");  |  Returns 1 if "name" has raw data, and 0 if it does not have any raw data.   
havedata("name","data");  |  Returns 1 if "name" has the raw data named "data", and 0 if it does not have that data.   
  
**Examples**

The following example shows the output of ?getdata, when it is called after a simulation has been run. There is a monitor group in the simulation that has an analysis script file and at least one result parameter. Before the analysis script is run, the monitor group does not have data, after it is run the monitor group has data that is stored in the result parameter. 
    
    
    ?getdata;
    local sources:
     source2 
    local monitors:
     monitor group 
    ?havedata("monitor group");
    result: 
    0 
    runanalysis("monitor group");
    ?havedata("monitor group");
    result: 
    1  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ haveresult ](/hc/en-us/articles/360034409894-haveresult) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ cleardcard ](/hc/en-us/articles/360034930273-cleardcard) , [ workspace ](/hc/en-us/articles/360034409394-workspace) , [ havesweepdata ](/hc/en-us/articles/360034409934-havesweepdata)
