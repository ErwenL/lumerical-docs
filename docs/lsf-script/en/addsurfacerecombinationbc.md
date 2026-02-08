# addsurfacerecombinationbc

Adds a new surface recombination boundary condition to the CHARGE solver
\[[Boundary Conditions (Electrical Simulation)](https://optics.ansys.com/hc/en-us/articles/360034918833-Boundary-Conditions-Electrical-Simulation-)\].
A CHARGE solver region must be present in the objects tree before a surface
recombination boundary condition can be added.

| **Syntax**                 | **Description**                                                                                                   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| addsurfacerecombinationbc; | Adds a new surface recombination boundary condition to the CHARGE solver. This function does not return any data. |

**Example 1**

The following script commands will add a surface recombination boundary condition to the
CHARGE solver (already present in the objects tree) and print all available properties
of the boundary condition.

```
addsurfacerecombinationbc;  
?set;
```

**Example 2**

The following script commands will add a surface recombination boundary condition to the
existing CHARGE solver and assign it to the interface (surfaces) between silicon and
silicon dioxide. It will set the surface recombination velocity of electrons and holes
to 100 cm/sec.

```
addsurfacerecombinationbc;  

set("name","Si_SiO2");  
set("surface type","material:material");  
set("material 1","Si (Silicon)");  
set("material 2","SiO2 (Glass) - Sze");  
set("electron velocity",100e-2);   # m/sec  
set("hole velocity",100e-2);   # m/sec  
set("apply to majority carriers",1);
```

The "apply to majority carriers" option should be enabled when modeling surface
recombination at semiconductor-oxide or semiconductor-semiconductor interfaces.

## NOTE: The 'materials' folder in the objects tree must already contain the materials used in the script commands to set up the boundary condition.

**Example 3**

The following script commands will add a surface recombination boundary condition to the
interface (surfaces) between silicon and aluminum. It will set the surface recombination
velocity of electrons and holes to 1e7 cm/sec.

```
addsurfacerecombinationbc;  

set("name","Si_Al");  
set("surface type","material:material");  
set("material 1","Si (Silicon)");  
set("material 2","Al (Aluminium) - CRC");  
set("electron velocity",1e5);   # m/sec  
set("hole velocity",1e5);   # m/sec  
set("apply to majority carriers",0);
```

The "apply to majority carriers" option should be disabled when modeling surface
recombination at semiconductor-metal interfaces.

**See Also**

[addelectricalcontact](./addelectricalcontact.md),
[addmodelmaterial](./addmodelmaterial.md)
