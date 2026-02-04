<!--
Translation from English documentation
Original command: resume
Translation date: 2026-02-04 22:50:14
-->

# resume

Resume the simulation from previously created [checkpoint](https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object#h_01HQ233EQNZ88X91YBEKF8SQ9R). When the simulation finishes, all simulation data will be saved to the current simulation file. The updated simulation file will then be re-loaded by the GUI.

**语法** |  **描述**  
---|---  
resume; |  Launch 该 仿真 在 parallel mode as defined 在 该 resource manager. This 函数 does not 返回 any 数据.  
resume(option1); |  Option1 (default: 3) 可以 为:

  * 1: resume FDTD 在 single processor mode (legacy) avoiding any use 的 MPI.
  * 2: resume FDTD 在 single processor mode (legacy). Pop-up dialogs no longer take focus.
  * 3: resume FDTD 在 parallel mode as defined 在 该 resource manager.

  
  
**Requirements 到 resume**

  * Project 必须 为 identical 使用 该 exception 的 "auto shutoff min" 和 "auto shutoff max".
  * Project 可以 为 在 either layout 或 分析 mode. Simulation 可以 still 为 resumed after switching 到 layout.
  * Each of multiple/distributed/MPI processes must have access to its particular checkpoint file. User may need to [specify process rank allocation](https://software.intel.com/en-us/mpi-developer-guide-linux-controlling-process-placement).
  * Processor layout, MPI technology (mpich 或 impi etc), platform (linux/mac/windows), CPU architecture, 和 Lumerical build 数字 必须 为 该 same



**Memory usage**

  * Checkpointing 或 resuming 从 checkpoint does not require extra memory



**Supported Objects**

  * All 源 和 monitors types.
  * To resume 一个 movie 监视器, 该 previous movie 文件 必须 still exist 在 disk. Otherwise 该 movie 监视器 将 为 ignored.



**参见**

[run](/hc/en-us/articles/360034931333-run), [resumejobs](/hc/en-us/articles/360036896654-resumejobs), [FDTD 仿真 对象](/hc/en-us/articles/360034382534-Simulation%20-%20FDTD)
