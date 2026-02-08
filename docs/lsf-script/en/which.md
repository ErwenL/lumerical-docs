# which

Returns the full file pathname for the specified file.

This function can be helpful when you have added several directories to the Lumerical
path variable and you want to check which files are being accessed.

| **Syntax**               | **Description**                                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| out = which("filename"); | Returns the pathname of the file "filename" as a string. Use ?which("filename"); to display the result to the screen. |

**Examples**

Gets the full path and filename of the file results.txt.

```
file = "results.txt";    # set file name
write(file,"my data file"); # create file
?fullPath = which(file);   # get full name and path
 C:/Program Files/Lumerical/FDTD/scripts/results.txt
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ getpath ](./getpath.md)
, [ addpath ](./addpath.md) , [ pwd ](./pwd.md) ,
[ currentfilename ](./currentfilename.md) , [ fileexists ](./fileexists.md)
