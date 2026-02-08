# load

Loads a simulation project file. If the simulation has been run, the file will also
contain the simulation results.

| **Syntax**      | **Description**                                                    |
| --------------- | ------------------------------------------------------------------ |
| load(filename); | Loads the simulation file. This function does not return any data. |

**Examples**

Loads a simulation project file.

```
filename="simulation.fsp";
load(filename); # load the file in the current working directory
load("C:\Downloads\project_name.fsp") # load the file in a path specified
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ loaddata ](./loaddata.md) , [ save ](./save.md) , [ savedata ](./savedata.md) ,
[ savedcard ](./savedcard.md) , [ fileexists ](./fileexists.md) , [ dir ](./dir.md)
