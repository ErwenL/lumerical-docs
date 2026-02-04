<!--
Translation from English documentation
Original command: listjobs
Translation date: 2026-02-03
-->

# listjobs

列出作业管理器队列中的所有作业。

**语法** |  **描述**
---|---
listjobs("solver"); |  列出指定求解器的作业队列中的所有作业。如果未指定求解器，则将列出所有求解器的作业。在 INTERCONNECT 中，此命令不需要参数。

**示例**

以下脚本代码将列出 MODE 中 FDE 求解器队列下的作业。

    ?listjobs("FDE");

**相关命令**

- [run](./run.md)
- [runsweep](./runsweep.md)
- [addjob](./addjob.md)
- [clearjobs](./clearjobs.md)
- [save](./save.md)
- [load](./load.md)
