<!--
Translation from English documentation
Original command: getvalue
Translation date: 2026-02-04 22:50:00
-->

# getvalue

获取 一个 internal 值 用于 一个 元素's internal ‘s 参数’. 

**语法** |  **描述**  
---|---  
值=getvalue("元素", "参数");  值=getvalue("元素", "参数", "类型");  |  获取 一个 internal 值 用于 一个 元素's internal ‘参数’. Different 从 ‘设置’ 或 ‘getnamed’, ‘getvalue’ 可以 have direct access 到 internal 元素 参数. ‘类型’ allows 用于 variations 用于 一个 given ‘参数’.   
  
**示例**

The following example 获取 该 "s 参数" 从 该 元素 "SPAR_1". 
    
    
    ?getvalue("SPAR_1", "s 参数");
    Cell 数组 使用 3 elements

**参见**

[ setvalue ](/hc/en-us/articles/360034927773-setvalue)
