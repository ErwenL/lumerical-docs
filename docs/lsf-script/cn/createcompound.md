<!-- Translation completed: 2026-02-04 -->
<!-- Original command: createcompound -->

# createcompound

**语法** | **描述**
---|---
createcompound; | Creates a compound 元素 with the currently selected 元素.

**示例**

Suppose a "Straight Waveguide_1" and a "Waveguide Coupler_1_1" are added and connected in the schematic editor, using those scripts will create a compound 
    select("Straight Waveguide_1");
    select("Waveguide Coupler_1_1");
    createcompound;
with a default name "COMPOUND_1". 

Suppose a "Straight Waveguide_1" and a "Waveguide Coupler_1_1" are added and connected in the schematic editor, using those scripts will create a compound 
    select("Straight Waveguide_1");
    select("Waveguide Coupler_1_1");
    createcompound;
with a default name "COMPOUND_1". 

**另请参阅**

[ autoarrange ](/hc/en-us/articles/360034409034-autoarrange) , [ addproperty ](/hc/en-us/articles/360034409074-addproperty) , [ setexpression ](/hc/en-us/articles/360034409094-setexpression)
