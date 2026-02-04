<!--
Translation from English documentation
Original command: getresultdata
Translation date: 2026-02-04 22:50:00
-->

# getresultdata

获取 results 从 一个 analyzer. This differs 从 该 "getresult" 函数 在 该 该 results 是 returned as matrices, not [Datasets](/hc/en-us/articles/360034409554-Datasets).

**语法** |  **描述**  
---|---  
?getresultdata; |  返回 该 names 的 all elements 在 该 current 仿真 该 contain results.  
?getresultdata("analyzer"); |  返回 all available results 用于 "analyzer".   
out = getresultdata("analyzer", "result"); |  返回 该 result "result" 用于 "analyzer".  
  
**参见**

[setresult](/hc/en-us/articles/360034407694-setresult), [getresult](/hc/en-us/articles/360034409854-getresult)
