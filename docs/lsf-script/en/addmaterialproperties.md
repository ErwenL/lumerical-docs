# addmaterialproperties

Adds a (material) property to the selected material model. A material model (in the 'materials' folder) must be selected in the objects tree for this script command to work.

**Syntax** |  **Description**  
---|---  
addmaterialproperties("material_type","material_name"); |  Adds a (material) property to the selected material model in the objects tree in Finite Element IDE. The property comes from one of the material databases in Finite Element IDE. The "material_type" argument selects the type of material property to be added. The options are "CT" for electrical property, "HT" for thermal property, and "EM" for optical property. The "material_name" argument defines the name of the material in the appropriate material database whose properties will be imported. The function does not return any data.  
addmaterialproperties("material_type"); |  The "material_type" argument selects the type of material property to be added. The options are "CT" for electrical property, "HT" for thermal property, and "EM" for optical property. The function returns a list of available material names as a string.  
  
**Example**

The following script commands will add a new material to the objects tree in Finite Element IDE name it, and assign optical properties to it using a material model in the optical material database. The script will then add electrical and thermal properties to the same material using an appropriate material model in the electrical/thermal material database.
    
    
    addmodelmaterial;
    set("name","silicon");
    addmaterialproperties("EM","Si (Silicon) - Palik");  # importing from optical material database
    select("materials::silicon");
    addmaterialproperties("CT","Si (Silicon)");  # importing from electrical material database
    select("materials::silicon");
    addmaterialproperties("HT","Si (Silicon)");  # importing from thermal material database

NOTE:  Once a material property is assigned to the material model the selection changes to the corresponding property. Therefore the material model must be re-selected before adding a new property to it.  
---  
  
**See Also**

[ addmodelmaterial ](/hc/en-us/articles/360034404974-addmodelmaterial) , [ addemmaterialproperty ](/hc/en-us/articles/360034924953-addemmaterialproperty) , [ addctmaterialproperty ](/hc/en-us/articles/360034404994-addctmaterialproperty) , [ addhtmaterialproperty ](/hc/en-us/articles/360034924973-addhtmaterialproperty)
