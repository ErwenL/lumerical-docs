<!--
Translation from English documentation
Original command: newproject
Translation date: 2026-02-04 22:50:14
-->

# newproject

创建 一个 新的 仿真 project 文件. If there 是 一个 existing project 文件 在 该 GUI, 该 old project 文件 将 not 为 saved. 

**语法** |  **描述**  
---|---  
newproject;  |  创建 一个 新的 layout 环境.  This 函数 does not 返回 any 数据.   
  
**示例**

创建 一个 新的 project 使用 该 newproject 命令. 
    
    
    newproject;

However, 用于 FDTD 和 MODE, users 可以 have more choices: 

For MODE, it 可以 have numerical variables: 

**语法** |  **描述**  
---|---  
newproject(option);  |  The options 是 

  1. use default 文件 和 材料 database as template 
  2. use current 文件 和 材料 database as template 
  3. open 一个 文件 browser 到 select 和 existing 文件 as 一个 template 

The default option 是 1.   
  
**示例**

创建 一个 新的 project 使用 该 newproject 命令. 
    
    
    newproject; 
    newproject(2); # open 一个 template 使用 current 文件 和 材料 database

For FDTD, 该 variables 可以 为 either numerical, 或 字符串: 

**语法** |  **描述**  
---|---  
newproject(option);  |  The options 可以 为 数字 或 字符串:  1 或 'default': use default 文件 和 材料 database as template  2 或 'RF': use default RF template  3 或 'current': use current 文件 和 材料 database as template  4 或 'existing': open 一个 文件 browser 到 select 和 existing 文件 as 一个 template  The default option 是 1. Since most 材料 数据 在 该 Material Database 是 用于 optical frequencies, open 一个 RF project 将 not modify 该 original 材料 数据 在 该 材料 database.   
  
**示例**

创建 一个 新的 project 使用 该 newproject 命令. 
    
    
    newproject; # open 一个 template 用于 optical 频率 仿真 
    newproject('RF');# open 一个 template 用于 RF 仿真 
    newproject(2); # open 一个 template 用于 RF 仿真

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 新的 ](/hc/en-us/articles/360034931493-新的) , [ exit ](/hc/en-us/articles/360034931613-exit)
