# listjobs

Lists all the jobs in the job manager queue.

**Syntax** |  **Description**  
---|---  
listjobs("solver"); |  Lists all the jobs in the Job queue for specified solver. If the solver is not specified, all the jobs for all solvers will be listed. No argument is necessary for this command in INTERCONNECT.  
  
**Example**

The following script code will list jobs under FDE solver queue in MODE.
    
    
    ?listjobs("FDE");

**See Also**

[run](/hc/en-us/articles/360034931333-run), [runsweep](/hc/en-us/articles/360034931413-runsweep), [addjob](/hc/en-us/articles/360034410714-addjob), [clearjobs](/hc/en-us/articles/360034931393-clearjobs), [save](/hc/en-us/articles/360034410814-save), [load](/hc/en-us/articles/360034410834-load)
