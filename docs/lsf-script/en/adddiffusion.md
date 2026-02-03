# adddiffusion

Adds a [diffusion doping region](/hc/en-us/articles/360034918673) to the simulation environment. This command requires a CHARGE solver region to be present in the objects tree.

**Syntax** |  **Description**  
---|---  
adddiffusion; |  Add a diffusion doping region in the simulation environment. This function does not return any data.  
adddiffusion(struct_data); |  Adds a diffusion doping region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add a n-type diffusion doping object and set its properties. The face where the dopants are introduced is defined by the "source face" property and the peak doping is defined by the "concentration" property. The "junction width" property defines the distance over which the doping drops from the (peak) concentration to the low "ref concentration" at the other faces of the doping object.
    
    
    adddiffusion;
    set("name","nwell");
    # set dimensionset("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",1e-6);
    set("z",5e-6);
    set("z span",1e-6);
    # set doping profile
    set("dopant type","n");
    set("source face",6);  # upper z
    set("junction width",0.2e-6);
    set("concentration",1e25);  # SI unit (/m3)

The figure below shows the resulting doping profile.

More information about the doping object itself, including the diffusion parameters can be found in [this article](https://support.lumerical.com/hc/en-us/articles/360034918673).

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ adddope ](/hc/en-us/articles/360034404594-adddope)
