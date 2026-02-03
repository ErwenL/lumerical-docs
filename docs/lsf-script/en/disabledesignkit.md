# disabledesignkit

Disables a design kit in the Design Kits folder. 

**Syntax** |  **Description**  
---|---  
disabledesignkit("name", ["version"]);  |  Disables a design kit that is already installed to the Design Kit folder with the version number "version". The "version" is optional, default is an empty string.   
  
**Example**
    
    
    #disables the design kit "LCML" with version v1.1 from the element library ‘Design kits’ folder
    disabledesignkit("LCML", "v1.1");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ removedesignkit ](/hc/en-us/articles/360034407494-removedesignkit) , [ reloaddesignkit ](/hc/en-us/articles/360034927653-reloaddesignkit) , [ loaddesignkit ](/hc/en-us/articles/360034927613-loaddesignkit) , [ enabledesignkit ](/hc/en-us/articles/360034927633-enabledesignkit) , [ installdesignkit ](/hc/en-us/articles/360034407534-installdesignkit) , [ uninstalldesignkit ](/hc/en-us/articles/360034407554-uninstalldesignkit)
