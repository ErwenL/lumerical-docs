# lookupappend

Inserts a new association into an existing lookup table.

| **Syntax**                                              | **Description**                                          |
| ------------------------------------------------------- | -------------------------------------------------------- |
| lookupappend("filename", "table", design, "extracted"); | Inserts a new association into an existing lookup table. |

**Example**

Loads the lookup table "coupler_map.ixml" and prints the cell array that containing all
the contents of the .ixml file

```
clear;
tabCoupler = lookupread( "coupler_map.ixml" );
?toscript( tabCoupler );
```

where “coupler_map.ixml” is a lookup table containing a map between coupler parameters
and different s-parameters:

```
tabCoupler=cell(1);
tabCoupler{1}=struct;
tabCoupler{1}.association=cell(1);
tabCoupler{1}.association{1}=struct;
tabCoupler{1}.association{1}.design=cell(1);
tabCoupler{1}.association{1}.design{1}=struct;
tabCoupler{1}.association{1}.design{1}.name='gap';
tabCoupler{1}.association{1}.design{1}.value=3.5e-007;
tabCoupler{1}.association{1}.extracted=cell(1);
tabCoupler{1}.association{1}.extracted{1}=struct;
tabCoupler{1}.association{1}.extracted{1}.name='coupling_length';
tabCoupler{1}.association{1}.extracted{1}.value=7.18624e-006;
tabCoupler{1}.name='coupler_extracted';
```

The following commands insert an object into the existing lookup table:

```
association=struct;
association.design=cell(1);
association.design{1}=struct;
association.design{1}.name='gap';
association.design{1}.value=5e-007;
association.extracted=cell(1);
association.extracted{1}=struct;
association.extracted{1}.name='coupling_length';
association.extracted{1}.value=9e-006;
# insert association at last position
tabCoupler{1}.association = insert( tabCoupler{1}.association, association, 2 );
# print updated values
?toscript(tabCoupler);
lookupwrite( "coupler_map.ixml", tabCoupler );
```

now the table prints as below:

```
tabCoupler=cell(1);
tabCoupler{1}=struct;
tabCoupler{1}.association=cell(2);
tabCoupler{1}.association{1}=struct;
tabCoupler{1}.association{1}.design=cell(1);
tabCoupler{1}.association{1}.design{1}=struct;
tabCoupler{1}.association{1}.design{1}.name='gap';
tabCoupler{1}.association{1}.design{1}.value=3.5e-007;
tabCoupler{1}.association{1}.extracted=cell(1);
tabCoupler{1}.association{1}.extracted{1}=struct;
tabCoupler{1}.association{1}.extracted{1}.name='coupling_length';
tabCoupler{1}.association{1}.extracted{1}.value=7.18624e-006;
tabCoupler{1}.association{2}=struct;
tabCoupler{1}.association{2}.design=cell(1);
tabCoupler{1}.association{2}.design{1}=struct;
tabCoupler{1}.association{2}.design{1}.name='gap';
tabCoupler{1}.association{2}.design{1}.value=5e-007;
tabCoupler{1}.association{2}.extracted=cell(1);
tabCoupler{1}.association{2}.extracted{1}=struct;
tabCoupler{1}.association{2}.extracted{1}.name='coupling_length';
tabCoupler{1}.association{2}.extracted{1}.value=9e-006;
tabCoupler{1}.name='coupler_extracted';
```

The following commands append a new association into the existing table:

```
clear;
design=cell(1);
design{1}=struct;
design{1}.name='gap';
design{1}.value=6e-007;
# create extracted parameter
extracted=cell(1);
extracted{1}=struct;
extracted{1}.name='coupling_length';
extracted{1}.value=9.9e-006;
# append to existing table
lookupappend( "coupler_map.ixml", "coupler_extracted", design, extracted );
# print contents
?toscript( lookupread( "coupler_map.ixml" ) );
```

Now the lookup table prints as below:

```
value=cell(1);
value{1}=struct;
value{1}.association=cell(3);
value{1}.association{1}=struct;
value{1}.association{1}.design=cell(1);
value{1}.association{1}.design{1}=struct;
value{1}.association{1}.design{1}.name='gap';
value{1}.association{1}.design{1}.value=3.5e-007;
value{1}.association{1}.extracted=cell(1);
value{1}.association{1}.extracted{1}=struct;
value{1}.association{1}.extracted{1}.name='coupling_length';
value{1}.association{1}.extracted{1}.value=7.18624e-006;
value{1}.association{2}=struct;
value{1}.association{2}.design=cell(1);
value{1}.association{2}.design{1}=struct;
value{1}.association{2}.design{1}.name='gap';
value{1}.association{2}.design{1}.value=5e-007;
value{1}.association{2}.extracted=cell(1);
value{1}.association{2}.extracted{1}=struct;
value{1}.association{2}.extracted{1}.name='coupling_length';
value{1}.association{2}.extracted{1}.value=9e-006;
value{1}.association{3}=struct;
value{1}.association{3}.design=cell(1);
value{1}.association{3}.design{1}=struct;
value{1}.association{3}.design{1}.name='gap';
value{1}.association{3}.design{1}.value=6e-007;
value{1}.association{3}.extracted=cell(1);
value{1}.association{3}.extracted{1}=struct;
value{1}.association{3}.extracted{1}.name='coupling_length';
value{1}.association{3}.extracted{1}.value=9.9e-006;
value{1}.name='coupler_extracted';
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ lookupopen ](./lookupopen.md) , [ lookupread ](./lookupread.md) ,
[ lookupwrite ](./lookupwrite.md) , [ lookupclose ](./lookupclose.md) ,
[ lookupreadtable ](./lookupreadtable.md) , [ lookupreadvalue ](./lookupreadvalue.md) ,
[ lookupreadnportsparameter ](./lookupreadnportsparameter.md) , [ insert ](./insert.md)
