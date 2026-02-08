# savedata

Saves workspace variables to a Lumerical data file (ldf) file. To save monitor (D-card)
data to an ldf file, see the savedcard function.

| **Syntax**                            | **Description**                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------ |
| savedata("filename");                 | Saves all current variables to the specified file. This function does not return any data. |
| savedata("filename", var1, var2,...); | Saves only variables with the specified names to file.                                     |

**Examples**

This is a simple example that shows how to save two workspace variables to a .ldf data
file.

```
x=1:10;
y=x^2;
savedata("x_squared_data", x, y);
```

This example shows a section of code that could be used to save some specific data from
a monitor named xy_monitor. The data is first obtained with script functions such as
getdata and transmission. These workspace variables are then saved with the savedata
function.

Note that the complex file names can be created with the num2str command. This is useful
when doing parameter sweeps where a unique file name is required for each point in the
sweep.

```
# get data from the simulation to be saved
mname="xy_monitor";       # monitor name
x=getdata(mname,"x");      # position vectors associated with Ex fields
y=getdata(mname,"y");      # position vectors associated with Ex fields
Ex=getdata(mname,"Ex");     # Ex fields at monitor
T=transmission(mname);     # Power transmission through monitor
 
# save variables x, y, Ex, T and i to a data file
filename="results_"+num2str(i); # set filename. i could be a loop counter variable.
savedata(filename, x,y,Ex,T,i); 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ savedcard ](./savedcard.md) , [ loaddata ](./loaddata.md) ,
[ workspace ](./workspace.md) , [ matlabsave ](./matlabsave.md)
