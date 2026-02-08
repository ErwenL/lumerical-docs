# str2num

Converts a string into a floating point number. Use the format script command to change
the precision of the output.

| **Syntax**             | **Description**                |
| ---------------------- | ------------------------------ |
| out = str2num(string); | Converts string into a number. |

**Example**

Convert a string into a number.

```
?str2num("1+2");
3
```

Compare the output using almostequal .

```
?almostequal(str2num("1.5677"), 1.5677);
result: 
1  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ " ](./minus.md) ,
[ + ](./minus.md) , [ ? ](./minus.md) , [ endl ](./endl.md) , [ write ](./write.md) ,
[ format ](https://optics.ansys.com/hc/en-us/articles/360034931913-format) ,
[ findstring ](./findstring.md) , [ replace ](./replace.md) ,
[ replacestring ](./replacestring.md) , [ substring ](./substring.md) ,
[ lower ](./lower.md) , [ upper ](./upper.md) , [ toscript ](./toscript.md) ,
[ almostequal ](./almostequal.md)
