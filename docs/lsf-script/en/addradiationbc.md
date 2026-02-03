# addradiationbc

Adds a new radiation boundary condition to the HEAT or CHARGE solver [ [ Boundary Conditions (Thermal Simulation) ](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-) ]. A HEAT or CHARGE solver region must be present in the objects tree before this boundary condition can be added. If both solvers are present then the intended solver's name must be provided as an argument to the script command.

The radiation boundary condition can only be added to the CHARGE solver when the solver's temperature dependency is set to 'coupled'.

**Syntax** |  **Description**  
---|---  
addradiationbc; |  Adds a radiation boundary condition to the HEAT or CHARGE solver (whichever is present in the objects tree). This function does not return any data.  
addradiationbc("solver_name"); |  Adds a radiation boundary condition to the desired solver defined by the argument "solver_name". The options are "HEAT" and "CHARGE". This function does not return any data.  
  
**Example 1**

The following script commands will add a radiation boundary condition to the solver already present in the objects tree and print all available properties of the boundary condition.
    
    
    addradiationbc;
    ?set;

**Example 2**

The following script commands will add a radiation boundary condition to the HEAT solver already present in the objects tree. The boundary condition is then assigned to the interface (surfaces) between silicon and air. The ambient temperature is set to 300 K and the emissivity is set to 0.9.
    
    
    addradiationbc("HEAT");
    set("name","radiation_air");
    set("ambient temperature",300);
    set("emissivity",0.9);
    set("surface type","material:material");
    set("material 1","Si (Silicon)");
    set("material 2","Air");

NOTE:  The 'materials' folder in the objects tree must already contain the materials used in the script commands to set up the boundary condition.  
---  
  
**Example 3**

The following script commands will add a radiation boundary condition to the HEAT solver already present in the objects tree. The boundary condition is assigned to the top (+z) surface of the simulation region. The ambient temperature is set to 300 K and the emissivity is set to 0.9.
    
    
    addradiationbc("HEAT");
    set("name","radiation_top");
    set("ambient temperature",300);
    set("emissivity",0.9);
    set("surface type","simulation region");
    set("z max",1);

**See Also**

[ addtemperaturebc ](/hc/en-us/articles/360034924813-addradiationbc) , [ addconvectionbc ](/hc/en-us/articles/360034404854-addconvectionbc) , [ addthermalpowerbc ](/hc/en-us/articles/360034404874-addthermalpowerbc) , [ addheatfluxbc ](/hc/en-us/articles/360034404894-addheatfluxbc) , [ addthermalinsulatingbc ](/hc/en-us/articles/360034924833-addthermalinsulatingbc) , [ addvoltagebc ](/hc/en-us/articles/360034404914-addvoltagebc)
