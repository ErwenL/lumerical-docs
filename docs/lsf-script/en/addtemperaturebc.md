# addtemperaturebc

Adds a new temperature boundary condition to the HEAT or CHARGE solver
\[[Boundary Conditions (Thermal Simulation)](https://optics.ansys.com/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-)\].
A HEAT or CHARGE solver region must be present in the objects tree before this boundary
condition can be added. If both solvers are present then the intended solver's name must
be provided as an argument to the script command.

The temperature boundary condition can only be added to the CHARGE solver when the
solver's temperature dependency is set to 'coupled'.

| **Syntax**                       | **Description**                                                                                                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addtemperaturebc;                | Adds a temperature boundary condition to the HEAT or CHARGE solver (whichever is present in the objects tree). This function does not return any data.                          |
| addtemperaturebc("solver_name"); | Adds a temperature boundary condition to the desired solver defined by the argument "solver_name". The options are "HEAT" and "CHARGE". This function does not return any data. |

**Example 1**

The following script commands will add a temperature boundary condition to the solver
already present in the objects tree and print all available properties of the boundary
condition.

```
addtemperaturebc;  
?set;
```

**Example 2**

The following script commands will add a steady state temperature boundary condition to
the HEAT solver already present in the objects tree. It will then name the boundary
condition, assign it to the -z simulation boundary, and sweep the temperature from 300 K
to 400 K in 5 steps.

```
addtemperaturebc("HEAT");  

set("name","T_bottom");  
set("bc mode","steady state");  
set("sweep type","range");  
set("range start",300);  
set("range stop",400);  
set("range num points",5);  
set("surface type","simulation region");  
set("z min",1);
```

**Example 3**

The following script commands will set up a transient temperature boundary condition to
the HEAT solver where the temperature is 300 K at t = 0 which steps to 400 K between t =
1 us and 1.1 us (tslew = 0.1 us) and remains at 400 K until t = 10 us. The temperature
boundary condition is assigned to a surfaces with surface id = 15 and 20.

```
addtemperaturebc("HEAT");  

set("name","T_trans");  
set("bc mode","transient");  

tstep = [0, 1e-6, 1.1e-6, 10e-6];  
Temp = [300, 300, 400, 400];  

set("transient time steps",tstep);  
set("transient value table",Temp);  
set("surface type","surface");  
set("surfaces",[15, 20]);
```

**See Also**

[addconvectionbc](./addconvectionbc.md), [addradiationbc](./addradiationbc.md),
[addthermalpowerbc](./addthermalpowerbc.md), [addheatfluxbc](./addheatfluxbc.md),
[addthermalinsulatingbc](./addthermalinsulatingbc.md), [addvoltagebc](./addvoltagebc.md)
