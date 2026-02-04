<!--
Translation from English documentation
Original command: clearsourcedata
Translation date: 2026-02-04 22:49:48
-->

# clearsourcedata

Clears 源 数据 用于 一个 imported 源, 或 该 选中的 mode 用于 一个 mode 源. 

**语法** |  **描述**  
---|---  
clearsourcedata;  |  Clears 源 数据 用于 该 选中的 源.   
  
**示例**

Clear 源 数据 从 一个 imported 源. This 将 make 该 文件 much smaller, 该 可以 为 convenient 当 emailing 仿真 files. 
    
    
    select("source3");
    clearsourcedata; 

**参见**

[ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ asapload ](/hc/en-us/articles/360034931973-asapload) , [ asapexport ](/hc/en-us/articles/360034931953-asapexport) , [ clearmodedata ](/hc/en-us/articles/360034408774-clearmodedata) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver)
