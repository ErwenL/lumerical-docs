# clearportmodedata

Clears mode data from selected FDTD port and ports in MODE's EME solver. For more information about the port object see [ Ports ](/hc/en-us/articles/360034382554-Ports) .

**Syntax** |  **Description**  
---|---  
clearportmodedata; |  Clears mode data from selected port. This function does not return any data.  
  
**Example** The following script adds a FDTD simulation region and port, then sets the name of the port, and selects the port modes then clears the selected port mode data.
    
    
    # add objects  
    addfdtd; # add FDTD simulation region
    addport; # add port
    # set up port
    set("name","input_port"); # set the name of the port
    seteigensolver("bent waveguide",true); # set the solver to look for modes of a bent waveguide
    seteigensolver("bend radius",10e-6); # set bending radius to 10 um
    updateportmodes(1:2); # select the first 2 modes of the port
    # clear the selected mode data
    clearportmodedata;

**See Also**

[ Ports ](/hc/en-us/articles/360034382554-Ports) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ set ](/hc/en-us/articles/360034928773-set) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ updateportmodes ](/hc/en-us/articles/360034409174-updateportmodes)
