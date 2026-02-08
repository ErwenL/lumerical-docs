# resumejobs

Resume all simulations in the job manager queue from previously created checkpoint. The
script execution will be paused while the jobs run, then resume when all of the
simulations have completed successfully. If errors occur, the script will not proceed.

| **Syntax**                  | **Description**                                                                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| resumejobs;                 | Resume jobs in the Job queue for FDTD. Use the computer resources and parallel settings that are specified in the Resource Manager.                                                                                                               |
| resumejobs("FDTD", option); | Resume jobs in the Job queue for FDTD. option=0: resume jobs in single process mode using only the local computer. option=1: resume jobs using the computer resources and parallel settings that are specified in the Resource Manager. (default) |

**See Also**

[runjobs](./runjobs.md), [resume](./resume.md), [addjob](./addjob.md),
[clearjobs](./clearjobs.md), [listjobs](./listjobs.md), [save](./save.md),
[load](./load.md)
