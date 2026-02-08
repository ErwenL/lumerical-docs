# save

Saves a simulation project file. If the simulation has been run, the file will also
contain the simulation results, such as sweep and optimization data.

| **Syntax**      | **Description**                                                                         |
| --------------- | --------------------------------------------------------------------------------------- |
| save;           | Open a file browser to save the file. This function does not return any data.           |
| save(filename); | Save with the specified name to the current working directory. A path can be specified. |

**Examples**

Saves the current profile file

```
save("project_name"); # saves the file in the current working directory
save("C:\Downloads\project_name.fsp") # saves the file in a path specified
```

### **See Also**

[ load](./load.md), [ loaddata](./loaddata.md), [ savedata](./savedata.md),
[ savedcard](./savedcard.md)
