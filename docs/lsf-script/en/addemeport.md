# addemeport

Adds a [port](https://optics.ansys.com/hc/en-us/articles/360034396374) to an EME solver
region/object. The EME solver object must be set as the active solver for this command
to work.

| **Syntax**               | **Description**                                                                                                                                                                                                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addemeport;              | Add a port to the active EME solver region. This function does not return any data.                                                                                                                                                                                                                |
| addemeport(struct_data); | Adds a port to the active EME solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add a port to the EME solver region. The
setactivesolver command is first used to set the EME solver region as the active solver.

```
setactivesolver("EME");
addemeport;
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ setactivesolver ](./setactivesolver.md)
