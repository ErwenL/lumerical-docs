# adduniformheat

Adds a constant heat source to the HEAT solver region. The input is defined as the net
heat input to the volume in units of Watt. The uniform heat source can either be 2D or
3D. The heat input per unit volume (W/m 3 ) is calculated by dividing the net input
power by the volume of the (3D) source. In the case of a 2D source the volume of the
source is defined by setting the length in the third dimension equal to either the
"equivalent length" of the source or the "norm length" of the HEAT solver.

| **Syntax**                   | **Description**                                                                                                                                                                                                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adduniformheat;              | Adds a constant heat source to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| adduniformheat(struct_data); | Adds a constant heat source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script adds a 3D uniform heat source to the HEAT solver, sets its
dimension, and assigns a net input power.

```
adduniformheat;  # the dafult format of a newly created heat source is 3D  

set("x",0);  
set("x span",2e-6);  
set("y",0);  
set("y span",5e-6);  
set("z",0);  
set("z span",10e-6);  
set("total power",1e-4);  #  Pin = 0.1 mW
```

The following script adds a 2D y-normal uniform heat source to the HEAT solver, sets its
dimension, forces the length in the third dimension to be equal to the "norm length" of
the HEAT solver, and assigns a net input power.

```
adduniformheat;    

set("source type",2);  # 2D y-normal  
set("use solver norm length",1);  
set("x",0);  
set("x span",2e-6);  
set("y",0);  
set("z",0);  
set("z span",10e-6);  
set("total power",1e-4);  #  Pin = 0.1 mW
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ addimportheat ](./addimportheat.md)
