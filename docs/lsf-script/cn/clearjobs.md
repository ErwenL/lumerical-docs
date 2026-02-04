<!--
Translation from English documentation
Original command: clearjobs
Translation date: 2026-02-04 22:49:48
-->

# clearjobs

Remove all jobs 从 该 job manager queue. 

**语法** |  **描述**  
---|---  
clearjobs("求解器");  |  Remove all jobs 从 该 job queue 的 该 specified 求解器. If no 求解器 是 specified, jobs 用于 all solvers 将 为 removed 从 job manager queue. No 求解器 参数 是 needed 用于 INTERCONNECT.   
  
**示例**
    
    
    newproject;
    addfdtd;
    adddipole;
    addcircle;
    run;
    clearjobs;

**参见**

[ addjob ](/hc/en-us/articles/360034410714-addjob) , [ runjobs ](/hc/en-us/articles/360034931373-runjobs) , [ listjobs ](/hc/en-us/articles/360034410774-listjobs)
