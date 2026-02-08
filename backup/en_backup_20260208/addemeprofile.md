# addemeprofile

Adds an [EME profile monitor](/hc/en-us/articles/360034396474) that can be used to return the spatial electric and magnetic field profiles when using an EME solver region. The EME solver object must be set as the active solver for this command to work.

**Syntax** |  **Description**  
---|---  
addemeprofile; |  Add a profile monitor when using an EME solver region. This function does not return any data.  
addemeprofile(struct_data); |  Adds a EME profile monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add an index monitor to the EME solver region. The  setactivesolver  command is first used to set the EME solver region as the active solver.
    
    
    setactivesolver("EME");
    addemeprofile;

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ setactivesolver ](/hc/en-us/articles/360034409014-setactivesolver)
