# findstring

Returns the position of a given substring in a string.

| **Syntax**                 | **Description**                                                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| pos = findstring(s,s1);    | Returns the position of the first instance substring s1 in s. If s1 is not found in s, it returns -1.                                            |
| pos = findstring(s,s1,p0); | Returns the position of the first instance substring s1 in s, starting at position p0. If s1 is not found in s, starting from p0, it returns -1. |

**Example**

These are some examples of how to find a substring in a string.

```
?findstring("test12test34","test34");
result: 
7
?findstring("test12test34","test");
result: 
1
?findstring("test12test34","test",4);
result: 
7
?findstring("test12test34","test",8);
result: 
-1
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ length ](./length.md) ,
[ substring ](./substring.md) , [ replace ](./replace.md) ,
[ replacestring ](./replacestring.md) , [ str2num ](./str2num.md) ,
[ num2str ](./num2str.md) , [ splitstring ](./splitstring.md) , [ lower ](./lower.md) ,
[ upper ](./upper.md) , [ toscript ](./toscript.md)
