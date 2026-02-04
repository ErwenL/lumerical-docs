<!--
Translation from English documentation
Original command: workspace
Translation date: 2026-02-04 22:50:32
-->

# workspace

返回 一个 list 的 all 该 currently defined variables 在 该 scripting workspace. 

**语法** |  **描述**  
---|---  
out = workspace;  |  返回 一个 字符串 该 lists all currently defined variables 在 该 workspace.  Use ?workspace; 到 print 此 到 该 screen.   
  
**示例**
    
    
    clear;
    my_data=4;
    result=矩阵(2,2);
    ?workspace;
    matrices:
     pi mu0 eps0 my_data result c

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ clear ](/hc/en-us/articles/360034929753-clear)
