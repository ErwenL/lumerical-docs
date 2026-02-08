# replacestring

Replaces all the instances of a substring in a string with a new string.

| **Syntax**                     | **Description**                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------- |
| snew = replacestring(s,s1,s2); | Replaces all instances of s1 in s with s2. If s1 is not found, the original string s is returned. |

**Example**

Replace a substring in a string at all the places where it occurs.

```
?replacestring("test12test34","test","NEWTEST");
NEWTEST12NEWTEST34
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ length ](./length.md) ,
[ substring ](./substring.md) , [ findstring ](./findstring.md) ,
[ replace ](./replace.md) , [ str2num ](./str2num.md) , [ num2str ](./num2str.md) ,
[ splitstring ](./splitstring.md) , [ lower ](./lower.md) , [ upper ](./upper.md) ,
[ toscript ](./toscript.md)
