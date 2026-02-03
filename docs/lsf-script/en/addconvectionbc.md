# addconvectionbc

Adds a new convection boundary condition to the HEAT or CHARGE solver [ [ Boundary Conditions (Thermal Simulation) ](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-) ]. A HEAT or CHARGE solver region must be present in the objects tree before this boundary condition can be added. If both solvers are present then the intended solver's name must be provided as an argument to the script command.

The convection boundary condition can only be added to the CHARGE solver when the solver's temperature dependency is set to 'coupled'.

**Syntax** |  **Description**  
---|---  
addconvectionbc; |  Adds a convection boundary condition to the HEAT or CHARGE solver (whichever is present in the objects tree). This function does not return any data.  
addconvectionbc("solver_name"); |  Adds a convection boundary condition to the desired solver defined by the argument "solver_name". The options are "HEAT" and "CHARGE". This function does not return any data.  
  
**Example 1**

The following script commands will add a convection boundary condition to the solver already present in the objects tree and print all available properties of the boundary condition.
    
    
    addconvectionbc;
    ?set;

**Example 2**

The following script commands will add a convection boundary condition to the HEAT solver already present in the objects tree. The boundary condition is then assigned to the interface (surfaces) between silicon and air. The model is set to a constant h (convection heat transfer coefficient) and the value of h is set to 10 W/m^2-K. The ambient temperature is set to 300 K.
    
    
    addconvectionbc("HEAT");
    set("name","conv_air");
    set("convection model","constant");
    set("ambient temperature",300);
    set("h convection",10);
    set("surface type","material:material");
    set("material 1","Si (Silicon)");
    set("material 2","Air");

NOTE:  The 'materials' folder in the objects tree must already contain the materials used in the script commands to set up the boundary condition.  
---  
  
**Example 3**

The following script commands will add a convection boundary condition to the HEAT solver already present in the objects tree. The boundary condition is assigned to the interface (surfaces) between silicon and air. The model is set to forced convection. The fluid material is automatically selected from the material combination and the length scale, fluid velocity, and ambient temperature are set from the script.
    
    
    addconvectionbc("HEAT");
    set("name","conv_air");
    set("convection model","forced");
    set("ambient temperature",300);
    set("length scale",1e-3);  # 1 mm
    set("fluid velocity",100);  # m/sec
    set("surface type","material:material");
    set("material 1","Si (Silicon)");
    set("material 2","Air");

**Example 4**

The following script commands will add a convection boundary condition to the HEAT solver already present in the objects tree. The boundary condition is assigned to the top (+z) surface of the simulation region. The model is set to a constant h (convection heat transfer coefficient) and the value of h is set to 100 W/m^2-K. The ambient temperature is set to 300 K.
    
    
    addconvectionbc("HEAT");
    set("name","conv_top");
    set("convection model","constant");
    set("ambient temperature",300);
    set("h convection",100);
    set("surface type","simulation region");
    set("z max",1);
 
**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [addtemperaturebc](./addtemperaturebc.md)
- [addradiationbc](./addradiationbc.md)
- [addthermalpowerbc](./addthermalpowerbc.md)
- [addheatfluxbc](./addheatfluxbc.md)
- [addthermalinsulatingbc](./addthermalinsulatingbc.md)
- [addvoltagebc](./addvoltagebc.md)
