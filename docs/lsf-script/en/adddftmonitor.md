# adddftmonitor

Adds a frequency domain field profile monitor to the simulation environment. This monitor will snap to the nearest mesh cell to record the data by default. To record data exactly where the monitor is placed, change the “spatial interpolation” settings under “Advanced” in the object properties to “specified position”. Specifics regarding each spatial interpolation option can be found in the Knowledge Base article on [Frequeny-domain monitor](https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-Profile-and-Power-monitor-Simulation-object).

**Syntax** |  **Description**  
---|---  
adddftmonitor; |  Adds a field profile monitor to the simulation environment. This function does not return any data.  
adddftmonitor(struct_data); |  Adds a field profile monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
The following script commands will add a 2D z-normal frequency domain field profile monitor to the simulation region and set its dimension.
    
    
    adddftmonitor;  
    set("name","field_profile");  
    set("monitor type",7); # 2D z-normal  
    set("x",0);  
    set("x span",5e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",0);

**See Also**

[**List of commands**](https://optics.ansys.com/hc/en-us/articles/360037228834), [**set**](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
