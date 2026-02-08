# resumejobs

Resume all simulations in the job manager queue from previously created checkpoint. The script execution will be paused while the jobs run, then resume when all of the simulations have completed successfully. If errors occur, the script will not proceed.

**Syntax** |  **Description**  
---|---  
resumejobs; |  Resume jobs in the Job queue for FDTD. Use the computer resources and parallel settings that are specified in the Resource Manager.  
resumejobs("FDTD", option); |  Resume jobs in the Job queue for FDTD. option=0: resume jobs in single process mode using only the local computer. option=1: resume jobs using the computer resources and parallel settings that are specified in the Resource Manager. (default)  
  
**See Also**

[runjobs](/hc/en-us/articles/360034931373-runjobs), [resume](/hc/en-us/articles/360036896474-resume), [addjob](/hc/en-us/articles/360034410714-addjob), [clearjobs](/hc/en-us/articles/360034931393-clearjobs), [listjobs](/hc/en-us/articles/360034410774-listjobs), [save](/hc/en-us/articles/360034410814-save), [load](/hc/en-us/articles/360034410834-load)
