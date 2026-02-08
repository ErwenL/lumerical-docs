# addhtmaterialproperty

Adds a new thermal material property to the selected material model or the selected
solid alloy. A material model (in the 'materials' folder) or a solid alloy thermal
material property must be selected in the object tree for this script command to work. A
solid alloy may not be created as a component of a solid alloy. To add a thermal
material property from the electrothermal material database, see
[ addmaterialproperties ](./addmaterialproperties.md) . For details of thermal material
models, see
[ Electrical/Thermal Material Models ](https://optics.ansys.com/hc/en-us/articles/360034919093-Electrical-Thermal-Material-Models)
.

| **Syntax**                              | **Description**                                                                                                                                            |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addhtmaterialproperty("property_type"); | Adds a new thermal material property to the selected material model or the selected solid alloy. The "property_type" argument can be one of the following: |

- "Solid"
- "Solid Alloy"
- "Fluid"

This function does not return any data.

**Example**

The following script commands will add a new material to the objects tree in Finite
Element IDE, and assign thermal property of fluid to it.

```
addmodelmaterial;
addhtmaterialproperty("Fluid");
```

## NOTE: Once a material property is assigned to the material model the selection changes to the corresponding property. Therefore the material model must be re-selected before adding a new property to it.

NOTE: For a newly created alloy, when the first base material is added to the alloy, the
second base material will also be the same material as the first. For example, the
following lines will create a new alloy and assign the solid material "A" as both base
material 1 and base material 2 for the alloy:

```
addmodelmaterial;
set("name","test");
addhtmaterialproperty("Solid Alloy");
set("name","alloy");
addhtmaterialproperty("Solid");
set("name","A");  
```

______________________________________________________________________

**See Also**

[ addmodelmaterial ](./addmodelmaterial.md) ,
[ addmaterialproperties ](./addmaterialproperties.md) ,
[ addemmaterialproperty ](./addemmaterialproperty.md) ,
[ addctmaterialproperty ](./addctmaterialproperty.md)
