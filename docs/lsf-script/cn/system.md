<!--
Translation from English documentation
Original command: system
Translation date: 2026-02-04 22:50:15
-->

# system

The system 命令 allows you 到 have 该 operating system (OS) execute 一个 命令, rather than 该 Lumerical Script Prompt.

**语法** |  **描述**  
---|---  
system("命令"); |  Run "命令" at 该 OS 命令 prompt. The system 命令 does not 返回 any 数据.  
  
**Note** : This command cannot be used while in [safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**示例**

Opens 该 text editor Notepad 在 windows.
    
    
     system("notepad");

The following example demonstrates 如何 该 system 命令 可以 为 used 到 获取 该 computer's date 和 时间 settings (wall-clock 时间), 用于 example, 到 时间 stamp your files. It 是 necessary 到 run 一个 system 命令 because 该 Lumerical 脚本 language does not currently have 一个 getDateAndTime scriptcommand. This example shows 如何 到 获取 该 时间 在 一个 Windows machine, but it could easily 为 modified 用于 other OS. The system 命令 是 used 到 save 该 current 时间 从 该 system clock into 一个 文件. The read 命令 是 那么 used 到 read 该 时间 从 该 文件.
    
    
    fname="cur_time.txt";    # 文件 name 到 store current 时间  
    
    cmd="echo %时间% >>" + fname; # system 命令 到 获取 current 时间 和 write 到 fname   
    
    rm(fname);          # delete 时间 文件  
    
    system(cmd);         # run 命令 到 获取 时间 和 save 到 文件  
    
    cur_time=read(fname);     # read 时间 从 文件  
    
    ?cur_time;             # current 时间: Hr, Min, Sec 

This example shows 如何 到 start 一个 新的 instance 的 该 Lumerical GUI 从 一个 脚本 文件 在 一个 Windows computer. For example, 如果 you have multiple Lumerical products, you 可能 find it useful 到 have one product (eg. CHARGE) 为 able 到 start 一个 second product (eg. FDTD). The following example 将 start 一个 新的 instance 的 FDTD 该 runs 该 脚本 文件 runAnalysis.lsf.

Two variations 的 该 命令 是 provided. In 该 first, 一个 新的 instance 的 FDTD Solution 是 started 和 将 run 该 脚本 文件 runAnalysis.lsf. When 此 是 executed, 该 initial instance 的 该 GUI (该 one running 该 system 命令) 将 为 frozen while 该 新的 instance 是 running. The first instance 将 continue running once 该 second instance 是 closed. Tip: you 应该 添加 一个 'exit' 命令 到 该 end 的 该 runAnalysis.lsf 脚本 so 该 新的 instance automatically closes 当 it reaches 该 end 的 该 脚本.

The second variation allows 该 first instance 的 该 GUI 到 continue running while 该 second instance 是 open.
    
    
    system('""C:\Program files\Lumerical\[[verpath]]\bin\fdtd-solutions.exe" -run "C:\temp\runAnalysis.lsf""');  
    
    system('start "name" /B "C:\Program files\Lumerical\[[verpath]]\bin\fdtd-solutions.exe" -run "C:\temp\runAnalysis.lsf"');

The following code 可以 为 used 在 Windows OS 到 launch 一个 FDTD 仿真 从 该 terminal 和 那么 immediately close 该 graphical interface.
    
    
    # specify 命令 到 run 从 该 terminal  
    
    save;  
    
    MPICMD = '"C:\Program Files\Lumerical\MPICH2\mpiexec.exe" -n 2';  
    
    engineCMD = '"C:\Program files\Lumerical\[[verpath]]\bin\fdtd-engine.exe"';  
    
    simulationCMD = '"' + currentfilename + '"';  
    
    ?fullCMD = MPICMD + " " + engineCMD + " " + simulationCMD;  
    
    # run 从 terminal  
    
    system('start "name" /B ' + fullCMD);  
    
    # exit CAD  
    
    exit;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ readdata ](/hc/en-us/articles/360034411234-readdata) , [ exit ](/hc/en-us/articles/360034931613-exit) , [ " ](/hc/en-us/articles/360034410394--) , [ currentfilename ](/hc/en-us/articles/360034931793-currentfilename)
