# addjfluxmonitor

Adds a current flux monitor to the simulation environment. This command requires the presence of a CHARGE solver region in the objects tree.

**Syntax** |  **Description**  
---|---  
addjfluxmonitor; |  Adds a current flux monitor to the simulation environment. This function does not return any data.  
addjfluxmonitor(struct_data); |  Adds a current flux monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a 2D y-normal current flux monitor to the simulation environment and set its dimension.
    
    
    addjfluxmonitor;
    set("name","current_flux");
    set("monitor type",7);  # 2D z-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ addefieldmonitor ](/hc/en-us/articles/360034924633-addefieldmonitor) , [ addchargemonitor ](/hc/en-us/articles/360034924613-addchargemonitor) , [ addbandstructuremontor ](/hc/en-us/articles/360034924653-addbandstructuremonitor)
