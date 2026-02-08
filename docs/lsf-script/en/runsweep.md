# runsweep

Runs a parameter sweep or optimization task.

| **Syntax**                            | **Description**                                                                                                   |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| runsweep;                             | Runs all sweeps and optimization tasks. In FDTD, this will run tasks in CPU mode.                                 |
| runsweep("taskname");                 | Runs only the sweep or optimization named taskname. In FDTD, this will run the sweep or optimization in CPU mode. |
| runsweep(“resource_type”);            | FDTD only, runs all sweeps and optimization tasks using a specified resource_type, either “GPU” or “CPU”          |
| runsweep("taskname",”resource_type”); | FDTD only, runs the sweep or optimization named taskname using a specified resource_type, either “CPU” or “GPU”.  |

When using
[Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical),

| **Syntax**                                                     | **Description**                                                                                                                                                 |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| runsweep(“taskname”,”resource_type”, “burst”, burst_settings); | Run a single parameter sweep with a specific type of resource. An error is returned in the sweep uses a solver that does not support Ansys Cloud Burst Compute: |

- taskname: Name of sweep to run
- resource_type: Type of resource to run, either “CPU” or “GPU”
- burst_settings: Optional, settings structure to use for the current job submission.
  The structure fields should match the results obtained from
  [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command).
  If left empty, default settings are used.

runsweep(“type”,”burst”, burst_settings); | Run all sweeps with the specified resource
type. The settings are applied to all sweeps. An error is returned if a sweep in the
list does not support Ansys Cloud Burst Compute:

- type: Type of resource to run, either “CPU” or “GPU”
- burst_settings: Optional, settings structure to use for the current job submission.
  The structure fields should match the results obtained from
  [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command).
  If left empty, default settings are used.

**Example**

```
runsweep;
runsweep("thickness_sweep");
```

**See Also**

[ run ](./run.md) , [ getsweepdata ](./getsweepdata.md) , [ addjob ](./addjob.md) ,
[ runjobs ](./runjobs.md) ,
[ parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
