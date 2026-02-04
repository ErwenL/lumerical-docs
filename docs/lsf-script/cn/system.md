<!-- Translation completed: 2026-02-03 -->
<!-- Original command: system -->

# system

system命令允许您让操作系统(OS)执行命令，而不是在Lumerical脚本提示符中执行。

**语法** | **描述**
---|---
`system("command");` | 在OS命令提示符处运行"command"。system命令不返回任何数据。

**注意**：此命令不能在[安全模式](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode)下使用。

**示例**

在Windows中打开文本编辑器记事本。

```
system("notepad");
```

以下示例演示如何使用system命令获取计算机的日期和时间设置(挂钟时间)，例如用于为文件添加时间戳。由于Lumerical脚本语言目前没有getDateAndTime脚本命令，因此需要运行系统命令。此示例展示如何在Windows机器上获取时间，但也可以轻松修改为其他操作系统。system命令用于将系统时钟的当前时间保存到文件中。然后使用read命令从文件中读取时间。

```
fname="cur_time.txt";    # file name to store current time

cmd="echo %time% >>" + fname; # system command to get current time and write to fname 

rm(fname);          # delete time file

system(cmd);         # run command to get time and save to file

cur_time=read(fname);     # read time from file

?cur_time;             # current time: Hr, Min, Sec
```

此示例展示如何在Windows计算机上从脚本文件启动Lumerical GUI的新实例。例如，如果您有多个Lumerical产品，可能会发现让一个产品(如CHARGE)能够启动第二个产品(如FDTD)很有用。以下示例将启动运行脚本文件runAnalysis.lsf的FDTD新实例。

提供了两种命令变体。第一种将启动FDTD Solutions的新实例并运行脚本文件runAnalysis.lsf。执行时，GUI的初始实例(运行system命令的那个)将在新实例运行时冻结。第二个实例关闭后，第一个实例将继续运行。提示：您应该在runAnalysis.lsf脚本末尾添加'exit'命令，以便新实例在到达脚本末尾时自动关闭。

第二种变体允许GUI的第一个实例在第二个实例打开时继续运行。

```
system('""C:\Program files\Lumerical\[[verpath]]\bin\fdtd-solutions.exe" -run "C:\temp\runAnalysis.lsf""');

system('start "name" /B "C:\Program files\Lumerical\[[verpath]]\bin\fdtd-solutions.exe" -run "C:\temp\runAnalysis.lsf"');
```

以下代码可用于Windows操作系统从终端启动FDTD仿真，然后立即关闭图形界面。

```
# specify command to run from the terminal

save;

MPICMD = '"C:\Program Files\Lumerical\MPICH2\mpiexec.exe" -n 2';

engineCMD = '"C:\Program files\Lumerical\[[verpath]]\bin\fdtd-engine.exe"';

simulationCMD = '"' + currentfilename + '"';

?fullCMD = MPICMD + " " + engineCMD + " " + simulationCMD;

# run from terminal

system('start "name" /B ' + fullCMD);

# exit CAD

exit;
```

**参见**

[命令列表](List_of_commands.md), [readdata](readdata.md), [exit](exit.md), [currentfilename](currentfilename.md)
