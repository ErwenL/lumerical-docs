# exist

Returns a number based on type of the string used in the command.

| **Syntax** | **Description**                                                                                                                                                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| exist("x") | Returns 0 if there is no variable, operator, built-in function or script file (x.lsf) in the current script path 1 if x is a variable, example: x=5; ?exist(“x”); 2 if x is an operator or built in keyword, example: ?exist(“\*”) or ?exist(“for”); 3 if x is a script file in the current script path, called “x.lsf” |

**Examples**

The following simple examples show the usage of the exist command

```
a = 1:10;
?exist("a");
result: 
1  
?exist("farfield3d");
result: 
2 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ newproject ](./newproject.md) , [ fileexists ](./fileexists.md)
