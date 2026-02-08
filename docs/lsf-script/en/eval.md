# eval

Executes a string containing Lumerical's scripting language.

| **Syntax**    | **Description**                                                                           |
| ------------- | ----------------------------------------------------------------------------------------- |
| eval(string); | Executes the Lumerical script commands in string. This function does not return any data. |

**Example**

Execute a string as a command.

```
eval("x=1+2;");
?x;
3
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ feval ](./feval.md) ,
[ str2num ](./str2num.md) , [ num2str ](./num2str.md) , [ lower ](./lower.md) ,
[ upper ](./upper.md) , [ toscript ](./toscript.md)
