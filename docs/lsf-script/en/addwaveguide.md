# addwaveguide

Adds a waveguide object in the simulation space.

| **Syntax**                 | **Description**                                                                                                                                                                                                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addwaveguide;              | Adds a waveguide in the simulation space. This function does not return any data.                                                                                                                                                                                       |
| addwaveguide(struct_data); | Adds a waveguide and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will create a bent waveguide using 4 poles. For mode
details on how the waveguide object generates the shape of the waveguide using the poles
take a look at this KB page:
[ Structures - Waveguide ](https://optics.ansys.com/hc/en-us/articles/360034382234-Structures-Waveguide)
.

```
addwaveguide;  

set("base width",600e-9);  
set("base height",220e-9);  
set("base angle",70);  

pole = [0,0; 1,9; 6,9.8; 10,10]*1e-6;  
set("poles",pole);  
  
set("material","Si (Silicon) - Palik");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md)
