# mcfit

The script command runs the multi-coefficient fitting for a file containing multiple
frequency dependent transmission values.

| **Syntax**                                                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mcfit(filenamein,filenameout,npoles,tolerance,automatic) ; | Runs the multi-coefficient fitting for a file containing multiple frequency dependent transmission values (filenamein), where each transmission depends on an operating point, and generates a file containing the fitting data (filenameout). The number of poles and the fitting tolerance are defined by parameters npoles and tolerance respectively. The parameter ‘automatic’ define if the fitting will use the user defined npoles or estimate the number of poles automatically. |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ mczfit ](./mczfit.md)
