# feval

Evaluates a string as script file. This function is useful for running script files that
are not in your path and files with spaces in the name.

| **Syntax**       | **Description**                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------- |
| feval(filename); | Execute string containing the name of a script file. This function does not return any data. |

**Example**

Run the script file C:\\temp\\example.lsf.

```
feval("C:\temp\example.lsf");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ eval ](./eval.md) ,
[ str2num ](./str2num.md) , [ num2str ](./num2str.md) , [ lower ](./lower.md) ,
[ upper ](./upper.md) , [ toscript ](./toscript.md)
