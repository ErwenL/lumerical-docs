# listjobs

Lists all the jobs in the job manager queue.

| **Syntax**          | **Description**                                                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| listjobs("solver"); | Lists all the jobs in the Job queue for specified solver. If the solver is not specified, all the jobs for all solvers will be listed. No argument is necessary for this command in INTERCONNECT. |

**Example**

The following script code will list jobs under FDE solver queue in MODE.

```
?listjobs("FDE");
```

**See Also**

[run](./run.md), [runsweep](./runsweep.md), [addjob](./addjob.md),
[clearjobs](./clearjobs.md), [save](./save.md), [load](./load.md)
