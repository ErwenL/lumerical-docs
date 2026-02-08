# addplane

# 

Adds a plane wave source to the simulation environment.

## For FDTD and MODE

| **Syntax**             | **Description**                                                                                                                                                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addplane;              | Adds a plane wave source to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addplane(struct_data); | Adds a plane wave source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add a plane wave source in the simulation environment
that will propagate in the negative z direction. The script will set the dimension (and
position) of the source and will define the frequency range.

```
addplane;
set("injection axis","z");
set("direction","backward");
set("x",0);
set("x span",2e-6);
set("y",0);
set("y span",5e-6);
set("z",3e-6);
set("wavelength start",0.3e-6);
set("wavelength stop",1.2e-6);
```

## For DGTD:

Adds a plane wave source to the 'DGTD' solver in Finite Element IDE. A DGTD solver
region must be present in the objects tree for this command to work.

| **Syntax** | **Description**                                                                        |
| ---------- | -------------------------------------------------------------------------------------- |
| addplane;  | Adds a plane wave source to the 'DGTD' solver. This function does not return any data. |

**Example 1**

The following script commands will add a plane wave source to the 'DGTD' solver already
present in the objects tree and print the name of all of its properties.

```
addplane;?set;
```

**Example 2**

The following script commands will add a plane wave source to the 'DGTD' solver, change
its name, and set up its properties. The script then sets the solid named "2D rectangle"
as the injection surface.

```
addplane; 
set("name","plane_wave");# set the propagation directionset("direction definition","axis");set("direction","backward");set("angle theta",30);set("angle phi",60);
# set the polarization angleset("polarization angle",90);
# set the injection surfaceset("surface type","solid");set("solid","2D rectangle");
```

### **See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ addplane ](./addplane.md) , [ addgaussian ](./addgaussian.md) ,
[ addtfsf ](./addtfsf.md) , [ adddgtdsolver ](./adddgtdsolver.md)
