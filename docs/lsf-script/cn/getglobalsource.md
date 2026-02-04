<!--
Translation from English documentation
Original command: getglobalsource
Translation date: 2026-02-04 22:50:00
-->

# getglobalsource

设置 global 监视器 属性. This 命令 将 返回 一个 error 在 分析 mode. 

**语法** |  **描述**  
---|---  
getglobalsource;  |  返回 一个 list 的 该 global 源 属性   
getglobalsource("属性");  |  返回 该 值 的 该 requested 属性.   
  
**示例**

设置 该 global start 波长 到 400nm, 那么 confirm 值 was 设置 properly. 
    
    
    setglobalsource("波长 start",400e-9);
    ?getglobalsource("波长 start");
    result: 
    4e-007 

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ 获取 ](/hc/en-us/articles/360034928873-获取) , [ setglobalmonitor ](/hc/en-us/articles/360034408494-setglobalmonitor) , [ getglobalmonitor ](/hc/en-us/articles/360034928933-getglobalmonitor) , [ setglobalsource ](/hc/en-us/articles/360034928813-setglobalsource)
