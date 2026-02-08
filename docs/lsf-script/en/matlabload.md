# matlabload

## Notes

- Starting with Lumerical 2024 R1, MATLAB Linux libraries are no longer packaged with
  the Lumerical Applications
- We still support MATLAB file load and save for versions 7 and greater
- See this
  [KB for more information](https://optics.ansys.com/hc/en-us/articles/360026142074).

Load Matlab .mat data into workspace

| **Syntax**              | **Description**                                            |
| ----------------------- | ---------------------------------------------------------- |
| matlabload("filename"); | Load to the workspace the data of the specified .mat file. |

**Examples**

This is a simple example that shows how to load to workspace from a .mat data file.

```
#this file has variables data1, data2, data3
matlabload("myData.mat");  
?workspace;
matrices:
 data1 data2 data3
```

**See Also**

[MATLAB script integration – Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360034923913-MATLAB-script-integration)

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ matlabput ](./matlabput.md) ,
[ matlabsavelegacy ](https://optics.ansys.com/hc/en-us/articles/360034928133-matlabsavelegacy)
, [ matlabsave ](./matlabsave.md) ,
