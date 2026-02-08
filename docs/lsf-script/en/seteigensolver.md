# seteigensolver

Mode sources, mode expansion monitors, and ports in FDTD and MODE, and each individual
cell in EME have embedded eigensolvers. This script command makes it possible to set the
properties of that eigensolver without using the GUI.

Changing any values of the embedded eigensolver with this command will automatically
invalidate any existing mode data. This means that new updates based on overlap
calculations with previous modes will fail after using this command. Therefore please
call this command before making any calls to updatesourcemode or updatemodes.

| **Syntax**                        | **Description**                                                                                                                                      |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| ?seteigensolver;                  | Returns a list of the properties of the embedded eigensolver                                                                                         |
| seteigensolver("property",value); | This will set the eigensolver properties of the currently selected objects. Value can be a number or string. This function does not return any data. |

**Example**

1. Change the radius of curvature for a mode expansion calculation, and calculate the
   first 10 modes which can be subsequently used for mode expansion. Please open
   ring_resonator2.lms from the [ ring resonator example ](**%20to%20be%20defined%20**)
   using the varFDTD solver in MODE:

```
select("expansion");


seteigensolver("bent waveguide",true);
seteigensolver("bend radius",10e-6);
updatemodes(1:10);
```

2\. Change the number of trial modes for cell 1 in EME:

```
select("EME::Cells::cell_1");  
seteigensolver("number of trial modes",25);
```

Also see the examples in the [ addmodeexpansion ](./addmodeexpansion.md) , and
[ addport ](https://optics.ansys.com/hc/en-us/articles/360034924793-addport) script
functions.

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ addmode ](./addmode.md) , [ addmodeexpansion ](./addmodeexpansion.md) ,
[ addport ](https://optics.ansys.com/hc/en-us/articles/360034924793-addport) ,
[ clearsourcedata ](./clearsourcedata.md) , [ clearmodedata ](./clearmodedata.md) ,
[ clearportmodedata ](./clearportmodedata.md) , [ expand ](./expand.md) ,
[ geteigensolver ](./geteigensolver.md) , [ updatemodes ](./updatemodes.md) ,
[ updatesourcemode ](./updatesourcemode.md) , [ updateportmodes ](./updateportmodes.md)
