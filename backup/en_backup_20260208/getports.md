# getports

Returns a list of ports available in an element. 

**Syntax** |  **Description**  
---|---  
out = getports("name")  |  Gets a list of available ports.   
out = getports("name", "type")  |  Gets a list of available ports with the type "type".   
  
**Parameter** |  **Type** |  **Description**  
---|---|---  
name  |  string  |  name of the element.   
type  |  string  |  type of the port. Available types:  "electrical"  "optical"  "digital"   
  
**Example**
    
    
    addelement("Optical Amplifier");
    ?getports("AMP_1", "optical");
    >input
    output

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834)
