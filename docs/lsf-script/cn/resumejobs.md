<!--
Translation Status: Completed
Source: docs/lsf-script/en/resumejobs.md
Last Updated: 2026-02-03
-->

# resumejobs

从先前创建的检查点恢复作业管理器队列中的所有模拟。脚本执行将在作业运行时暂停，然后在所有模拟成功完成后恢复。如果发生错误，脚本将不会继续执行。

**语法** |  **说明**  
---|---  
resumejobs; |  恢复FDTD的作业队列中的作业。使用在资源管理器中指定的计算机资源和并行设置。  
resumejobs("FDTD", option); |  恢复FDTD的作业队列中的作业。option=0：仅以单进程模式使用本地计算机恢复作业。option=1：使用在资源管理器中指定的计算机资源和并行设置恢复作业。（默认值）  
  
**另请参见**

- [runjobs](./runjobs.md)
- [resume](./resume.md)
- [addjob](./addjob.md)
- [clearjobs](./clearjobs.md)
- [listjobs](./listjobs.md)
- [save](./save.md)
- [load](./load.md)
