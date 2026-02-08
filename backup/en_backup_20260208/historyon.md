# historyon

Enables taking snapshots (history) for the current object tree (non-INTERCONNECT)/schematic (INTERCONNECT) for undo redo functionality.

When running co-simulations in INTERCONNECT or multiple simulations each with lots of operations (for example, when using [lumopt](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API)), this option could will hinder performance.

**Syntax** |  **Description**  
---|---  
historyon; |  Enables taking snapshots (history) for the current object tree (non-INTERCONNECT)/schematic (INTERCONNECT) for undo redo functionality.  
  
**Example**
    
    
    historyon;

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [undo](/hc/en-us/articles/360034408894-undo), [redo](/hc/en-us/articles/360034929253-redo), [historyoff](/hc/en-us/articles/360034408914-historyoff)
