# framerate

Orbits the perspective view and returns the framerate. This can be useful for estimating
your graphics performance. If comparing the performance of two computers, be sure to use
exactly the same simulation file.

| **Syntax**                        | **Description**                                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| fr = framerate(num_frames, zoom); | num_frames - Number of frames to draw zoom - Zoom factor used in perspective view fr - number of frames / wall time required to complete orbit. |

**Example**

```
framerate(1000,2);
```

**See Also**

[Manipulating objects](../lsf-script-commands-alphabetical.md), [setview](./setview.md),
[getview](./getview.md), [orbit](./orbit.md)
