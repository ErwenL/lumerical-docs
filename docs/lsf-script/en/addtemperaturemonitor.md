# addtemperaturemonitor

Adds a temperature monitor to the Finite Element IDE simulation environment. The monitor
can only be added if the simulation environment already has a 'HEAT' or 'CHARGE' (or
both) solver present.

| **Syntax**                                         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addtemperaturemonitor;                             | Adds a temperature monitor to the simulation environment. This format of the command is only application when only one solver is present in the model tree. This function does not return any data. If multiple solvers are present then use the second format                                                                                                                                                                          |
| addtemperaturemonitor("solver_name");              | This format of the command will add a temperature monitor to the solver defined by the argument. The "solver name" will be either “CHARGE” or “HEAT.” For the CHARGE solver, the temperature monitor only works if the "temperature dependence" is set to "non-isothermal" or "coupled."                                                                                                                                                |
| addtemperaturemonitor(struct_data);                | Adds a temperature monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This format of the command is only application when only one solver is present in the model tree. This function does not return any data.                                                     |
| addtemperaturemonitor("solver_name", struct_data); | This format of the command will add a temperature monitor to the solver defined by the argument. The "solver name" will be either “CHARGE” or “HEAT.” Adds a temperature monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add a 2D y-normal temperature monitor to the CHARGE
solver region and set its dimension.

```
addtemperaturemonitor("CHARGE");  

set("name","Tmap");  
set("monitor type",6);  # 2D y-normal  
set("x",0);  
set("x span",2e-6);  
set("y",0);  
set("z",0);  
set("z span",10e-6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ addheatfluxmonitor ](./addheatfluxmonitor.md)
