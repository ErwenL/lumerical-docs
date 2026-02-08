# getnumber

Gets the number of objects that are selected. 

**Syntax** |  **Description**  
---|---  
out = getnumber;  |  Returns the number of objects that are selected;   
  
**Example**

Add 2 microns to the radius of all objects named "circle". 
    
    
    select("circle");
    for (i=1:getnumber) {
     rad=get("radius",i);
     set("radius",rad+2e-6,i);
    }

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ get ](/hc/en-us/articles/360034928873-get) , [ getnamed ](/hc/en-us/articles/360034408574-getnamed) , [ getnamednumber ](/hc/en-us/articles/360034408594-getnamednumber) , [ set ](/hc/en-us/articles/360034928773-set)
