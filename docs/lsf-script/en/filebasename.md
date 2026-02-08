# filebasename

Gets the file basename from a string.

| **Syntax**                                     | **Description**                        |
| ---------------------------------------------- | -------------------------------------- |
| out = filebasename( "location/filename.ext" ); | Returns the file basename as a string. |

**Examples**

Isolates the file basename from the full filename.

```
?filebasename("C:\Users\myname\Documents\FDTD Files\test.fsp");
test
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ currentfilename ](./currentfilename.md) , [ getpath ](./getpath.md) ,
[ which ](./which.md) , [ pwd ](./pwd.md) , [ filedirectory ](./filedirectory.md) ,
[ fileextension ](./fileextension.md)
