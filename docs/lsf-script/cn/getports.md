<!--
Translation from English documentation
Original command: getports
Translation date: 2026-02-04 22:50:00
-->

# getports

返回 一个 list 的 ports available 在 一个 元素. 

**语法** |  **描述**  
---|---  
out = getports("name")  |  获取 一个 list 的 available ports.   
out = getports("name", "类型")  |  获取 一个 list 的 available ports 使用 该 类型 "类型".   
  
**Parameter** |  **Type** |  **描述**  
---|---|---  
name  |  字符串  |  name 的 该 元素.   
类型  |  字符串  |  类型 的 该 端口. Available types:  "electrical"  "optical"  "digital"   
  
**示例**
    
    
    addelement("Optical Amplifier");
    ?getports("AMP_1", "optical");
    >input
    output

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834)
