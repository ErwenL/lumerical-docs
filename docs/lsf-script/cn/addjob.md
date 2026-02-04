# addjob

<!-- 翻译说明：本文档已被人工翻译为中文，如有错误请指正 -->
<!-- Translation metadata: manually_translated=true, reviewer=none, last_updated=2026-02-04 -->

将仿真文件添加到作业管理器队列。

**语法** | **说明**
---|---
addjob(filename,"solver"); | 将仿真文件"filename"添加到作业管理器队列。"solver"参数用于选择要添加作业的求解器，如果仿真环境中只存在一个（或活动）求解器，则该参数是可选的。INTERCONNECT不支持"solver"参数。

**示例**

指定短文件名。在这种情况下，当前工作目录路径将被添加到文件名中。


    addjob("mySimulation.fsp"); 

指定带完整路径的文件名。


    file="C:\working\mySimulation.fsp";
    addjob(file); 

使用currentfilename脚本命令指定文件名。


    addjob(currentfilename); 

有关更完整的示例，请参见runjobs脚本命令页面。

**另请参阅**

[run](/hc/en-us/articles/360034931333-run) , [runsweep](/hc/en-us/articles/360034931413-runsweep) , [runjobs](/hc/en-us/articles/360034931373-runjobs) , [clearjobs](/hc/en-us/articles/360034931393-clearjobs) , [listjobs](/hc/en-us/articles/360034410774-listjobs) , [currentfilename](/hc/en-us/articles/360034931793-currentfilename)
