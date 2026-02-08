# getresource

Returns the current setting for properties of the available resources in resource
manager for the specified solver. This command is also used to obtain submittable fields
for
[Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical).

For all resources except Ansys Cloud Burst Compute™ for Lumerical:

| **Syntax**                                           | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out=getresource("solver", resource_num, "property"); | Returns the current setting for properties of the available resources in resource manager for the specified solver. The "solver" argument is used to select the solver from which the resource is being selected. The "solver" argument is not supported by INTERCONNECT. resource_num is the number of the desired resource (row number in resource manager) and is optional. If not specified, the command will return the number of resources currently available for the specified solver. "property" is the desired property of the resource and is optional. If not specified, the command will return a list of all properties available for the resource. |

When using
[Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical):

| **Syntax**                                                                                                                                            | **Description**                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| out=getresource("burst");                                                                                                                             | Returns a structure containing burst settings. The fields of the output structure are described below. |
| out = getresource(“burst”,”accounts”);                                                                                                                | Returns a list of available burst accounts to choose from.                                             |
| out = getresource(“burst”, “name”, “resource_type”);                                                                                                  | Returns a list of available queues for the account specified by the parameter name.                    |
| The queue type, as specified by the resource_type parameter, can either be “GPU” for a list of all GPU queues, or “CPU” for a list of all CPU queues. |                                                                                                        |

The structure returned by `getresource("burst")` is described below. These are the
fields that can be modified during job submission.

The settings for Ansys Cloud Burst Compute for Lumerical will be reverted to default
after every job submission. As such, the values of each field will be their default
values. To modify settings during job submission, see
[run](https://optics.ansys.com/hc/en-us/articles/360034931333-run-Script-command) and
[runsweep](https://optics.ansys.com/hc/en-us/articles/360034931413-runsweep-Script-command).

| **Field**                                                                                              | **Description**                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account                                                                                                | Current account name.                                                                                                                                                                                                                                                             |
| download                                                                                               | Whether or not to download the results after simulation completion. This is 0 if the results are not downloaded, and 1 if the results are downloaded. The results can be downloaded from [Ansys Engineering Portal](https://portal.ansys.com/) if automatic download is disabled. |
| jobMonitoring                                                                                          | Whether or not job monitoring from the GUI is enabled. This result 0 if you are not monitoring the job in the GUI. An Ansys Engineering Portal link to the job is provided in the script prompt when you submit a job without monitoring.                                         |
| name                                                                                                   | Name of the current Ansys Cloud Burst Compute job.                                                                                                                                                                                                                                |
| queue                                                                                                  | Name of the queue to be used for the job. By default, this will be empty to indicate that a queue will be automatically selected.                                                                                                                                                 |
| You can find a list of queues using the `getresource("burst","name","type")` command documented above. |                                                                                                                                                                                                                                                                                   |

**Example**

This example will return the number of processes currently set for the second resource
of the DGTD solver in Finite Element IDE

```
out=getresource("DGTD",2,"processes");
```

**See Also**

[addresource](./addresource.md), [setresource](./setresource.md),
[deleteresource](./deleteresource.md)
