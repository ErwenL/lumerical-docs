# historyon

Enables taking snapshots (history) for the current object tree
(non-INTERCONNECT)/schematic (INTERCONNECT) for undo redo functionality.

When running co-simulations in INTERCONNECT or multiple simulations each with lots of
operations (for example, when using
[lumopt](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API)),
this option could will hinder performance.

| **Syntax** | **Description**                                                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| historyon; | Enables taking snapshots (history) for the current object tree (non-INTERCONNECT)/schematic (INTERCONNECT) for undo redo functionality. |

**Example**

```
historyon;
```

**See Also**

[Manipulating objects](../lsf-script-commands-alphabetical.md), [undo](./undo.md),
[redo](./redo.md), [historyoff](./historyoff.md)
