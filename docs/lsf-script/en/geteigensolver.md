# geteigensolver

Mode sources, mode expansion monitors, and ports in FDTD and MODE, and each individual
cell in EME have embedded eigensolvers. This script command makes it possible to get the
properties of that eigensolver without using the GUI.

| **Syntax**                  | **Description**                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ?geteigensolver;            | Returns a list of the properties of the embedded eigensolver                                                                                           |
| geteigensolver("property"); | This will get the eigensolver properties of the currently selected objects. The returned value may be a number or a string, depending on the property. |

**Example**

Please open ring_resonator2.lms from the
[ ring resonator example ](**%20to%20be%20defined%20**) and type in this command

```
select("expansion");
?geteigensolver;
```

It will give a list of the parameters of the eigensolver. Any parameters can be
obtained, for example, type in

```
?geteigensolver("bend radius");
result: 
1e-005  
```

Will give the bend radius of 10e-6 meter.

Also see the examples in the [ seteigensolver ](./seteigensolver.md) and
[ addmodeexpansion ](./addmodeexpansion.md) script functions.

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ addmode ](./addmode.md) , [ addmodeexpansion ](./addmodeexpansion.md) ,
[ addport ](https://optics.ansys.com/hc/en-us/articles/360034924793-addport) ,
[ clearsourcedata ](./clearsourcedata.md) , [ clearmodedata ](./clearmodedata.md) ,
[ clearportmodedata ](./clearportmodedata.md) , [ getresult ](./getresult.md) ,
[ seteigensolver ](./seteigensolver.md) , [ geteigensolver ](./geteigensolver.md) ,
[ updatemodes ](./updatemodes.md) , [ updatesourcemode ](./updatesourcemode.md) ,
[ updateportmodes ](./updateportmodes.md)
