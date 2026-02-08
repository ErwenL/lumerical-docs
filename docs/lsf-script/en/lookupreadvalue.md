# lookupreadvalue

Finds the value from a file containing a lookup table of design and extracted
parameters.

| **Syntax**                                                     | **Description**                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = lookupreadvalue ("filename","table",design,"extracted"); | Find the value from a file containing a lookup table of design and extracted parameters. Parameter table is the name of the lookup table located inside the file, design is a cell containing multiple structures that define the design parameters to search, and extracted is the name of the parameter to be extracted. It will return the value is interpolated at the design parameters. |

**Example**

In order to load the coupling length index associated to a coupler gap:

```
#design cell containing design/layout parameters (input parameter to search)
#“gap” is the name of the property in the file
w_gap=3.5e-07;
design = cell(1);
design{1} = struct;
design{1}.name = "gap";
design{1}.value = w_gap;
#read coupling length from file (using design as input search “coupling_length”)
cl=lookupreadvalue( "coupler_map.ixml", "coupler_extracted", design, "coupling_length" );
?cl
7.18624026618721e-06
```

where “coupler_map.ixml” is a lookup table containing a map between coupler gap and
coupling length values:

```
<?xml version="1.0" encoding="UTF-8"?>
<lumerical_lookup_table version="1.0" name="coupler">
  <association>
    <design>
      <value name="gap" type="double">3.5e-07</value>
    </design>
    <extracted>
      <value name="coupling_length" type="double">7.18624026618721e-06</value>
    </extracted>
  </association>
</lumerical_lookup_table>
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ lookupopen ](./lookupopen.md) , [ lookupread ](./lookupread.md) ,
[ lookupwrite ](./lookupwrite.md) , [ lookupclose ](./lookupclose.md) ,
[ lookupreadtable ](./lookupreadtable.md) ,
[ lookupreadnportsparameter ](./lookupreadnportsparameter.md) ,
[ lookupappend ](./lookupappend.md) , [ insert ](./insert.md)
