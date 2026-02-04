<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getglobalmonitor -->

# getglobalmonitor

**语法** | **描述**
---|---
?getglobalmonitor; | 返回 a list of the global 监视器 properties
?getglobalmonitor("property"); | 返回 the 值 of the requested property.

**示例**

Set the global 数字 of monitored 频率 points to 11, then confirm 值 was set properly. 
    setglobalmonitor("频率 points",11);
    ?getglobalmonitor("频率 points");
    result: 
    11  

Set the global 数字 of monitored 频率 points to 11, then confirm 值 was set properly. 
    setglobalmonitor("频率 points",11);
    ?getglobalmonitor("频率 points");
    result: 
    11  

**另请参阅**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ get ](/hc/en-us/articles/360034928873-get) , [ setglobalmonitor ](/hc/en-us/articles/360034408494-setglobalmonitor) , [ setglobalsource ](/hc/en-us/articles/360034928813-setglobalsource) , [ getglobalsource ](/hc/en-us/articles/360034928953-getglobalsource)
