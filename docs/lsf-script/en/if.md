# if

Starts an if statement. The scripting language supports if statements in the following
forms:

| **Syntax**                                              | **Description**                  |
| ------------------------------------------------------- | -------------------------------- |
| if(x < 5) { y = x^2; }                                  | Simple if statement on one line. |
| if(x < 5) { y = x^2; }                                  | Multi-line if statement          |
| if(x < 5) { y = x^2; } else { y = x^3; }                | If else statement.               |
| if(x < 5) { if(x > 0) {y = x^2;} } else { y = x^3; }    | Nested if statement with else.   |
| if(x < 5) { y = x^2; } else if ( x > 10 ) { y = 2\*x; } | Chained if else if statement.    |

**Examples**

This example shows a simple if, OR, AND logical statement

```
clear;
a=1;
b=2;
d=3;
if((a==1)|(b==2)&(d==3)){
?"correct";}
else{
?"not correct";}
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ for ](./for.md) ,
[ List of commands ](../lsf-script-commands-alphabetical.md) , [ == ](./minus.md) ,
[ almostequal ](./almostequal.md) , [ ? ](./minus.md)
