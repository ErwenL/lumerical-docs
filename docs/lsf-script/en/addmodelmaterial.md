# addmodelmaterial

Adds an empty material model to the 'materials' folder in the objects tree. Different properties (electrical, thermal, or optical) can then be assigned to the material. Once created the material can be assigned to any geometry and be used in simulations using the CHARGE, HEAT, or DGTD solvers.

**Syntax** |  **Description**  
---|---  
addmodelmaterial; |  Adds a new material to the 'materials' folder in the objects tree in Finite Element IDE. This function does not return any data.  
addmodelmaterial(struct_data); |  Adds a new material to the 'materials' and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a new material to the objects tree in Finite Element IDE, name it, and assign optical properties to it using a material model in the optical material database. The script will then add electrical and thermal properties to the same material using an appropriate material model in the electrical/thermal material database.
    
    
    addmodelmaterial;
    set("name","silicon");
    addmaterialproperties("EM","Si (Silicon) - Palik");
    select("materials::silicon");
    addmaterialproperties("CT","Si (Silicon)");
    select("materials::silicon");
    addmaterialproperties("HT","Si (Silicon)");

NOTE:  Once a material property is assigned to the material model the selection changes to the corresponding property. Therefore the material model must be re-selected before adding a new property to it.  
---  
  
**See Also**

[ addmaterialproperties ](/hc/en-us/articles/360034924933-addmaterialproperties)
