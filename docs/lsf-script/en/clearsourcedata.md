# clearsourcedata

Clears source data for an imported source, or the selected mode for a mode source. 

**Syntax** |  **Description**  
---|---  
clearsourcedata;  |  Clears source data for the selected source.   
  
**Example**

Clear source data from an imported source. This will make the file much smaller, which can be convenient when emailing simulation files. 
    
    
    select("source3");
    clearsourcedata; 

**See Also**

[ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ asapimport ](/hc/en-us/articles/360034411274-asapimport) , [ asapload ](/hc/en-us/articles/360034931973-asapload) , [ asapexport ](/hc/en-us/articles/360034931953-asapexport) , [ clearmodedata ](/hc/en-us/articles/360034408774-clearmodedata) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver)
