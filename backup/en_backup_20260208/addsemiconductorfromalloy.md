# addsemiconductorfromalloy

Converts an Alloy material to a Semiconductor material at a fixed mole fraction and adds its electrothermal material properties to the selected material model in the object tree.

The alloy material parameters are obtained from the electrothermal material database, and the conversion is done by interpolating material properties from base materials at a given alloy mole fraction.

To use this command, first add an empty material model with [addmaterialmodel](https://optics.ansys.com/hc/en-us/articles/360034404974-addmodelmaterial-Script-command).

For further details of electrothermal material models, see [Electrical/Thermal Material Models](https://optics.ansys.com/hc/en-us/articles/360034919093-Electrical-Thermal-material-models-in-CHARGE-HEAT-and-MQW) and the page about [Semiconductors](https://optics.ansys.com/hc/en-us/articles/360034919113-Semiconductor-Material-Model-Properties). For further information on alloy materials, see the Knowledge Base page about [Alloy Material Model Properties](https://optics.ansys.com/hc/en-us/articles/360034398494-Alloy-material-model-properties).

**Syntax** |  **Description**  
---|---  
addsemiconductorfromalloy (name,x); |  Converts a Ternary Alloy material to a Semiconductor material and adds its electrothermal material properties to the selected material model in the object tree:

  * name: A ternary alloy material name in the electrothermal material database.
  * x: Alloy mole fraction.

This function does not return any data.  
addsemiconductorfromalloy (name,x,y);  |  This syntax is identical to above, but for a quaternary alloy. Converts a Quaternary Alloy material to a Semiconductor material and adds its electrothermal material properties to the selected material model in the object tree:

  * name: A quaternary alloy material name in the electrothermal material database.
  * x,y: Alloy mole fractions.

This function does not return any data.  
  
**Example**
    
    
    #Add a ternary alloy to the simulation as Semiconductor material type  
    addmodelmaterial;  
      
    set("name","AlGaAs");  
    x = 0.2; #The alloy composition is Al(x)Ga(1-x)As per convention in the database  
      
    addsemiconductorfromalloy("AlGaAs (Aluminium Gallium Arsenide)",x);  
      
    #Add quaternary alloy to the simulation as Semiconductor material type  
    addmodelmaterial;  
      
    set("name","AlGaInAs");  
    x = 0.1; #Al(x)Ga(y)In(1-x-y)As  
    y = 0.2;  
    addsemiconductorfromalloy("AlGaInAs",x,y);
