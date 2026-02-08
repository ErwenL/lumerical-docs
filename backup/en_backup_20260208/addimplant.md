# addimplant

Adds a implant doping region to the simulation environment. This command requires a CHARGE solver region to be present in the objects tree.

**Syntax** |  **Description**  
---|---  
adddimplant; |  Add a implant doping region in the simulation environment. This function does not return any data.  
adddimplant(struct_data); |  Adds a implant doping region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add a n-type implant doping object and set its properties. The implantation direction is defined by the "surface normal" property and the peak doping is defined by the "peak concentration" property.
    
    
    addimplant;
    set("name","nwell");
    # set dimension
    V=[-0.5,-0.5;0.5,-0.5;0.5,0.5;-0.5,0.5]*1e-6; # SI unit (m)
    set("vertices",V);
    # set doping profile
    set("dopant type","n");
    set("surface normal","y"); 
    set("source theta",45);
    set("source phi",90);
    set("distribution function","Pearson4");
    set("peak concentration",1e24);  # SI unit (1/m3), equivalent to 1e18 1/cm3

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ adddope ](/hc/en-us/articles/360034404594-adddope) ,
