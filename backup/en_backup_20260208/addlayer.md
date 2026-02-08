# addlayer

Adds a layer to the layer builder object. The command only works if there is a layer builder object and is selected.

**Syntax** |  **Description**  
---|---  
addlayer; |  Adds a layer to the selected layer builder object. The name of the layer is set to "default name". This function does not return any data.  
addlayer("name"); |  Adds a layer named "name"  
  
**Example**

The following script commands will create a layer builder object and add two layers to it.
    
    
    addlayerbuilder;
    # Layer 1 = 100 nm layer of silver
    addlayer("layer_1");
    setlayer("layer_1","thickness",100e-9);
    setlayer("layer_1","material","Ag (Silver) - CRC");
    # Layer 2 = 500 nm layer of silicon
    addlayer("layer_2");
    setlayer("layer_2","thickness",500e-9);
    setlayer("layer_2","material","Si (Silicon)");

**See Also**

[ addlayerbuilder ](/hc/en-us/articles/360034404714-addlayerbuilder) , [ getlayerlist ](/hc/en-us/articles/360034409134-getlayerlist) , [ setlayer ](/hc/en-us/articles/360034929453-setlayer) , [ loadgdsfile ](/hc/en-us/articles/360034929473-loadgdsfile) , [ getcelllist ](/hc/en-us/articles/360034929413-getcelllist) , [ getlayerlist ](/hc/en-us/articles/360034409134-getlayerlist) , [ setlayer ](/hc/en-us/articles/360034929453-setlayer)
