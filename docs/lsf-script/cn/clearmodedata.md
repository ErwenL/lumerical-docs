<!--
Translation from English documentation
Original command: clearmodedata
Translation date: 2026-02-04 22:49:48
-->

# clearmodedata

Clears mode 数据 用于 一个 mode expansion 监视器 在 layout mode. This 是 mainly useful 到 reduce 文件 sizes 当 保存. 

**语法** |  **描述**  
---|---  
clearmodedata;  |  Clears mode 数据 用于 该 选中的 mode expansion 监视器.   
  
**示例**

Clear mode 数据 stored 在 mode expansion 监视器. This 将 make 该 文件 much smaller, 该 可以 为 convenient 当 emailing 仿真 files. 
    
    
    select("expansion");
    clearmodedata; 

**参见**

[ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ asapload ](/hc/en-us/articles/360034931973-asapload) , [ asapexport ](/hc/en-us/articles/360034931953-asapexport) , [ clearsourcedata ](/hc/en-us/articles/360034929093-clearsourcedata) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver)
