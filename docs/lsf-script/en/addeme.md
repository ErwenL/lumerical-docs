# addeme

Adds an
[Eigenmode Expansion (EME) solver region](https://optics.ansys.com/hc/en-us/articles/360034917013)
to the MODE simulation environment.

| **Syntax**           | **Description**                                                                                                                                                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addeme;              | Add an EME solver region to the simulation environment. This function does not return any data.                                                                                                                                                                                  |
| addeme(struct_data); | Adds an EME solver region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add an EME solver region, set its dimension and other
properties, and run the simulation. The script assumes that the simulation environment
already has the geometry set up.

```
addeme;
# set dimension
set("x min",-8e-6);
set("y",0);
set("y span",5.5e-6);
set("z",0.5e-6);
set("z span",7e-6);
# set cell properties
set("number of cell groups",3);
set("group spans",[3e-6; 10e-6; 3e-6]);
set("cells",[1; 19; 1]);
set("subcell method",[0; 1; 0]);   # 0 = none,  1 = CVCS
# set up ports: port 1
select("EME::Ports::port_1");
set("use full simulation span",1);
set("y",0);
set("y span",5.5e-6);
set("z",0);
set("z span",7e-6);
set("mode selection","fundamental mode");
# set up ports: port 2
select("EME::Ports::port_2");
set("use full simulation span",1);
set("y",0);
set("y span",5.5e-6);
set("z",0);
set("z span",7e-6);
set("mode selection","fundamental mode");
run;
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ select ](./select.md) ,
[ run ](./run.md) , [ addvarfdtd ](./addvarfdtd.md) , [ addfde ](./addfde.md)
