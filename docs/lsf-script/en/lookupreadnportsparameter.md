# lookupreadnportsparameter

Returns an interpolated s-parameter cell for specific design parameters from an
[xml file containing a lookup table of design](https://optics.ansys.com/hc/en-us/articles/360034416634-INTERCONNECT-XML-lookup-tables-for-element-data).

The xml file should have a lookup table associating s-parameter data files with design
parameters. Each s-parameter file associated by the table should be compatible with the
[Optical N Port S-Parameter element](https://optics.ansys.com/hc/en-us/articles/360036107914-Optical-N-Port-S-Parameter-SPAR-INTERCONNECT-Element),
in the exact same format, and should not contain any header.

| **Syntax**                                                               | **Description**                                                                                |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| out = lookupreadnportsparameter ("filename","table",design,"extracted"); | Returns an interpolated s-parameter cell from an xml file containing a lookup table of design: |

- filename: Name of the xml file.
- table: Name of the lookup table located inside the xml file.
- design: Cell containing multiple structures defining the target design to extract.
- extracted: Name of the parameter inside the lookup table that holds names of the
  s-parameter data file for each design.

out = lookupreadnportsparameter ("filename","table",design,"extracted", opt); | Returns
an interpolated s-parameter cell from an xml file containing a lookup table of design
with interpolation options in the structure opt:

- filename: Name of the xml file.
- table: Name of the lookup table located inside the xml file.
- design: Cell containing multiple structures defining the target design to extract.
- extracted: Name of the parameter inside the lookup table that holds names of the
  s-parameter data file for each design.
- opt: Structure setting interpolation options. The structure fields are described in
  the table below.

The option structure has the following fields, the spelling of each field is
case-sensitive.

| **Field** | **Description**                                                         |
| --------- | ----------------------------------------------------------------------- |
| method    | The method used for interpolation. The following options are supported: |

- spline: Spline interpolation method, this is the default method.
- Geodesic: Geodesic interpolation method which ensures smooth transitions. When
  geodesic interpolation is selected, a similarity check is performed on original data
  points near the interpolated point used for the interpolation, if these points are not
  sufficiently similar, the data is coarse, and a warning is displayed. This method
  cannot be used for extrapolation.

passivity | Whether passivity is enforced for the s-parameter data prior to
interpolation. This field only affects results when “geodesic” is selected as the
interpolation method. When data is non-passive, a warning message is always displayed
for geodesic interpolation. The following options are supported:

- enforce: Ensures S-matrix is passive by making sure that the induced 2-norm of the
  s-parameters is less than 1. This is the default method.
- ignore: Ignores passivity of the s-parameters and interpolates as-is.

**Note** : For more information on how passivity is enforced, see this
[Knowledge Base](https://optics.ansys.com/hc/en-us/articles/360059772393-S-parameter-passive-workflow-guide#toc_4)
article.

**Example**

Loads the s-parameters of a coupler depending on user defined design parameters set up
target for interpolation:

```
filename = "coupler.ixml";
table = "coupler";
radius = 3e-06;
gap = 3e-07;
design = cell(2);
#design (input parameters)
design{1} = struct;
design{1}.name = "radius";
design{1}.value = radius;
design{2} = struct;
design{2}.name = "gap";
design{2}.value = gap; 
```

Interpolate parameters and load into S-parameter cell array using spline interpolation

```
?M = lookupreadnportsparameter( filename, table, design, "out_filename" ); 
```

Interpolate parameters and load into S-parameter cell array using geodesic
interpolation, ignoring passivity of the element

```
?M = lookupreadnportsparameter( filename, table, design, "out_filename", {"method":"geodesic","passivity":"ignore" ); 
```

Set parameters to element

```
addelement("Optical N Port S-Parameter");  
setvalue('SPAR_1','s parameters',M);
```

“coupler.ixml” is a lookup table containing a map between coupler parameters and
different s-parameters:

```
<?xml version="1.0" encoding="UTF-8"?>
<lumerical_lookup_table version="1.0" name = "coupler">
  <association>
    <design>
      <value name="radius" type="double">3e-06</value>
      <value name="gap" type="double">3e-07</value>
    </design>
    <extracted>
      <value name="out_filename" type="string">radius_3_gap_3.txt</value>
    </extracted>
  </association>
</lumerical_lookup_table>
```

For example “radius_3_gap_3.txt” file contains s-parameters for the ‘Optical N Port
S-Parameter’ element

```
("port 1","TE",1,"port 1",1,"transmission")
(3,3)
 2.262580000000e+014 1.034036580296e-002 -2.629253819969e+000
 2.275690000000e+014 9.716591457652e-003 -2.734774978072e+000
 2.288790000000e+014 6.884340821788e-003 -2.838683842048e+000
("port 1","TE",1,"port 2",1,"transmission")
(3,3)
 2.262580000000e+014 9.847090174703e-001 1.376105202083e-001
 2.275690000000e+014 9.959778891317e-001 1.450376288706e-001
 2.288790000000e+014 1.002869828593e+000 1.483183421805e-001
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ lookupopen ](./lookupopen.md) , [ lookupread ](./lookupread.md) ,
[ lookupwrite ](./lookupwrite.md) , [ lookupclose ](./lookupclose.md) ,
[ lookupreadtable ](./lookupreadtable.md) , [ lookupreadvalue ](./lookupreadvalue.md) ,
[ lookupappend ](./lookupappend.md) , [ insert ](./insert.md)
