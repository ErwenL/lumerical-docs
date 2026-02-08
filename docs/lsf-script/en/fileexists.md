# fileexists

Checks if a file exists. The file extension (ie, .fsp, .lms, etc) must be specified. By
default, the entire path will be searched.

| **Syntax**                              | **Description**                                                    |
| --------------------------------------- | ------------------------------------------------------------------ |
| out = fileexists("filename");           | Returns 1 if the file exists Returns 0 if the file does not exist. |
| out = fileexists("c:\\temp\\file.txt"); | Search for a file not in the path                                  |

**Examples**

Checks if a file exists before opening it.

```
filename="simulation.fsp";
if (fileexists(filename)) {
 load(filename);
}
```

Load a simulation project file, if it exists. First check current directory, then check
up one directory.

```
filename="simulation.fsp";
if (fileexists(file)) {
 load(filename);
} else {
 file = "../"+file;
 if (fileexists(file)) {
  load(filename);
 } else {
  ?"File not found.";
 }
}
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ getpath ](./getpath.md)
, [ which ](./which.md) , [ pwd ](./pwd.md) , [ load ](./load.md) ,
[ loaddata ](./loaddata.md) , [ write ](./write.md) , [ readdata ](./readdata.md) ,
[ currentfilename ](./currentfilename.md) , [ rm ](./rm.md) , [ exist ](./exist.md)
