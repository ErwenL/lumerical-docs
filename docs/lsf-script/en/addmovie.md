# addmovie

Adds a movie monitor to the simulation environment. Movie monitors capture a desired
field component over the region spanned by the monitor for the duration of the
simulation.

| **Syntax**             | **Description**                                                                                                                                                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addmovie;              | Adds a movie monitor to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addmovie(struct_data); | Adds a movie monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will add a 2D z-normal movie monitor to the simulation
region, set its location and dimension, and set its resolution while keeping the aspect
ratio locked. Locking the aspect ratio ensures that the video will keep the shape of the
monitor data.

```
addmovie;
set("name","movie_1");
set("monitor type",3);  # 1 = 2D x-normal,  2 = 2D y-normal,  3 = 2D z-normal
set("x",0);
set("x span",5e-6);
set("y",0);
set("y span",5e-6);
set("z",0);
set("lock aspect ratio",1);
set("horizontal resolution",240);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md)
