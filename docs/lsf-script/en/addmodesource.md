# addmodesource

Adds a mode source to the 2.5D varFDTD simulation environment. The varFDTD solver object
must be set as the active solver for this command to work.

| **Syntax**                  | **Description**                                                                                                                                                                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addmodesource;              | Adds a mode source to the varFDTD solver region. This function does not return any data.                                                                                                                                                                                                               |
| addmodesource(struct_data); | Adds a mode source to the varFDTD solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will add a mode source to the varFDTD solver region in
MODE and select the injection axis.

```
addmodesource;
set("injection axis","x");
set("x",0);
set("y",0);
set("y span",5e-6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ addvarfdtd ](./addvarfdtd.md) , [ updatesourcemode ](./updatesourcemode.md)
