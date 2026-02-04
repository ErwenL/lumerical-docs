<!--
Translation from English documentation
Original command: createcompound
Translation date: 2026-02-04 22:49:48
-->

# createcompound

The 脚本 命令 创建 一个 compound 元素 使用 该 currently 选中的 elements. 

**语法** |  **描述**  
---|---  
createcompound;  |  创建 一个 compound 元素 使用 该 currently 选中的 elements.   
  
**示例**

Suppose 一个 "Straight Waveguide_1" 和 一个 "Waveguide Coupler_1_1" 是 added 和 connected 在 该 schematic editor, 使用 那些 scripts 将 创建 一个 compound 
    
    
    select("Straight Waveguide_1");
    select("Waveguide Coupler_1_1");
    createcompound;

使用 一个 default name "COMPOUND_1". 

**参见**

[ autoarrange ](/hc/en-us/articles/360034409034-autoarrange) , [ addproperty ](/hc/en-us/articles/360034409074-addproperty) , [ setexpression ](/hc/en-us/articles/360034409094-setexpression)
