# updateportmodes

Selects the specified modes in the selected port object in FDTD or MODE's EME solver, or updates already selected port modes. Modes are specified by the mode number in the eigensolver's mode list. For more information about the port object in FDTD see [ Ports ](/hc/en-us/articles/360034382554-Ports) .

**Syntax** |  **Description**  
---|---  
updateportmodes(modes_to_select); |  Selects the specified modes in the the selected port object. This function returns 1 if modes were updated successfully and -1 if there was an error updating the modes.  
updateportmodes; |  Updates the mode profiles of the selected mode ports.  
  
**Examples**

The following demonstrates different possible syntax that can be used to specify the list of modes to select.
    
    
    # select the second mode
    updateportmodes(2);
    # select the first 10 modes
    updateportmodes(1:10);
    # select modes 1, 2, 3, 9. Note that the first mode specified in the 
    # list will be used as the default source mode if the port is 
    # selected as the source port.
    updateportmodes([2,1,3,9]);
    # update already selected modes
    updateportmodes;

The following script adds a FDTD simulation region and port, then sets the name of the port, and selects the port modes and source mode.
    
    
    # add objects
    addfdtd; # add FDTD simulation region
    addport; # add port
    # set up port
    set("name","input_port"); # set the name of the port
    seteigensolver("bent waveguide",true); # set the solver to look for modes of a bent waveguide
    seteigensolver("bend radius",10e-6); # set bending radius to 10 um
    updateportmodes(1:2); # select the first 2 modes of the port
    # select the second mode of the port to be the source mode
    select("FDTD::ports"); # select the port group
    set("source port","input_port");
    set("source mode","mode 2");

**See Also**

[ Ports ](/hc/en-us/articles/360034382554-Ports) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ set ](/hc/en-us/articles/360034928773-set) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ clearportmodedata ](/hc/en-us/articles/360034409194-clearportmodedata)
