# addemeindex

Adds an [index monitor](https://optics.ansys.com/hc/en-us/articles/360034396434) that
can be used to return the spatial refractive index when using an EME solver region. The
EME solver object must be set as the active solver for this command to work.

| **Syntax**                | **Description**                                                                                                                                                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addemeindex;              | Add an index monitor when using an EME solver region. This function does not return any data.                                                                                                                                                                                    |
| addemeindex(struct_data); | Adds an EME index monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add an index monitor to the EME solver region. The
setactivesolver command is first used to set the EME solver region as the active solver.

```
setactivesolver("EME");
addemeindex;
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ setactivesolver ](./setactivesolver.md)
