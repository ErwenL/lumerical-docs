# substring

Extracts a substring from a string.

| **Syntax**                 | **Description**                                                                                                                                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| s1 = substring(s,pos);     | Returns a substring of s, starting at position pos to the end of s. The position pos can be 1 to length(s).                                                                                                |
| s1 = substring(s,pos,len); | Returns a substring of s, starting at position pos, with len characters. If len is -1 (or any value less than 0) it returns the substring at position pos to the end of s. The default value of len is -1. |

**Example**

The following example shows the different ways to extract a substring from a string.

```
?substring("hello",3);
llo
?substring("hello",3,2);
ll  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ length ](./length.md) ,
[ findstring ](./findstring.md) , [ replace ](./replace.md) ,
[ replacestring ](./replacestring.md) , [ str2num ](./str2num.md) ,
[ num2str ](./num2str.md) , [ splitstring ](./splitstring.md) , [ lower ](./lower.md) ,
[ upper ](./upper.md) , [ toscript ](./toscript.md)
