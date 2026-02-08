# addthermalpowerbc

Adds a new thermal power boundary condition to the HEAT or CHARGE solver
\[[Boundary Conditions (Thermal Simulation)](https://optics.ansys.com/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-)\].
A HEAT or CHARGE solver region must be present in the objects tree before this boundary
condition can be added. If both solvers are present then the intended solver's name must
be provided as an argument to the script command.

The thermal power boundary condition can only be added to the CHARGE solver when the
solver's temperature dependency is set to 'coupled'.

| **Syntax**                        | **Description**                                                                                                                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addthermalpowerbc;                | Adds a thermal power boundary condition to the HEAT or CHARGE solver (whichever is present in the objects tree). This function does not return any data.                          |
| addthermalpowerbc("solver_name"); | Adds a thermal power boundary condition to the desired solver defined by the argument "solver_name". The options are "HEAT" and "CHARGE". This function does not return any data. |

**Example 1**

The following script commands will add a thermal power boundary condition to the solver
already present in the objects tree and print all available properties of the boundary
condition.

```
addthermalpowerbc;  
?set;
```

**Example 2**

The following script commands will add a steady state thermal power boundary condition
to the HEAT solver already present in the objects tree. It will then name the boundary
condition, assign it to the solid named 'heater', and sweep the power from 1 mW to 10 mW
in 5 steps.

```
addthermalpowerbc("HEAT");  

set("name","P_in");  
set("bc mode","steady state");  
set("sweep type","range");  
set("range start",1e-3);  
set("range stop",10e-3);  
set("range num points",5);  
set("surface type","solid");  
set("solid","heater");
```

**Example 3**

The following script commands will set up a transient thermal power boundary condition
to the HEAT solver where the power applied to the solid 'heater' is set to 0 W at t = 0.
The power input then steps from 0 W to 1 mW between t = 1 us to t = 1.1 us (tslew = 0.1
us). The power input is then kept at 1 mW until 10 us.

```
addthermalpowerbc("HEAT");  

set("name","P_heater");  
set("bc mode","transient");  

tstep = [0, 1e-6, 1.1e-6, 10e-6];  
Pin = [0, 0, 1e-3, 1e-3];  

set("transient time steps",tstep);  
set("transient value table",Pin);  
set("surface type","solid");  
set("solid","heater");
```

**See Also**

[addtemperaturebc](./addthermalpowerbc.md), [addconvectionbc](./addconvectionbc.md),
[addradiationbc](./addradiationbc.md), [addheatfluxbc](./addheatfluxbc.md),
[addthermalinsulatingbc](./addthermalinsulatingbc.md), [addvoltagebc](./addvoltagebc.md)
