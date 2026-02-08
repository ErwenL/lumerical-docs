# addport (FDTD)

Adds a port object to the ports group under the FDTD simulation region. A simulation
region must be present in order to add a port. For more information about the port
object see [ Ports ](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports) .
This topic addresses the addport command in FDTD - for information about the
INTERCONNECT command, see
[ addport (INTERCONNECT) ](https://optics.ansys.com/hc/en-us/articles/360034408934-addport)
.

| **Syntax**            | **Description**                                                                                                                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| addport;              | Adds a port. This function does not return any data.                                                                                                                                                                                                               |
| addport(struct_data); | Adds a port and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example** The following script adds a FDTD simulation region and port, then sets the
name of the port, and selects the port modes and source mode.

```
addfdtd; # add FDTD simulation region
addport; # add port
# set up port
set("name","input_port"); 
seteigensolver("bent waveguide",true); 
seteigensolver("bend radius",10e-6); 
updateportmodes(1:2); # select the first 2 modes of the port
# select the second mode of the port to be the source mode
select("FDTD::ports"); # select the port group
set("source port","input_port");
set("source mode","mode 2");
```

**See Also**

[ Ports ](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports) ,
[ set ](./set.md) , [ geteigensolver ](./geteigensolver.md) ,
[ seteigensolver ](./seteigensolver.md) , [ updateportmodes ](./updateportmodes.md) ,
[ clearportmodedata ](./clearportmodedata.md)
