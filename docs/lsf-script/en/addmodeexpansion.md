# addmodeexpansion

Adds a mode expansion monitor to the simulation environment. In MODE an active varFDTD
region needs to be present for this command to work.

| **Syntax**                     | **Description**                                                                                                                                                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addmodeexpansion;              | Adds a mode expansion monitor to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addmodeexpansion(struct_data); | Adds a mode expansion monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will add mode expansion and field monitors and then setup
some of the expansion monitor properties.

```
# add monitors
addmodeexpansion;
set("name","mode_expansion");
addpower;
set("name","field");
# set the field monitor to be used by the expansion monitor
select("mode_expansion");
setexpansion("input", "field");
# set the expansion monitor mode solver properties
if (true) { 
# select fundamental, fundamental TE or fundamental TM mode 
  set("mode selection","fundamental mode");
} else { 
# alternately, set expansion monitor mode solver properties,  
# rather than one of the 'fundamental modes 
  set("mode selection","user select"); # use the 'user select' option 
  seteigensolver("use max index",0); # specify a custom value for 'n' 
  seteigensolver("n",1.1); updatemodes(3); # select the 3rd mode
}
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ Using Mode Expansion Monitors ](https://optics.ansys.com/hc/en-us/articles/360034902433-Using-Mode-Expansion-Monitors)
, [ setexpansion ](./setexpansion.md) , [ removeexpansion ](./removeexpansion.md) ,
[ updatemodes ](./updatemodes.md) , [ seteigensolver ](./seteigensolver.md) ,
[ geteigensolver ](./geteigensolver.md)
