# addport (INTERCONNECT)

Adds a port to a compound/script element (Note that this command does not apply for
primitive elements). This topic addresses the addport command in INTERCONNECT - for
information about the FDTD command, see
[ addport (FDTD) ](https://optics.ansys.com/hc/en-us/articles/360034924793-addport) .

| **Syntax**                                                          | **Description**                                                                                             |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| addport("element", "port", "type", "data", "position", "location"); | Adds a new port to the element with the specified properties. Returns the name of the port that is created. |
| **Property**                                                        |                                                                                                             |
| ---                                                                 | ---                                                                                                         |
| element                                                             | required                                                                                                    |
| port                                                                | required                                                                                                    |
| type                                                                | required                                                                                                    |
| data                                                                | required                                                                                                    |
| position                                                            | optional                                                                                                    |
| location                                                            | optional                                                                                                    |

**Example**

Open this example file compound_element.icp from
[ Compound Elements ](**%20to%20be%20defined%20**) and input the following script

```
disconnect("Optical Network Analyzer","input 1","Compound Element","port 2");
disconnect("Optical Network Analyzer","output","Compound Element","port 1");
removeport("Compound Element","port 1"); #delete the port
addport("Compound Element","port 1","input","optical Signal"); #add port
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ removeport ](./removeport.md)
