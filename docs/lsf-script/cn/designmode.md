<!--
Translation from English documentation
Original command: designmode
Translation date: 2026-02-04 22:49:48
-->

# designmode

In INTERCONNECT, 此 脚本 命令 可以 为 used 到 determine whether 该 仿真 文件 是 currently 在 DESIGN mode 或 在 ANALYSIS mode. It 是 important 到 use 此 命令 到 check 该 status 的 该 project 文件 once it 是 opened 到 avoid running into 一个 error during 该 subsequent operations 如果 该 文件 是 not 在 该 desired mode. 

**语法** |  **描述**  
---|---  
?designmode;  |  返回 1 如果 在 DESIGN mode, 和 0 如果 在 ANALYSIS mode.   
  
**示例**

The following 脚本 commands 将 first load 一个 project 文件 named "test.icp". The aim 的 该 脚本 是 到 添加 一个 新的 optical oscilloscope 到 该 existing circuit. However, 如果 该 文件 是 在 ANALYSIS mode 那么 该 "addelement" 命令 将 创建 一个 error. To avoid 此, 该 脚本 命令 "designmode" 是 first used 到 determine 该 status 的 该 文件. Then 一个 "如果/否则" statement 是 used 到 添加 该 元素 directly 如果 该 文件 是 already 在 DESIGN mode 或 到 添加 该 元素 after switching 到 DESIGN mode first 如果 该 文件 是 在 ANALYSIS mode. 
    
    
    load("test.icp");
    status = designmode;
    如果 (status == 1) {
        addelement("Optical Oscilloscope");
    }
    否则 {
        switchtodesign;
        addelement("Optical Oscilloscope");
    }

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ switchtolayout ](/hc/en-us/articles/360034923993-switchtolayout) , [ layoutmode ](/hc/en-us/articles/360034924033-layoutmode) , [ switchtodesign ](/hc/en-us/articles/360034924013-switchtodesign)
