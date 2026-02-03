# geteigensolver

Mode sources, mode expansion monitors, and ports in FDTD and MODE, and each individual cell in EME have embedded eigensolvers. This script command makes it possible to get the properties of that eigensolver without using the GUI. 

**Syntax** |  **Description**  
---|---  
?geteigensolver;  |  Returns a list of the properties of the embedded eigensolver   
geteigensolver("property");  |  This will get the eigensolver properties of the currently selected objects. The returned value may be a number or a string, depending on the property.   
  
**Example**

Please open  ring_resonator2.lms  from the [ ring resonator example ](**%20to%20be%20defined%20**) and type in this command 
    
    
    select("expansion");
    ?geteigensolver;

It will give a list of the parameters of the eigensolver. Any parameters can be obtained, for example, type in 
    
    
    ?geteigensolver("bend radius");
    result: 
    1e-005  

Will give the bend radius of 10e-6 meter. 

Also see the examples in the [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) and [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) script functions. 

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ addmode ](/hc/en-us/articles/360034924353-addmode) , [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ clearsourcedata ](/hc/en-us/articles/360034929093-clearsourcedata) , [ clearmodedata ](/hc/en-us/articles/360034408774-clearmodedata) , [ clearportmodedata ](/hc/en-us/articles/360034409194-clearportmodedata) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ seteigensolver ](/hc/en-us/articles/360034929113-seteigensolver) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ updatemodes ](/hc/en-us/articles/360034929073-updatemodes) , [ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ updateportmodes ](/hc/en-us/articles/360034409174-updateportmodes)
