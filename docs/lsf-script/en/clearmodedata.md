# clearmodedata

Clears mode data for a mode expansion monitor in layout mode. This is mainly useful to reduce file sizes when saving. 

**Syntax** |  **Description**  
---|---  
clearmodedata;  |  Clears mode data for the selected mode expansion monitor.   
  
**Example**

Clear mode data stored in mode expansion monitor. This will make the file much smaller, which can be convenient when emailing simulation files. 
    
    
    select("expansion");
    clearmodedata; 

**See Also**

[ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ asapload ](/hc/en-us/articles/360034931973-asapload) , [ asapexport ](/hc/en-us/articles/360034931953-asapexport) , [ clearsourcedata ](/hc/en-us/articles/360034929093-clearsourcedata) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver)
