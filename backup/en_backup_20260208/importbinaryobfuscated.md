# importbinaryobfuscated

This command is identical to importbinary but makes it possible to import data from a file that has been obfuscated. For details on how to obfuscate the data files, please see the Online Help in the User Guide, Structures section.

**Syntax** |  **Description**  
---|---  
out = importbinaryobfuscated(key,filename,file_units,x0,y0,z0,reverse_index_order); |  Import binary data from filename in three dimensional simulations. All arguments after the filename are optional.  
**Parameter** |  **Default value** |  **Type** |  **Description**  
---|---|---|---  
key |  required |  string |  The key that is used to decrypt the obfuscated file.  
filename |  required |  string |  name of the file with binary data to import. May contain complete path to file, or path relative to current working directory  
file_units |  "m" |  string |  The optional string argument file_units can be "m", "cm, "mm", "microns" or "nm" to specify the units in the file.  
x0 |  0 |  number |  The optional arguments x0, y0 and z0 specify the data origin in the global coordinates of the Graphical Layout Editor. For example, if you defined your volume with respect to a particular point in space, for example (0,0,-5) microns, then you should set z0 to -5 microns.  
y0 |  0 |  number |   
z0 |  0 |  number |   
reverse_index_order |  0 |  number |  The optional argument reverse_index_order can be set to 1 to reverse how the indices are interpreted in the file. It is best to verify the correct setting with a graphical import before using the script command.  
  
**Example**

Please refer this example [Obfuscating import data](**%20to%20be%20defined%20**).

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [importbinary](/hc/en-us/articles/360034408734-importbinary)
