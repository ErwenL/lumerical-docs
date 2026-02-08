# fileextension

Gets the file extension from a string.

| **Syntax**                        | **Description**                         |
| --------------------------------- | --------------------------------------- |
| out = fileextension( "name.ext"); | Returns the file extension as a string. |

**Examples**

Isolates the file extension from the full filename.

```
?fileextension("C:/Users/myname/Documents/FDTD/myfile.fsp");
fsp
```

Uses the following code to check with product you are using. This can be helpful if you
are trying to write scripts that will be shared between multiple products.

```
save("myfile");
if(fileextension(currentfilename)=="fsp") { ?"Using FDTD"; }
if(fileextension(currentfilename)=="lms") { ?"Using MODE"; }
if(fileextension(currentfilename)=="ldev") { ?"Using Finite Element IDE"; }
if(fileextension(currentfilename)=="icp") { ?"Using INTERCONNECT"; }
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ currentfilename ](./currentfilename.md) , [ getpath ](./getpath.md) ,
[ which ](./which.md) , [ pwd ](./pwd.md) , [ filedirectory ](./filedirectory.md) ,
[ filebasename ](./filebasename.md)
