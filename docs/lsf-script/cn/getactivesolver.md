<!--
Translation from English documentation
Original command: getactivesolver
Translation date: 2026-02-04 22:49:59
-->

# getactivesolver

获取 该 active 求解器. This could 为 该 FDE, varFDTD, 或 EME solvers 在 MODE. 

**语法** |  **描述**  
---|---  
?getactivesolver;  |  List 该 active 求解器.   
  
**示例**

When "EME" 求解器 是 already added, 该 following 脚本 将 give 该 result: 
    
    
    setactivesolver("EME");
    ?getactivesolver;
    EME

**参见**

[ setactivesolver ](/hc/en-us/articles/360034409014-setactivesolver)
