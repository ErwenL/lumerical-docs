# setexpression

The script command sets the selected element's specified property to the mentioned expression.

**Syntax** |  **Description**  
---|---  
setexpression (name,p,expr); |  Set the property ‘p’ of element ‘name’ to an expression ‘expr’.  
  
**Example**

To set a label for the temperature ad "%Temp%" of a waveguide named "Straight Waveguide_1", use the following script
    
    
    setexpression("Straight Waveguide_1","temperature","%Temp%");

**See Also**

[autoarrange](/hc/en-us/articles/360034409034-autoarrange), [addproperty](/hc/en-us/articles/360034409074-addproperty), [setexpression](/hc/en-us/articles/360034409094-setexpression), [createcompound](/hc/en-us/articles/360034409054-createcompound)
