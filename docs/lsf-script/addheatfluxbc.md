# addheatfluxbc

Adds a new heat flux boundary condition to the HEAT or CHARGE solver [ [ Boundary Conditions (Thermal Simulation) ](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-) ]. A HEAT or CHARGE solver region must be present in the objects tree before this boundary condition can be added. If both solvers are present then the intended solver's name must be provided as an argument to the script command.

The heat flux boundary condition can only be added to the CHARGE solver when the solver's temperature dependency is set to 'coupled'.

**Syntax** |  **Description**  
---|---  
addheatfluxbc; |  Adds a heat flux boundary condition to the HEAT or CHARGE solver (whichever is present in the objects tree). This function does not return any data.  
addheatfluxbc("solver_name"); |  Adds a heat flux boundary condition to the desired solver defined by the argument "solver_name". The options are "HEAT" and "CHARGE". This function does not return any data.  
  
**Example 1**

The following script commands will add a heat flux boundary condition to the solver already present in the objects tree and print all available properties of the boundary condition.
    
    
    addheatfluxbc;
    ?set;

**Example 2**

The following script commands will add a steady state heat flux boundary condition to the HEAT solver already present in the objects tree. It will then name the boundary condition, assign it to the -x simulation region boundary, and set the heat flux to 1e6 W/m^2.
    
    
    addheatfluxbc("HEAT");
    set("name","P_in");
    set("heat flux",1e6);
    set("surface type","simulation region");
    set("x min",1);

**See Also**

[ addtemperaturebc ](/hc/en-us/articles/360034404894-addheatfluxbc) , [ addconvectionbc ](/hc/en-us/articles/360034404854-addconvectionbc) , [ addradiationbc ](/hc/en-us/articles/360034924813-addradiationbc) , [ addthermalpowerbc ](/hc/en-us/articles/360034404874-addthermalpowerbc) , [ addthermalinsulatingbc ](/hc/en-us/articles/360034924833-addthermalinsulatingbc) , [ addvoltagebc ](/hc/en-us/articles/360034404914-addvoltagebc)
