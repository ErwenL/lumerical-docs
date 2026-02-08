# addproperty

The script command adds a property to a compound or to a scripted element.

| **Syntax**                                                                                                                          | **Description**                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| addproperty(name, property=”new_property”, category=””, type=”Number”, from=0, to=0, kind=”FixedUnit”, unit=””, default_value = "") | Adds a new property to a Scripted element or a Compound element with the following options: |

- name: element name.
- property: property name.
- category: defines the folder when the property will be stored in the properties view
  window.
- type: defines the property type. Can be chosen from \["Number", "String", "Logical",
  "Matrix", "ComboChoice", "FileSave", "FileOpen"\], please refer to the details below.
- from, to: defines the range for a "Number" type of property.
- kind: defines the property kind. Can be chosen from \["Angle", "Area", "Bandwidth",
  "Bitrate", "Capacitance", "Current", "Density", "Dimensionless", "Dispersion",
  "DispersionSlope", "Distance", "DopingDensity", "Energy", "EngineeringScale",
  "FixedUnit", "Frequency", "Gain", "GainCoefficient", "Inductance", "InverseDistance",
  "InverseVolume", "Loss", "LossCoefficient", "ModeDispersion", "NonQuantity", "Power",
  "PowerSpectralDensity", "Resistance", "Temperature", "Time", "Velocity", "Voltage",
  "Volume", "WaveguideLoss"\]; for the unit of all the kinds, please refer to the
  details below.
- unit: defines the unit of the property.
- default_value: defines the default value of the property. Can be a matrix or a string.
  If no default value is provided, the minimum range value will be used to initialize
  the property.

type:

- Number, String, Logical
- Matrix: Syntax for property value [a11, a12, a13; a21 ,a22, a23]
- ComboChoice: Creates a property with options to choose from. Syntax for property
  value: 'choice_1;choice_2:choice_3'
- FileSave: Allows a user to save a file. Syntax for property value: string with file
  path.
- FileOpen: Allows a user to open a file. Syntax for property value: string with file
  path.

kind:

- Frequency, Distance, Loss, etc: 'Unit' options are updated accordingly.
- FixedUnit: 'Unit' can be chosen from pre-defined units or can be user defined.
- NonQuantity: 'Unit' is blank (unitless). Recommended for all types expect "Number".

**Example**

Add property “new_property” to an existing compound element ‘COMPOUND_1’

```
addproperty("COMPOUND_1");
```

Add property “width” to an existing compound element ‘COMPOUND_1’

```
addproperty("COMPOUND_1","width");
```

Add property “gain” to an existing compound element ‘COMPOUND_1’, place it on category
‘Standard’

```
addproperty("COMPOUND_1","gain","Standard");
```

Add “temperature” property to an existing compound element ‘COMPOUND_1’, place it on
‘Thermal’ category, set its type, range and unit.

```
addproperty("COMPOUND_1","temperature","Thermal","Number",0,100,"Temperature","C");
```

**See Also**

[Manipulating objects](../lsf-script-commands-alphabetical.md),
[autoarrange](https://support.lumerical.com/hc/en-us/articles/360034409034-autoarrange),
[setexpression](https://support.lumerical.com/hc/en-us/articles/360034409094-setexpression),
[createcompound](https://support.lumerical.com/hc/en-us/articles/360034409054-createcompound)
