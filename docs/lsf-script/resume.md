# resume

Resume the simulation from previously created [checkpoint](https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object#h_01HQ233EQNZ88X91YBEKF8SQ9R). When the simulation finishes, all simulation data will be saved to the current simulation file. The updated simulation file will then be re-loaded by the GUI.

**Syntax** |  **Description**  
---|---  
resume; |  Launch the simulation in parallel mode as defined in the resource manager. This function does not return any data.  
resume(option1); |  Option1 (default: 3) can be:

  * 1: resume FDTD in single processor mode (legacy) avoiding any use of MPI.
  * 2: resume FDTD in single processor mode (legacy). Pop-up dialogs no longer take focus.
  * 3: resume FDTD in parallel mode as defined in the resource manager.

  
  
**Requirements to resume**

  * Project must be identical with the exception of "auto shutoff min" and "auto shutoff max".
  * Project can be in either layout or analysis mode. Simulation can still be resumed after switching to layout.
  * Each of multiple/distributed/MPI processes must have access to its particular checkpoint file. User may need to [specify process rank allocation](https://software.intel.com/en-us/mpi-developer-guide-linux-controlling-process-placement).
  * Processor layout, MPI technology (mpich or impi etc), platform (linux/mac/windows), CPU architecture, and Lumerical build number must be the same



**Memory usage**

  * Checkpointing or resuming from checkpoint does not require extra memory



**Supported Objects**

  * All source and monitors types.
  * To resume a movie monitor, the previous movie file must still exist on disk. Otherwise the movie monitor will be ignored.



**See Also**

[run](/hc/en-us/articles/360034931333-run), [resumejobs](/hc/en-us/articles/360036896654-resumejobs), [FDTD simulation object](/hc/en-us/articles/360034382534-Simulation%20-%20FDTD)
