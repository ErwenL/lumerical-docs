# gratingordercount

Returns the total number of supported grating numbers.

| **Syntax**                                                    | **Description**                                                                                 |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| out = gratingordercount( "monitorname", f, index, direction); | Returns the total number of supported grating orders. Same arguments as grating script command. |

**Example**

This example calculates power to each order only if grating orders are supported.

```
mname="T";       # monitor name
if(gratingordercount(mname) > 0){
N=gratingn(mname);   # grating order numbers
M=gratingm(mname);
u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
u2=gratingu2(mname);
G=grating(mname);   # power to each order (fraction of transmitted power)
}
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ grating ](./grating.md)
, [ gratingn ](./gratingn.md) , [ gratingm ](./gratingm.md)
