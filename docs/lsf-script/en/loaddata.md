# loaddata

Loads workspace variables or d-card data from a Lumerical data file (ldf) file. If any
current variables exist with the same names as those in the file, the current values
will be overwritten. This command will automatically detect if the .ldf file contains
d-card or script workspace variable data and load them into the d-card deck or script
workspace, respectively.

| **Syntax**            | **Description**                                                                                                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| loaddata("filename"); | Reads data script variables or d-card data from the specified file. This function does not return any data. Note: This function will check for the file in the current working directory. If the file to read from is in a different directory, either specify the full path or change the current working directory. |

**Examples**

Loads file called mydata.ldf . Then use the workspace and getdata commands to see what
workspace variables or d-cards have been created.

```
filename="mydata";
loaddata(filename);
?workspace;     # view workspace variables
?getdata;     # view d-cards (generally the complete set of data from a monitor)
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ savedata ](./savedata.md) , [ savedcard ](./savedcard.md) ,
[ workspace ](./workspace.md) , [ load ](./load.md) , [ fileexists ](./fileexists.md)
