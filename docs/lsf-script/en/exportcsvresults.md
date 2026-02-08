# exportcsvresults

This script command can export the results of a simulation to comma separated value
formatted files, which can be opened by Microsoft Excel.

| **Syntax**                                  | **Description**                                                                                     |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| exportcsvresults("filename")                | exports the results of the entire simulation to multiple .cvs files, named filename_elementname.csv |
| exportcsvresults("filename", "elementname") | exports the results of the specified element to a .cvs file, named filename_elementname.csv         |

| **Parameter** | **Type** | **Description**       |
| ------------- | -------- | --------------------- |
| filename      | string   | name of the .csv file |
| elementname   | string   | name of the element.  |

### See Also

[ List of commands ](../lsf-script-commands-alphabetical.md)
