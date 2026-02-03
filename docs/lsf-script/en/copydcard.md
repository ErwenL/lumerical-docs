# copydcard

Will create a global copy of any d-card currently in memory. 

**Syntax** |  **Description**  
---|---  
copydcard( "name");  |  Will create a global copy of any d-card currently in memory called "name". By default, the new name will be "::global_name". For example, copydcard("mode1"); sends mode1 to the deck, named global_mode1.  This function does not return any data.   
copydcard( "name", "newname");  |  Will create a global copy of any d-card currently in memory called "name". The new name will be "::newname".   
  
**Examples**

Sending modes to the d-card and run overlap analysis, eg, in the FDE solver 
    
    
    copydcard("mode1","test_mode1");
    copydcard("mode2","test_mode2");
    ?overlap("test_mode1","test_mode2");

Sending field profiles to the d-card and run overlap analysis, eg, in the FDTD solver 
    
    
    copydcard("::model::R","test_mode1"); # for the fields recorded by R, where R is the monitor name
    copydcard("::model::T","test_mode2"); # for the fields recorded by T, where T is the monitor name
    ?overlap("test_mode1","test_mode2");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ havedata ](/hc/en-us/articles/360034930213-havedata) , [ cleardcard ](/hc/en-us/articles/360034930273-cleardcard) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ savedcard ](/hc/en-us/articles/360034411154-savedcard)
