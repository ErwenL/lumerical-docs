# asapload

Loads data from an fld file from BRO's ASAP. asapload creates a d-card structure called
"fld_data" which contains all the data in the file. If "fld_data" exists, it will be
called "fld_data_2". After loading an asapfile with asapload, you can extract any
desired data., which can be

- Ex, Ey, Ez, Hx, Hy, Hz, x, y, z
- power, frequency, wavelength, index

| **Syntax**             | **Description**                                                                        |
| ---------------------- | -------------------------------------------------------------------------------------- |
| asapload;              | Select the file to load with the file browser. This function does not return any data. |
| asapload( "filename"); | Loads data from an fld file called "filename" without a file browser.                  |

**Examples**

After loading the file, you can use ?getdata to see a list of all d-cards, or the
variables in the d-card. Data can be extracted using the getdata function. For example,
the real part of Ex can be imaged using the following code.

```
asapload("asap.ldf");
?getdata;
global monitors:
 fld_data 
?getdata("fld_data");
f wavelength index power x y z Ex Ey
Ez Hx Hy Hz 
Ex = getdata("fld_data","Ex");
x = getdata("fld_data","x"); 
y = getdata("fld_data","y"); 
image(x,y,pinch(real(Ex)));
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ asapexport ](./asapexport.md) , [ asapimport ](./asapimport.md) ,
[ addimportedsource ](./addimportedsource.md) , [ fileexists ](./fileexists.md)
