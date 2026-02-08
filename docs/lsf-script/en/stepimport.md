# stepimport

Adds a structure to the simulation environment with structure geometry loaded from
specified [STEP or CAD file](https://optics.ansys.com/hc/en-us/articles/360034398374).
This command is identical to
[cadimport](https://optics.ansys.com/hc/en-us/articles/42995962396307-cadimport-Script-command).

| **Syntax**                           | **Description**                                                                                                                                                                                                                |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| stepimport("filename",scale_factor); | Add new structures from a specified CAD file. The list of supported file formats can be found in the Knowledge Base article on [CAD import](https://optics.ansys.com/hc/en-us/articles/360034398374). SCALE_FACTOR (optional): |

- Allowed values are 3, 0, -3, -6, -9, corresponding to the options of the STEP import
  dialog in Ansys Lumerical Multiphysics™. For example, the value -9 means that a STEP
  file saved in meters will be read as if in nanometers. Structures will be imported as
  \\(10^{-9}\\) times the actual size.

- When 'scale_factor' is omitted, 'no scaling' is applied

## This function does not return any data.<br /> Note: How to handle the "Model size exceeds valid box" error The geometry in the finite-element IDE cannot exceed a maximum size, a fixed number of length units. This error can be avoided by changing the solver to use a larger length unit, or by supplying a smaller 'scale_factor' argument.

**Example**

The following script commands is used to create a 3D geometry based on the STEP file
provided in the Knowledge Base article on
[CAD import](https://optics.ansys.com/hc/en-us/articles/360034398374).

```
filename = "stepimport.step";  
stepimport(filename);
```

The following script commands is used to create a 3D geometry based on the SolidWork
file provided in the Knowledge Base article on CAD import, using a scaling factor of
\\(10^{-6}\\).

```
filename = "Caliper.SLDPRT";  
stepimport(filename, -6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ stlimport, ](https://optics.ansys.com/hc/en-us/articles/360034924733)[cadimport](https://optics.ansys.com/hc/en-us/articles/42995962396307-cadimport-Script-command)
