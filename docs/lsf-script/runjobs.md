# runjobs

Run all simulations in the job manager queue. The script execution will be paused while the jobs run, then resume when all of the simulations have completed successfully. If errors occur, the script will not proceed.

For Ansys Lumerical FDTD™, Ansys Lumerical MODE™, Ansys Lumerical Multiphysics™, and Ansys Lumerical INTERCONNECT™

**Syntax** |  **Description**  
---|---  
runjobs; |  Run jobs in the Job queue for existing (active) solver. Use the computer resources and parallel settings that are specified in the Resource Manager.  
runjobs("solver", option); |  Run jobs in the Job queue for specified solver. option=0: run jobs in single process mode using only the local computer. option=1: run jobs using the computer resources and parallel settings that are specified in the Resource Manager. (default)  
  
When using [Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical),

**Syntax** |  **Description**  
---|---  
runjobs(“solver”, “resource_type”, “burst”, burst_settings); |  Run jobs in the job queue for the specified solver using Ansys Cloud Burst Compute™ for Lumerical:

  * solver: Name of the solver, currently, only “FDTD” is supported
  * resource_type: Type of simulation to run, either “CPU” or “GPU”
  * burst_settings: Settings structure to use for the current job submission. The structure fields should match the results obtained from getresource. The “queue” field must be specified in this structure. Any fields left blank uses default settings.

  
  
**Example**

The following script code illustrates how to use the addjob and runjobs script commands to do a parameter sweep. The initial for loop creates a simulation file for each point in the sweep and adds the simulations to the job queue. Next, the runjobs command will run all simulations in the job queue. If multiple computer resources are configured in the Resource Manager, then simulations will run concurrently. When all of the simulations are complete, a second for loop is used to re-load each simulation file and do the required analysis.
    
    
    # create 10 simulation files and add them to the job queue
    newproject;
    addvarfdtd;
    adddipole;
    addcircle;
    rad=linspace(1e-6,10e-6,10);
    for(i=1:10) {
    setnamed("circle","radius",rad(i));
    save("temp_"+num2str(i));
    addjob(currentfilename);
    }
    runjobs;
    # run all jobs in the job queue
    runjobs;
    # load each simulation and do required analysis
    for(i=1:10) {
     load("temp_"+num2str(i));
     ...
    }

**See Also**

[ run ](/hc/en-us/articles/360034931333-run) , [ runsweep ](/hc/en-us/articles/360034931413-runsweep) , [ addjob ](/hc/en-us/articles/360034410714-addjob) , [ clearjobs ](/hc/en-us/articles/360034931393-clearjobs) , [ listjobs ](/hc/en-us/articles/360034410774-listjobs) , [ save ](/hc/en-us/articles/360034410814-save) , [ load ](/hc/en-us/articles/360034410834-load)
