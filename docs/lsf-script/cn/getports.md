<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getports -->

# getports

**语法** | **描述**
---|---
out = getports("name") | Gets a list of available ports.
out = getports("name", "type") | Gets a list of available ports with the type "type".
name | 字符串
type | 字符串

**示例**

    addelement("Optical Amplifier");
    ?getports("AMP_1", "optical");
    >输入
    输出

    addelement("Optical Amplifier");
    ?getports("AMP_1", "optical");
    >输入
    输出

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834)
