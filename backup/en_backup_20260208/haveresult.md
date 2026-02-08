# haveresult

Used to see a simulation object (such as a monitor) has any results. 

Note: This command is very similar to havedata, but is intended to be used with the getresult command, rather than getdata. 

**Syntax** |  **Description**  
---|---  
haveresult;  |  Returns 1 if any simulation objects currently have any results.   
haveresult("name");  |  Returns 1 if "name" has any results, and 0 if it does not.   
haveresult("name","data");  |  Returns 1 if the "name" has a result named "data", and 0 if it does not.   
  
**Examples**

The following example shows the output of ?getresult, when it is called after a simulation has been run. There are several monitors and a source with available results. 
    
    
    ?getresult;
    time
    T
    R
    ModeSource
    ?haveresult;  # check if results are available
    result: 
    1 
    ?haveresult("T"); # check if 'T' has any results
    result: 
    1 
    ?haveresult("TT"); # check if 'TT' has any results 
    result: 
    0 
    ?haveresult("T","E"); # check if 'T' has a result named 'E'
    result: 
    1  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ havedata ](/hc/en-us/articles/360034930213-havedata) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ cleardcard ](/hc/en-us/articles/360034930273-cleardcard) , [ workspace ](/hc/en-us/articles/360034409394-workspace) , [ havesweepdata ](/hc/en-us/articles/360034409934-havesweepdata)
