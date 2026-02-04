<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getvalue -->

# getvalue

**语法** | **描述**
---|---
value=getvalue("element", "parameter");  value=getvalue("element", "parameter", "type"); | Gets an internal 值 for an 元素's internal ‘参数’. Different from ‘set’ or ‘getnamed’, ‘getvalue’ can have direct access to internal 元素 parameters. ‘type’ allows for variations for a given ‘参数’.

**示例**

The following 示例 gets the "s 参数" from the 元素 "SPAR_1". 
    ?getvalue("SPAR_1", "s parameters");
    Cell 数组 with 3 元素

The following 示例 gets the "s 参数" from the 元素 "SPAR_1". 
    ?getvalue("SPAR_1", "s parameters");
    Cell 数组 with 3 元素

**另请参阅**

[ setvalue ](/hc/en-us/articles/360034927773-setvalue)
