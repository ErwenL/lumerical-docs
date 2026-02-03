# addelectricalcontact

Adds a new electrical contact boundary condition to the CHARGE solver [ [ Boundary Conditions (Electrical Simulation) ](/hc/en-us/articles/360034918833-Boundary-Conditions-Electrical-Simulation-) ]. A CHARGE solver region must be present in the objects tree before an electrical contact boundary condition can be added.

**Syntax** |  **Description**  
---|---  
addelectricalcontact; |  Adds an electrical contact boundary condition to the CHARGE solver. This function does not return any data.  
  
**Example 1**

The following script commands will add an electrical contact boundary condition to the solver already present in the objects tree and print all available properties of the boundary condition.
    
    
    addelectricalcontact;
    ?set;

**Example 2**

The following script commands will create an electrical boundary condition with a fixed steady state voltage assigned to a solid named cathode. The objects tree must already have a CHARGE solver and a geometry named 'cathode' present.
    
    
    addelectricalcontact;
    set("name","cathode");
    set("bc mode","steady state");
    set("sweep type","single");
    set("voltage",0.2);  # setting the voltage to 0.2 V
    set("surface type","solid");
    set("solid","cathode");

**Example 3**

The following script commands will create a steady state electrical contact boundary condition named cathode and apply a voltage sweep over a predefined set of voltages. The objects tree must already have a CHARGE solver and a geometry named 'cathode' present.
    
    
    addelectricalcontact;
    set("name","cathode");
    set("bc mode","steady state");
    set("sweep type","value");
    V = [0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6];
    set("value table",V);
    set("surface type","solid");
    set("solid","cathode");

**Example 4**

The following script commands will set up a transient electrical contact boundary condition where the voltage is 0 V at t = 0, steps to 1 V between t = 10 ps and 100 ps (tslew = 90 ps), and remains at 1 V until t = 500 ps. The boundary condition is assigned to a solid named cathode.
    
    
    addelectricalcontact;
    set("name","cathode_trans");
    set("bc mode","transient");
    tstep = [0, 10e-12, 100e-12, 500e-12];
    V = [0, 0, 1, 1];
    set("transient voltage time steps",tstep);
    set("transient voltage table",V);
    set("surface type","solid");
    set("solid","cathode");

**See Also**

[ addsurfacerecombinationbc ](/hc/en-us/articles/360034404814-addsurfacerecombinationbc)
