# addemmaterialproperty

Adds a new optical material property to the selected material model. A material model
(in the 'materials' folder) must be selected in the object tree for this script command
to work. To add an optical material property from the optical material database, see
[ addmaterialproperties ](./addmaterialproperties.md) . For details of optical material
models, see
[ Optical Material Models ](https://optics.ansys.com/hc/en-us/articles/360034398454-Optical-Material-Models)
.

| **Syntax**                              | **Description**                                                                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| addemmaterialproperty("property_type"); | Adds a new optical material property to the selected material model. The "property_type" argument can be one of the following: |

- "Conductive"
- "Dielectric"
- "(n,k) Material"
- "Debye"
- "Plasma"
- "Lorentz"
- "Sampled Data 3D"

This function does not return any data.

**Example**

The following script commands will add a new material to the objects tree in Finite
Element IDE, and assign optical property of dielectric to it.

```
addmodelmaterial;
addemmaterialproperty("Dielectric");
```

## NOTE: Once a material property is assigned to the material model, the selection changes to the corresponding property. Therefore the material model must be re-selected before adding a new property to it.

**See Also**

[ addmodelmaterial ](./addmodelmaterial.md) ,
[ addmaterialproperties ](./addmaterialproperties.md) ,
[ addctmaterialproperty ](./addctmaterialproperty.md) ,
[ addhtmaterialproperty ](./addhtmaterialproperty.md)
