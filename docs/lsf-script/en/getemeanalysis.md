# getemeanalysis

Gets calculation parameters in MODE' EME analysis window.

| **Syntax**                  | **Description**                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| ?getemeanalysis;            | Lists all the parameters in the analysis window.                                            |
| getemeanalysis("property"); | Gets the value of the calculation parameter named "property" in EME solver analysis window. |

**Examples**

This code will display the values of the "group spans" parameters from the EME setup
section of the EME analysis window.

```
# display the values of the group spans  
?getemeanalysis("group spans");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ Spot size converter ](**%20to%20be%20defined%20**) ,
[ setemeanalysis ](./getemeanalysis.md)
