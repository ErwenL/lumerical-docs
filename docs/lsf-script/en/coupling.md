# coupling

Returns the complex coupling coefficient between two modes. The power coupling can be
calculated with the overlap function, or by the following formula.

Power_Coupling = | coupling | 2

Reference: Allan W. Snyder and John D. Love, Optical Waveguide Theory. Chapman & Hall,
London, England, 1983.

See the overlap function for more details about overlap and coupling calculations.

## Note: coupling command is deprecated, consider using [ expand ](./expand.md)

| **Syntax**                    | **Description** |
| ----------------------------- | --------------- |
| out = coupling(mode2, mode1); |                 |

- mode2, mode1: the mode names
- out: the coupling coefficient

out = coupling(mode2, mode1, x, y); | Mode alignment can be adjusted before coupling is
calculated.

- x offset
- y offset

**Examples**

This example shows how to use the overlap command to calculate the overlap and power
coupling between two modes.

```
copydcard("mode1","test_mode1");  
copydcard("mode2","test_mode2");  

out = overlap("test_mode1","test_mode2");  

?out(1);  # overlap  
?out(2);  # power coupling  
?coupling("test_mode1","test_mode2"); # the complex coupling coefficient  
?abs(coupling("test_mode1","test_mode2"))^2; # same as out(2), the power coupling
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ copydcard ](./copydcard.md) , [ findmodes ](./findmodes.md) ,
[ coupling ](./coupling.md) , [ overlap ](./overlap.md) ,
[ bestoverlap ](./bestoverlap.md) , [ propagate ](./propagate.md) ,
[ expand ](./expand.md) , [ expand2 ](./expand2.md)
