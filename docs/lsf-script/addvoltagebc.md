# addvoltagebc

Adds a new voltage boundary condition to the HEAT solver [[Boundary Conditions (Thermal Simulation)](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-)]. A HEAT solver region must be present in the objects tree before an electrical contact boundary condition can be added.

**Syntax** |  **Description**  
---|---  
addvoltagebc; |  Adds a voltage boundary condition to the HEAT solver. This function does not return any data.  
  
**Example 1**

The following script commands will add a voltage boundary condition to the CHARGE solver already present in the objects tree and print all available properties of the boundary condition.
    
    
    addvoltagebc;  
    ?set;

**Example 2**

The following script commands will create a voltage boundary condition with a fixed steady state voltage assigned to a solid named cathode. The objects tree must already have a HEAT solver and a geometry named 'cathode' present.
    
    
    addvoltagebc;  
    
    set("name","cathode");  
    set("bc mode","steady state");  
    set("sweep type","single");  
    set("voltage",0.2);  # setting the voltage to 0.2 V  
    set("surface type","solid");  
    set("solid","cathode");

**Example 3**

The following script commands will create a steady state voltage boundary condition named cathode and apply a voltage sweep over a predefined set of voltages. The objects tree must already have a HEAT solver and a geometry named 'cathode' present.
    
    
    addvoltagebc;  
    
    set("name","cathode");  
    set("bc mode","steady state");  
    set("sweep type","value");  
    
    V = [0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6];  
    set("value table",V);  
    
    set("surface type","solid");  
    set("solid","cathode");

**Example 4**

The following script commands will set up a transient voltage boundary condition where the voltage is 0 V at t = 0, steps to 1 V between t = 1 us and 1.001 us (tslew = 1 ns), and remains at 1 V until t = 10 us. The boundary condition is assigned to a solid named cathode.
    
    
    addvoltagebc;  
    
    set("name","cathode_trans");  
    set("bc mode","transient");  
    
    tstep = [0, 1e-6, 1.001e-6, 10e-6];  
    V = [0, 0, 1, 1];  
    
    set("transient time steps",tstep);  
    set("transient value table",V);  
    set("surface type","solid");  
    set("solid","cathode");

**See Also**

[addconvectionbc](/hc/en-us/articles/360034404854-addconvectionbc), [addradiationbc](/hc/en-us/articles/360034924813-addradiationbc), [addthermalpowerbc](/hc/en-us/articles/360034404874-addthermalpowerbc), [addheatfluxbc](/hc/en-us/articles/360034404894-addheatfluxbc), [addvoltagebc](/hc/en-us/articles/360034404914-addvoltagebc)
