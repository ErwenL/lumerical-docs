# run

Run the current simulation. When the simulation finishes, all simulation data will be
saved to the current simulation file. The updated simulation file will then be re-loaded
by the GUI. This function does not return any data.

For MODE, CHARGE, HEAT, FEEM, DGTD,

| **Syntax**     | **Description**                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| run;           | Launch the simulation in parallel mode as defined in the resource manager.                              |
| run(“solver”); | Launch the simulation using the specified “solver” in parallel mode as defined in the resource manager. |

For FDTD and RCWA,

| **Syntax**                                                                                                                                                                                             | **Description**                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| run;                                                                                                                                                                                                   |                                                                                                                              |
| Launch the simulation using the resource set in the [run simulation group](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface) of the simulator tab. |                                                                                                                              |
| run("solver");                                                                                                                                                                                         | Launch the simulation using the specified “solver”, using the resource set in the run simulation group of the simulator tab. |
| run("solver", "resource_type")                                                                                                                                                                         | Launch the simulation using solver and resource_type:                                                                        |

- solver: solver name, can be “FDTD”, “RCWA”
- resource_type: resource type, can be "CPU", "GPU" for FDTD, and “CPU” only for RCWA

This allows to use the specified resource without affecting the CPU/GPU selection set in
the
[run simulation group](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface)
of the simulator tab.\
run("solver", "resource_type", "resource_name"); | Launch the simulation using solver,
resource_type, and with a specified resource_name:

- solver: solver name, can be “FDTD”, “RCWA”
- resource_type: resource type, can be "CPU", "GPU" for FDTD, and “CPU” only for RCWA
- resource_name: resource name, must follow a resource set in the
  [resource configuration window](https://optics.ansys.com/hc/en-us/articles/360058790674-Resource-configuration-elements-and-controls)

run("FDTD", "GPU", "resource_name", CUDA_VISIBLE_DEVICE_values); | Launch an FDTD GPU
simulation with a specified resource_name and CUDA_VISIBLE_DEVICE_values:

- resource_name: resource name, must follow a resource set in the resource configuration
  window
- CUDA_VISIBLE_DEVICE_values: GPUs to be used specified by the environment variable
  CUDA_VISIBLE_DEVICE, can be a single value or a matrix representing multiple GPUs

For INTERCONNECT,

| **Syntax** | **Description**                                                                                                              |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------- |
| run;       | Launch the simulation. The simulation will be run using the settings from the first active resource in the resource manager. |

When using
[Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical),

| **Syntax**                                               | **Description**                |
| -------------------------------------------------------- | ------------------------------ |
| run(“solver”, “resource_type”, “burst”, burst_settings); | Submits the current burst job: |

- solver: Name of the solver, currently, only “FDTD” is supported
- resource_type: Type of simulation to run, either “CPU” or “GPU”
- burst_settings: Optional, settings structure to use for the current job submission.
  The structure fields should match the results obtained from
  [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command).

**Example**

Create and run a new simulation in FDTD.

```
newproject;  # create a new simulation file
addfdtd;    # add the FDTD simulation region
adddipole;   # add a diopole source
run;      # run the simulation in parallel mode
```

**See Also**

[ runanalysis ](./runanalysis.md) , [ addjob ](./addjob.md) , [ runjobs ](./runjobs.md)
, [ save ](./save.md) , [ load](./load.md),
[FDTD GPU Solver Information](https://optics.ansys.com/hc/en-us/articles/17518942465811)
