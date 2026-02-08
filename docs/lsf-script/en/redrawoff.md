# redrawoff

Disables automatic updating of the graphical viewports in the CAD or the schematic
layout drawing. This can greatly increase the speed of scripts that add large numbers of
objects.

| **Syntax** | **Description**                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| redrawoff; | Prevents redrawing of graphics. This function does not return any data. Cannot use this command in group setup scripts since redrawing is automatically turned off. |

**Example**

This example shows how to add objects more quickly by disabling the automatic redrawing.
The following FOR loop will run much faster when the automatic redrawing is disabled.

```
redrawoff;    # disable automatic redrawing
for (i=1:1000) { # add 1000 objects
 addcircle;
 set("radius",100e-9); 
 set("x",i*1e-8);
 if (i==500) {
  redraw;   # force one redraw half way through loop
 }
}
redrawon;     # enable automatic redrawing
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ redrawon ](./redrawon.md) , [ redraw ](./redraw.md) , [ redrawmode ](./redrawmode.md)
