# addmesh

Adds a mesh override region to the simulation environment. The mesh override region can
be used to control the size of the mesh in a certain region. In Finite Element IDE, a
CHARGE solver region must be present in the objects tree for this command to work.

| **Syntax**            | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addmesh;              | Adds a mesh override region to the simulation environment. In Finite Element IDE, this command adds an electrical mesh which applies only to the 'CHARGE' solver. This function does not return any data.                                                                                                                                                                                                                       |
| addmesh(struct_data); | Adds a mesh override region to the simulation environment. object and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. In Finite Element IDE, this command adds an electrical mesh which applies only to the 'CHARGE' solver. This function does not return any data. |

**Example**

The following script commands will add a mesh override region in FDTD, name it, set its
dimension, and set the mesh constraints. The mesh object will be set to restrict the
mesh in X direction only.

```
addmesh;
set("name","mesh_waveguide");
# set dimension
set("x",0);
set("x span",2e-6);
set("y",0);
set("y span",5e-6);
set("z",0);
set("z span",10e-6);
# enable in X direction and disable in Y,Z directions
set("override x mesh",1);
set("override y mesh",0);
set("override z mesh",0);
# restrict mesh by defining maximum step size
set("set maximum mesh step",1);
set("dx",5e-9);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md)
