# addthermalinsulatingbc

Adds a new insulating [(thermal) boundary condition](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-) to the HEAT or CHARGE solver. A HEAT or CHARGE solver region must be present in the objects tree before this boundary condition can be added. If both solvers are present then the intended solver's name must be provided as an argument to the script command. 

The insulating (thermal) boundary condition can only be added to the CHARGE solver when the solver's temperature dependency is set to 'coupled'. 

**Syntax** |  **Description**  
---|---  
addthermalinsulatingbc; |  Adds an insulating (thermal) boundary condition to the HEAT or CHARGE solver (whichever is present in the objects tree). This function does not return any data.  
addthermalinsulatingbc("solver_name"); |  Adds an insulating (thermal) boundary condition to the desired solver defined by the argument "solver_name". The options are "HEAT" and "CHARGE". This function does not return any data.  
  
**Example 1**

The following script commands will add an insulating (thermal) boundary condition to the solver already present in the objects tree and print all available properties of the boundary condition.
    
    
    addthermalinsulatingbc;  
    ?set;

**Example 2**

The following script commands will add an insulating (thermal) boundary condition to the HEAT solver already present in the objects tree. It will then name the boundary condition and assign it to the -x and +x simulation region boundaries.
    
    
    addthermalinsulatingbc("HEAT");  
    
    set("name","ins_x_bc");  
    set("surface type","simulation region");  
    set("x min",1);  
    set("x max",1);

**See Also**

[addtemperaturebc](/hc/en-us/articles/360034924833-addthermalinsulatingbc), [addconvectionbc](/hc/en-us/articles/360034404854-addconvectionbc), [addradiationbc](/hc/en-us/articles/360034924813-addradiationbc), [addthermalpowerbc](/hc/en-us/articles/360034404874-addthermalpowerbc), [addheatfluxbc](/hc/en-us/articles/360034404894-addheatfluxbc), [addvoltagebc](/hc/en-us/articles/360034404914-addvoltagebc)
