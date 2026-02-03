# clearjobs

Remove all jobs from the job manager queue. 

**Syntax** |  **Description**  
---|---  
clearjobs("solver");  |  Remove all jobs from the job queue of the specified solver. If no solver is specified, jobs for all solvers will be removed from job manager queue. No solver argument is needed for INTERCONNECT.   
  
**Example**
    
    
    newproject;
    addfdtd;
    adddipole;
    addcircle;
    run;
    clearjobs;

**See Also**

[ addjob ](/hc/en-us/articles/360034410714-addjob) , [ runjobs ](/hc/en-us/articles/360034931373-runjobs) , [ listjobs ](/hc/en-us/articles/360034410774-listjobs)
