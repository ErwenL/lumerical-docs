<!-- Translation completed: 2026-02-04 -->
<!-- Original command: workspace -->

# workspace

**语法** | **描述**
---|---
out = workspace; | 返回 a 字符串 that lists all currently defined variables in the workspace.  Use ?workspace; to print this to the screen.

**示例**

    clear;
    my_data=4;
    result=矩阵(2,2);
    ?workspace;
    matrices:
     pi mu0 eps0 my_data result c

    clear;
    my_data=4;
    result=矩阵(2,2);
    ?workspace;
    matrices:
     pi mu0 eps0 my_data result c

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ clear ](/hc/en-us/articles/360034929753-clear)
