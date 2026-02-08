# redraw

Forces the graphical viewports of the CAD or the schematic layout drawing to update. The
viewports update automatically by default, so this command is only required after using
the redrawoff command.

| **Syntax** | **Description**                                           |
| ---------- | --------------------------------------------------------- |
| redraw;    | Redraws graphics. This function does not return any data. |

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
[ redrawon ](./redrawon.md) , [ redrawoff ](./redrawoff.md) ,
[ redrawmode ](./redrawmode.md)
