# switchtolayout

Switches the solver to LAYOUT mode. The LAYOUT mode allows you to add and modify simulation objects for a new simulation. Once a simulation is run, the solver goes into ANALYSIS mode and no simulation objects can be added or modified (Except for the "Analysis" tab of analysis groups). While in ANALYSIS mode, any commands to modify objects will return errors. You must switch to LAYOUT mode before modifying any objects. Note that any available results will be lost once the solver is switched back to LAYOUT mode. 

**Syntax** |  **Description**  
---|---  
switchtolayout;  |  Switches to LAYOUT mode from ANALYSIS mode.  This function does not return any data.   
  
**Example**

The following script commands will first run an FDTD simulation. The solver will go to ANALYSIS mode. The "switchtolayout" command is then used to go to LAYOUT mode so that the simulation temperature can be changed in the next line. 
    
    
    run;
    switchtolayout;
    setnamed("FDTD","simulation temperature",400);   # simulation temp. set to 400 K

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ layoutmode ](/hc/en-us/articles/360034924033-layoutmode) , [ run ](/hc/en-us/articles/360034931333-run) , [ setnamed ](/hc/en-us/articles/360034928793-setnamed)
