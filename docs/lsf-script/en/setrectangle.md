# setrectangle

Sets the width or height of an element rectangle.

| **Syntax**                    | **Description**                                            |
| ----------------------------- | ---------------------------------------------------------- |
| setrectangle ("element",w,h); | Sets the width (w) and height (h) of an element rectangle. |

**Example**

To set a waveguide element named "Straight Waveguide_1" with w=1um and h=0.5um, use the
following script

```
 setrectangle("Straight Waveguide_1",1e-6,0.5e-6) ;
```

**See Also**

[Manipulating objects](../lsf-script-commands-alphabetical.md),
[getrectangle](./getrectangle.md), [setposition](./setposition.md)
