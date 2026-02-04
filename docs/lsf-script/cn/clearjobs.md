<!-- Translation completed: 2026-02-04 -->
<!-- Original command: clearjobs -->

# clearjobs

**语法** | **描述**
---|---
clearjobs("solver"); | Remove all jobs from the job queue of the specified 求解器. If no 求解器 is specified, jobs for all solvers will be removed from job manager queue. No 求解器 参数 is needed for INTERCONNECT.

**示例**

    newproject;
    addfdtd;
    adddipole;
    addcircle;
    run;
    clearjobs;

    newproject;
    addfdtd;
    adddipole;
    addcircle;
    run;
    clearjobs;

**另请参阅**

[ addjob ](/hc/en-us/articles/360034410714-addjob) , [ runjobs ](/hc/en-us/articles/360034931373-runjobs) , [ listjobs ](/hc/en-us/articles/360034410774-listjobs)
