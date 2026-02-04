<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getglobalsource -->

# getglobalsource

**语法** | **描述**
---|---
getglobalsource; | 返回 a list of the global 光源 properties
getglobalsource("property"); | 返回 the 值 of the requested property.

**示例**

Set the global start 波长 to 400nm, then confirm 值 was set properly. 
    setglobalsource("波长 start",400e-9);
    ?getglobalsource("波长 start");
    result: 
    4e-007 

Set the global start 波长 to 400nm, then confirm 值 was set properly. 
    setglobalsource("波长 start",400e-9);
    ?getglobalsource("波长 start");
    result: 
    4e-007 

**另请参阅**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ get ](/hc/en-us/articles/360034928873-get) , [ setglobalmonitor ](/hc/en-us/articles/360034408494-setglobalmonitor) , [ getglobalmonitor ](/hc/en-us/articles/360034928933-getglobalmonitor) , [ setglobalsource ](/hc/en-us/articles/360034928813-setglobalsource)
