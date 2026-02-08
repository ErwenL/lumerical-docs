# addindex

Adds an index monitor to the simulation environment. In MODE an active varFDTD region needs to be present for this command to work.

**Syntax** |  **Description**  
---|---  
addindex; |  Adds an index monitor to the simulation environment. This function does not return any data.  
addindex(struct_data); |  Adds an index monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script command will add a 2D y-normal index monitor to the simulation region and set its dimension.
    
    
    addindex;
    set("name","index_monitor");
    set("monitor type",2);  # 2D y-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("z",10e-6);
    set("z span",5e-6);

If an FDTD the index monitor holds results automatically without running simulations if a solver region is present. The following script command will add a solver region following the script above and will visualize the index preview.
    
    
    addfdtd;
    n = getresult("index_monitor","index preview");
    visualize(n);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ set ](/hc/en-us/articles/360034928773-set) , [ addfdtd ](/hc/en-us/articles/360034924173-addfdtd) , [ addvarfdtd ](/hc/en-us/articles/360034924193-addvarfdtd) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ visualize ](/hc/en-us/articles/360034410514-visualize)
