# addperiodic

Adds a periodic (or Bloch) boundary condition to the 'DGTD' solver in Finite Element
IDE. A DGTD solver region must be present in the objects tree for this command to work.

| **Syntax**   | **Description**                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------ |
| addperiodic; | Adds a periodic boundary condition to the 'DGTD' solver. This function does not return any data. |

**Example 1**

The following script commands will add a periodic boundary condition to the 'DGTD'
solver already present in the objects tree and print all available properties of the
boundary condition.

```
addperiodic;
?set;
```

**Example 2**

The following script commands will add a periodic boundary condition in the x direction
of the 'DGTD' solver.

```
addperiodic; 
set("x periodic",1);
```

**See Also**

[ adddgtdsolver ](./adddgtdsolver.md) , [ addpml ](./addperiodic.md) ,
[ addpmc ](./addpmc.md) , [ addpec ](./addpec.md) , [ addabsorbing ](./addabsorbing.md)
