# addpec

Adds a PEC (perfect electrical conductor) boundary condition to the DGTD or FEEM solver
in Finite Element IDE. A DGTD or FEEM solver region must be present in the objects tree
for this command to work. If both solvers are present then the intended solver's name
must be provided as an argument to the script command.

| **Syntax**             | **Description**                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addpec;                | Adds a PEC boundary condition to the DGTD or FEEM solver (whichever is present in the objects tree). This function does not return any data.                          |
| addpec("solver_name"); | Adds a PEC boundary condition to the desired solver defined by the argument "solver_name". The options are "DGTD" and "FEEM". This function does not return any data. |

**Example 1**

The following script commands will add a PEC boundary condition to the solver already
present in the objects tree and print all available properties of the boundary
condition.

```
addpec;
?set;
```

**Example 2**

The following script commands will add a PEC boundary condition to the DGTD solver, name
it, and assign it to the -x and +x boundaries of the simulation region.

```
addpec("DGTD"); 
set("name","PEC_x");
set("surface type","simulation region");
set("x min",1);
set("x max",1);
```

**See Also**

[ adddgtdsolver ](./adddgtdsolver.md) , [ addpml ](./addpec.md) ,
[ addpmc ](./addpmc.md) , [ addperiodic ](./addperiodic.md) ,
[ addabsorbing ](./addabsorbing.md)
