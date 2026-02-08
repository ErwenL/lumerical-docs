# addheatfluxmonitor

Adds a [heat flux monitor](/hc/en-us/articles/360034398274) to the HEAT solver region. The monitor can only be added if the simulation environment already has a 'HEAT' solver present.

**Syntax** |  **Description**  
---|---  
addheatfluxmonitor; |  Adds a heat flux monitor to the simulation environment. This function does not return any data.  
addheatfluxmonitor(struct_data); |  Adds a heat flux monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add a 2D y-normal heat flux monitor to the HEAT solver region and set its dimension.
    
    
    addheatfluxmonitor;
    set("name","heat");
    set("monitor type",6);  # 2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);

**See Also**

[set](/hc/en-us/articles/360034928773-set), [ addtemperaturemonitor](/hc/en-us/articles/360034924333-addtemperaturemonitor)
