# ~

Is the logical NOT operator. If a value is 0, then NOT returns 1. For all other values,
NOT returns 0. NOT(A) is equivalent to A==0, where == is the comparison operator.

| **Syntax** | **Description**                   |
| ---------- | --------------------------------- |
| out = !a;  | applies logical NOT operator to a |
| out = ~a;  | applies logical NOT operator to a |

**Examples**

This example shows the usage of the "!" and "~" operator.

```
a=1;
?!a; #output of not operator
result: 
0 
a=0;
?~a; #output of not operator
result: 
1 
a=3;
?~a; #output of not operator
result: 
0 
if (!fileexists("filename.fsp")) { 
 save("filename.fsp");
} 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ == ](./minus.md) ,
[ != ](./minus.md) , , [ = ](./minus.md) , , , [ & ](./minus.md) , [ and ](./and.md) ,
[ | ](./minus.md) , [ or ](./or.md) , [ ! ](./minus.md) , [ ~ ](./minus.md)
