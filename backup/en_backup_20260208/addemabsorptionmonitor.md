# addemabsorptionmonitor

Adds an [absorption monitor](/hc/en-us/articles/360034918573) to the 'DGTD' solver in Finite Element IDE. The monitor reports the power absorbed within the monitor volume. A DGTD solver region must be present in the objects tree for this command to work.

**Syntax** |  **Description**  
---|---  
addemabsorptionmonitor; |  Adds an absorption monitor to the 'DGTD' solver. This function does not return any data.  
addemabsorptionmonitor(struct_data); |  Adds an absorption monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example 1**

The following script commands will add an absorption monitor to the 'DGTD' solver already present in the objects tree and print all available properties of the monitor.
    
    
    addemabsorptionmonitor;
    ?set;

**Example 2**

The following script commands will add an absorption monitor to the 'DGTD' solver, change its name, set its frequency span to be the same as the source, and assign it to a solid named "nanoparticle".
    
    
    addemabsorptionmonitor; 
    set("name","Pabs");
    set("use source limits",1);
    set("reference source","plane_wave");  
    set("volume type","solid");
    set("volume solid","nanoparticle");

NOTE:  The script above assumes that there is already a solid named "nanoparticle" and a source named "plane_wave" present in the objects tree.  
---  
  
**See Also**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver) , [ addemfieldmonitor ](/hc/en-us/articles/360034405054-addemabsorptionmonitor) , [ addemfieldtimemonitor ](/hc/en-us/articles/360034925053-addemfieldtimemonitor)
