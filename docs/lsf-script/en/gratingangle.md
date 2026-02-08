# gratingangle

Returns the angle vector corresponding to the values returned by grating, in degrees,
for 2D simulations. For 3D simulations, use gratingu1 and gratingu2.

If Bloch boundary conditions are used, the Bloch vector must be properly set for this
command to return the correct results. To make sure the Bloch vector is properly set,
turn on the "set based on source angle" option in the "Boundary conditions" tab of the
FDTD solver settings.

| **Syntax**                               | **Description**                     |
| ---------------------------------------- | ----------------------------------- |
| out = gratingangle( "monitorname", ...); | Same arguments as grating function. |

**Example**

This example plots the relative strength of the grating orders.

```
mname="T";          # monitor name
theta=gratingangle(mname);  # angle of each grating order
G=grating(mname);      # power to each order (fraction of transmitted power)
plot(theta,G,"theta (deg)","relative power","grating orders","plot points");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ grating ](./grating.md)
, [ gratingu1 ](./gratingu1.md) , [ gratingu2 ](./gratingu2.md)
