<!--
Translation from English documentation
Original command: getglobalmonitor
Translation date: 2026-02-04 22:50:00
-->

# getglobalmonitor

设置 global 监视器 属性. This 命令 将 返回 一个 error 在 分析 mode. 

**语法** |  **描述**  
---|---  
?getglobalmonitor;  |  返回 一个 list 的 该 global 监视器 属性   
?getglobalmonitor("属性");  |  返回 该 值 的 该 requested 属性.   
  
**示例**

设置 该 global 数字 的 monitored 频率 points 到 11, 那么 confirm 值 was 设置 properly. 
    
    
    setglobalmonitor("频率 points",11);
    ?getglobalmonitor("频率 points");
    result: 
    11  

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ 获取 ](/hc/en-us/articles/360034928873-获取) , [ setglobalmonitor ](/hc/en-us/articles/360034408494-setglobalmonitor) , [ setglobalsource ](/hc/en-us/articles/360034928813-setglobalsource) , [ getglobalsource ](/hc/en-us/articles/360034928953-getglobalsource)
