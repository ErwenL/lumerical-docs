# sqrt

Calculates the square root of a number. Input can be complex or negative.

| **Syntax**     | **Description**                                                                                                                                                                                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = sqrt(x); | The square root of x. The square root is chosen so that real(sqrt(x))≥0 for any complex number x. The imaginary part, imag(sqrt(x)), can be positive or negative but if real(sqrt(x))=0 then imag(sqrt(x))≥0. |

**Example**

Calculate the square root of a number.

```
?sqrt(4);
result: 
2 
```

The square root function of z = x + iy in the complex plane has a branch cut at (-∞,0\],
as shown in the following example.

```
x = linspace(-1,1,100);
y = linspace(-1,1,100);
X = meshgridx(x,y);
Y = meshgridy(x,y);
image(x,y,real(sqrt(X+1i*Y)),"x", "y","Real part of sqrt(x+iy)");
image(x,y,imag(sqrt(X+1i*Y)),"x", "y","Imaginary part of sqrt(x+iy)");
```

|\
\---|---

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ ^ ](./minus.md)
