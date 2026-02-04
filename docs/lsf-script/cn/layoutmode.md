<!--
Translation from English documentation
Original command: layoutmode
Translation date: 2026-02-04 22:50:01
-->

# layoutmode

This 脚本 命令 可以 为 used 到 determine whether 该 仿真 文件 是 currently 在 LAYOUT mode 或 在 ANALYSIS mode. It 是 important 到 use 此 命令 到 check 该 status 的 该 project 文件 once it 是 opened 到 avoid running into 一个 error during 该 subsequent operations 如果 该 文件 是 not 在 该 desired mode. 

**语法** |  **描述**  
---|---  
?layoutmode;  |  返回 1 如果 在 LAYOUT mode (DESIGN mode 用于 INTERCONNECT), 和 0 如果 在 ANALYSIS mode.   
  
**示例**

The following 脚本 commands 将 first load 一个 project 文件 named "test.fsp". The aim 的 该 脚本 是 到 添加 一个 新的 rectangle 到 该 existing geometry. However, 如果 该 文件 是 在 ANALYSIS mode 那么 该 "addrect" 命令 将 创建 一个 error. To avoid 此, 该 脚本 命令 "layoutmode" 是 first used 到 determine 该 status 的 该 文件. Then 一个 "如果/否则" statement 是 used 到 添加 该 rectangle directly 如果 该 文件 是 already 在 LAYOUT mode 或 到 添加 该 rectangle after switching 到 LAYOUT mode first 如果 该 文件 是 在 ANALYSIS mode. 
    
    
    load("test.fsp");  
    status = layoutmode;  
    
    如果 (status == 1) {  
        addrect;  
    }  
    否则 {  
        switchtolayout;  
        addrect;  
    }

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ switchtolayout ](/hc/en-us/articles/360034923993-switchtolayout) , [ designmode ](/hc/en-us/articles/360034924053-designmode)
