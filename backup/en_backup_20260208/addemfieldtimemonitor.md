# addemfieldtimemonitor

Adds a time domain [EM (electro-magnetic) field monitor](/hc/en-us/articles/360034918493) to simulation with 'DGTD' solver. A DGTD solver region must be present in the objects tree for this command to work.

**Syntax** |  **Description**  
---|---  
addemfieldtimemonitor; |  Adds a time domain EM field monitor to the 'DGTD' solver. This function does not return any data.  
addemfieldtimemonitor(struct_data); |  Adds a time domain EM field monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example 1**

The following script commands will add a time domain EM field monitor to the 'DGTD' solver already present in the objects tree and print all available properties of the monitor.
    
    
    addemfieldtimemonitor;
    ?set;

**Example 2**

The following script commands will add a time domain EM field monitor to the 'DGTD' solver, change its name, and assign it to a solid named "2D rectangle".
    
    
    addemfieldtimemonitor; 
    set("name","time");
    set("geometry type","surface");
    set("surface type","solid");
    set("solid","2D rectangle");

NOTE:  The script above assumes that there is already a solid named "2D rectangle" present in the objects tree.  
---  
  
**Example 3**

The following script commands will add a 'point' time domain EM field monitor to the 'DGTD' solver and set its location.
    
    
    addemfieldtimemonitor; 
    set("name","time");
    set("geometry type","point");
    set("x",1e-6);
    set("y",0);
    set("z",0);

**See Also**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addemfieldmonitor ](/hc/en-us/articles/360034925053-addemfieldtimemonitor) , [ addemabsorptionmonitor ](/hc/en-us/articles/360034405054-addemabsorptionmonitor)
