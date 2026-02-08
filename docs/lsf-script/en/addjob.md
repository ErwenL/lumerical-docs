# addjob

Adds a simulation file to the job manager queue.

| **Syntax**                 | **Description**                                                                                                                                                                                                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addjob(filename,"solver"); | Add the simulation file "filename" to the job manager queue. The "solver" argument is used to select the solver to add the job to and is optional if only one solver exists (or is active) in the simulation environment. The "solver" argument is not supported by INTERCONNECT. |

**Example**

Specify short file name. In this case, the current working directory path will be added
to the filename.

```
addjob("mySimulation.fsp");  
```

Specify filename with full path.

```
file="C:\working\mySimulation.fsp";
addjob(file);  
```

Specify filename with the currentfilename script command.

```
addjob(currentfilename);  
```

For a more complete example, see the runjobs script command page.

**See Also**

[ run ](./run.md) , [ runsweep ](./runsweep.md) , [ runjobs ](./runjobs.md) ,
[ clearjobs ](./clearjobs.md) , [ listjobs ](./listjobs.md) ,
[ currentfilename ](./currentfilename.md)
