# addbandstructuremonitor

Adds a [band structure monitor](/hc/en-us/articles/360034398174) to the simulation environment. This command requires the presence of a CHARGE solver region in the objects tree.

**Syntax** |  **Description**  
---|---  
addbandstructuremonitor; |  Adds a band structure monitor to the simulation environment. This function does not return any data.  
addbandstructuremonitor(struct_data); |  Adds a band structure monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a bandstructure monitor to the simulation environment along the z axis, set its dimension, and enable saving the energy band for the vacuum level (Evac).
    
    
    addbandstructuremonitor;
    set("name","band");
    set("monitor type",4);  # linear z
    set("x",0);
    set("y",0);
    set("z",0);
    set("z span",5e-6);
    set("record Evac",1);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ addefieldmonitor ](/hc/en-us/articles/360034924633-addefieldmonitor) , [ addchargemonitor ](/hc/en-us/articles/360034924613-addchargemonitor) , [ addjfluxmonitor ](/hc/en-us/articles/360034924673-addjfluxmonitor)
