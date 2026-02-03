# setlayer

Sets the properties of the specified layer of the selected layer builder object. There needs to be a layer builder object selected.

**Syntax** |  **Description**  
---|---  
setlayer("layer name", "property name", "property value"); |  Sets the properties of a specified layer of the selected layer builder object.  
  
**Example**
    
    
    setlayer("abc","thickness",0.5e-6);
    setlayer("abc","background material","Ag (Silver) - CRC");
    setlayer("abc","layer number", "(2:0 and 3:0) or 1:0"); # generate the patterns corresponding to layer 1:0 plus the overlap of layers 2:0 and 3:0.
    setlayer("abc","pattern material","Ag (Silver) - CRC");
    setlayer("abc","name","abc123"); # change the name of "abc" to "abc123".

Please refer [ this example ](/hc/en-us/articles/360034382394-Layer-builder) for more details.

**See Also**

[ addlayerbuilder ](/hc/en-us/articles/360034404714-addlayerbuilder) , [ getlayerlist ](/hc/en-us/articles/360034409134-getlayerlist) , [ setlayer ](/hc/en-us/articles/360034929453-setlayer) , [ loadgdsfile ](/hc/en-us/articles/360034929473-loadgdsfile) , [ addlayer ](/hc/en-us/articles/360034924693-addlayer) , [ getcelllist ](/hc/en-us/articles/360034929413-getcelllist) , [ getlayerlist ](/hc/en-us/articles/360034409134-getlayerlist)
