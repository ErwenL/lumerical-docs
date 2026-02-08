# addctmaterialproperty

Adds a new electrical material property to the selected material model or the selected
ternary alloy. A material model (in the 'materials' folder) or a ternary alloy
electrical material property must be selected in the object tree for this script command
to work. A ternary alloy may not be created as a component of a ternary alloy. To add an
electrical material property from the electrothermal material database, see
[ addmaterialproperties ](./addmaterialproperties.md) . For details of electrical
material models, see
[ Electrical/Thermal Material Models ](https://optics.ansys.com/hc/en-us/articles/360034919093-Electrical-Thermal-Material-Models)
or the page specifically about
[ Semiconductors](https://optics.ansys.com/hc/en-us/articles/360034919113-Semiconductors).

| **Syntax**                              | **Description**                                                                                                                                                 |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addctmaterialproperty("property_type"); | Adds a new electrical material property to the selected material model or the selected ternary alloy. The "property_type" argument can be one of the following: |

- "Semiconductor"
- "Insulator"
- "Conductor"
- "Ternary Alloy"

This function does not return any data.

**Example**

The following script commands will add a new material to the objects tree in Finite
Element IDE, and assign electrical property of conductor to it.

```
addmodelmaterial;
addctmaterialproperty("Conductor");
```

## NOTE: Once a material property is assigned to the material model the selection changes to the corresponding property. Therefore the material model must be re-selected before adding a new property to it.

NOTE: For a newly created alloy, when the first base material is added to the alloy, the
second base material will also be the same material as the first. For example, the
following lines will create a new alloy and assign the solid material "A" as both base
material 1 and base material 2 for the alloy:

```
addmodelmaterial;
set("name","test");
addctmaterialproperty("Ternary Alloy");
set("name","alloy");
addctmaterialproperty("Semiconductor");
set("name","A");  
```

______________________________________________________________________

**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [addmodelmaterial](./addmodelmaterial.md)
- [addmaterialproperties](./addmaterialproperties.md)
- [addemmaterialproperty](./addemmaterialproperty.md)
- [addhtmaterialproperty](./addhtmaterialproperty.md)
