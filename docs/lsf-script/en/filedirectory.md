# filedirectory

Gets the file directory from a string.

| **Syntax**                                      | **Description**                         |
| ----------------------------------------------- | --------------------------------------- |
| out = filedirectory( "location/filename.ext" ); | Returns the file directory as a string. |

**Examples**

Isolates the file directory from the full filename.

```
?filedirectory("C:\Users\myname\Documents\FDTD Files\test.fsp");
C:/Users/myname/Documents/FDTD Files
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ currentfilename ](./currentfilename.md) , [ getpath ](./getpath.md) ,
[ which ](./which.md) , [ pwd ](./pwd.md) , [ fileextension ](./fileextension.md) ,
[ filebasename ](./filebasename.md)
