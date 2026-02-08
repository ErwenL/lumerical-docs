# importdataset

This command can be used to import a rectilinear or unstructured dataset into a
simulation object.

| **Syntax**                | **Description**                                                                                                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| importdataset("filename") | Imports the dataset from the specified Matlab file in the current working directory. The object to load data into must be selected.                                                                                                         |
| importdataset(charge)     | Imports the data from the specified dataset in the script workspace. The dataset can be loaded from a Matlab file to the script workspace using the [ matlabload ](./matlabload.md) command. The object to load data into must be selected. |

There are several cases where this command can be used

1\. Import data into a grid attribute (data could be from charge monitor or temperature
monitor in Finite Element IDE).

2\. Import doping data into a selected 'import doping' object.

3\. Import optical generation data into a selected 'import generation' object.

4\. Import field data to an import source (FDTD).

5\. Import field data to a port object (FDTD and MODE).

The command can be used in two ways. The dataset can be saved inside a matlab (.mat)
file which can be called to load the data or, the command can directly call the dataset
from the script workspace to load it into the simulation object. In both cases, the
dataset need to have the following properties:

| **Data**                                           | **Simulation object**                                                                   | **Dataset type**            | **Name for variables defining coordinate data**                                                                                                                  | **Name for variables defining actual data** |
| -------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Liquid crystal orientation (3 element unit vector) | 'lc orientation' grid attribute                                                         | Rectilinear                 | x, y, z                                                                                                                                                          | u                                           |
| Rotation angles in radians                         | 'permittivity rotation' grid attribute                                                  | Rectilinear                 | x, y, z                                                                                                                                                          | theta, phi, psi                             |
| Unitary transform matrix (3x3 tensor)              | 'matrix transform' grid attribute                                                       | Rectilinear                 | x, y, z                                                                                                                                                          | U                                           |
| Charge density                                     | 'np density' grid attribute                                                             | Unstructured                | x, y, z, C                                                                                                                                                       | n, p                                        |
| Doping profile                                     | 'Import doping' object                                                                  | Unstructured or rectangular | x, y, z, C (unstructured); x, y, z (rectangular)                                                                                                                 | N                                           |
| Optical generation rate                            | Import generation' object                                                               | Rectangular                 | x, y, z                                                                                                                                                          | G                                           |
| Temperature in Kelvin                              | 'temperature' grid attribute                                                            | Unstructured                | x, y, z, elements (see [ Dataset builder ](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder) for more information)                        | N                                           |
| E and H field data                                 | Import source in FDTD                                                                   | Rectilinear                 | x, y, z, f (optional) (see [ Sources - Import ](https://optics.ansys.com/hc/en-us/articles/360034383014-Sources-Import) for more information)                    | E (required), H (optional)                  |
| E and H field data                                 | Port in MODE EME solver (note that only 1 mode can be imported at a time for each port) | Rectilinear                 | x,y,z (see [ Impoting arbitrary source fields ](https://optics.ansys.com/hc/en-us/articles/360034396394-Importing-arbitrary-source-fields) for more information) | E, H                                        |

**Examples**

This example shows how to import an unstructured dataset 'charge' to the 'np Density'
grid attribute.

```
select("np density");
importdataset("device_data.mat");
```

It is also equivalent to the method below.

```
select("np Density");
matlabload("device_data.mat");
importdataset(charge);
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ cleardataset ](./cleardataset.md) , [ matlabload ](./matlabload.md) ,
[ Mach Zehnder ](https://apps.lumerical.com/pn_phase_shifter.html) ,
[ Import/export np Density ](https://optics.ansys.com/hc/en-us/articles/360034382494-Charge-to-index-conversion)
, [ addgridattribute ](./addgridattribute.md) ,
[ unstructureddataset ](./unstructureddataset.md)
