# addemfieldmonitor

Adds a frequency domain [EM (electro-magnetic) field monitor](https://optics.ansys.com/hc/en-us/articles/360034918553) to a simulation with 'DGTD' solver . Along with the EM field data the monitor also reports the net flux through the surface of the monitor. A DGTD solver region must be present in the objects tree for this command to work.

**Syntax** |  **Description**  
---|---  
addemfieldmonitor; |  Adds a frequency domain EM field monitor to the 'DGTD' solver. This function does not return any data.  
  
**Example 1**

The following script commands will add a frequency domain EM field monitor to the 'DGTD' solver already present in the objects tree and print all available properties of the monitor.
    
    
    addemfieldmonitor;
    ?set;

**Example 2**

The following script commands will add a frequency domain EM field monitor to the 'DGTD' solver, change its name, set its frequency span to be the same as the source, and assign it to a solid named "2D rectangle".
    
    
    addemfieldmonitor; 
    set("name","T");
    set("use source limits",1);
    set("reference source","plane_wave");  
    set("surface type","solid");
    set("solid","2D rectangle");

NOTE:  The script above assumes that there is already a solid named "2D rectangle" and a source named "plane_wave" present in the objects tree.  
---  
  
**See Also**

[ adddgtdsolver ](https://optics.ansys.com/hc/en-us/articles/360034925013-adddgtdsolver) , [ addemabsorptionmonitor ](https://optics.ansys.com/hc/en-us/articles/360034405054-addemabsorptionmonitor) , [ addemfieldtimemonitor ](https://optics.ansys.com/hc/en-us/articles/360034925053-addemfieldtimemonitor)
