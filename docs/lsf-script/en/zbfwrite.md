# zbfwrite

Zbfwrite writes a 4D dataset into a Zemax zbf file in the current directory. Data
written into the zbf file:

- Ex, Ey, Ez, x, y, z
- frequency, wavelength, index

\[[Note:]\] ONLY the transverse E field components are written to the zbf file. The
longitudinal component is not supported by the zbf format.

| **Syntax**                                                                                                                                                                                                                                                                                                             | **Description**                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| zbfwrite("filename",M);                                                                                                                                                                                                                                                                                                | Writes dataset M into zbf file. The dataset must include one frequency or wavelength value. If the fourth dimension is named "f" or "frequency", it will be automatically converted into wavelength. Any other name will be assumed to carry wavelength information and it will not be converted.                                                                       |
| zbfwrite("filename",M,index);                                                                                                                                                                                                                                                                                          | The optional parameter "index" is the refractive index that will be written into zbf file. A default value of "1" is used if no "index" is provided.                                                                                                                                                                                                                    |
| zbfwrite("filename",M,index,"attributeName");                                                                                                                                                                                                                                                                          | atributeName is an optional parameter with default value = "". This specifies the vector or scalar attribute to write. If a scalar attribute is written, it becomes an "unpolarized" zbf file. If nothing is specified(default value =""), then it will write the first vector attribute in the dataset, or the first scalar attribute if there is no vector attribute. |
| \[[Note:]\] The Zemax zbf file requires the data to be saved on a uniform grid of dimensions with a power of 2 (with \\(2^n \\times 2^m\\) points). The dataset will be interpolated on a grid with \\(n\\) and \\(m\\) defined so the mesh step is equal to or less than the smallest mesh step in the original data. |                                                                                                                                                                                                                                                                                                                                                                         |

______________________________________________________________________

### Example

The following code example shows how to create a dataset with correct dimensions and
write it into a zbf file with various optional parameters. The last section of the code
reads back the saved zbf file into the structure array and plots the field profile,
index, and wavelength.

```
# Create spatial distribution of E field data with Gaussian distribution
x = linspace(-5e-6,5e-6,100);
y = linspace(-6e-6,6e-6,101);
X = meshgridx(x,y);
Y = meshgridy(x,y);
Ex = exp(- (X^2+Y^2)/(2e-6)^2);
Ey = 2i*Ex;
Ez = 0*Ey;  

# Create dataset and add E field and wavelength data
M = rectilineardataset("E",x,y,0);
M.addparameter("lambda",500e-9);
M.addattribute("E",Ex,Ey,Ez);
M.addattribute("scalar",3*Ex);  

# Visualize the dataset before writing it into zbf file
visualize(M);  

# Write dataset M into zbf file in with and without the optional parameters
zbfwrite("testfile1.zbf",M);
zbfwrite("testfile2.zbf",M,1);
zbfwrite("testfile3.zbf",M,1,"E");
zbfwrite("testfile4.zbf",M,2,"scalar");  

# Read back the structured data from zbf file and visualize it
B = zbfread("testfile4.zbf");
visualize(B.beam);
?B.index;
B_beam=B.beam;
?B_beam.wavelength;
```

**See Also**

[ zbfexport ](./zbfwrite.md) , [ zbfload ](./zbfload.md) , [ zbfread ](./zbfread.md) ,
[ List of commands ](../lsf-script-commands-alphabetical.md)
