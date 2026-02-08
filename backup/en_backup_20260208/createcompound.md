# createcompound

The script command creates a compound element with the currently selected elements. 

**Syntax** |  **Description**  
---|---  
createcompound;  |  Creates a compound element with the currently selected elements.   
  
**Example**

Suppose a "Straight Waveguide_1" and a "Waveguide Coupler_1_1" are added and connected in the schematic editor, using those scripts will create a compound 
    
    
    select("Straight Waveguide_1");
    select("Waveguide Coupler_1_1");
    createcompound;

with a default name "COMPOUND_1". 

**See Also**

[ autoarrange ](/hc/en-us/articles/360034409034-autoarrange) , [ addproperty ](/hc/en-us/articles/360034409074-addproperty) , [ setexpression ](/hc/en-us/articles/360034409094-setexpression)
