# system

The system command allows you to have the operating system (OS) execute a command,
rather than the Lumerical Script Prompt.

| **Syntax**         | **Description**                                                                      |
| ------------------ | ------------------------------------------------------------------------------------ |
| system("command"); | Run "command" at the OS command prompt. The system command does not return any data. |

**Note** : This command cannot be used while in
[safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**Examples**

Opens the text editor Notepad in windows.

```
 system("notepad");
```

The following example demonstrates how the system command can be used to get the
computer's date and time settings (wall-clock time), for example, to time stamp your
files. It is necessary to run a system command because the Lumerical script language
does not currently have a getDateAndTime scriptcommand. This example shows how to get
the time on a Windows machine, but it could easily be modified for other OS. The system
command is used to save the current time from the system clock into a file. The read
command is then used to read the time from the file.

```
fname="cur_time.txt";    # file name to store current time  

cmd="echo %time% >>" + fname; # system command to get current time and write to fname   

rm(fname);          # delete time file  

system(cmd);         # run command to get time and save to file  

cur_time=read(fname);     # read time from file  

?cur_time;             # current time: Hr, Min, Sec 
```

This example shows how to start a new instance of the Lumerical GUI from a script file
on a Windows computer. For example, if you have multiple Lumerical products, you may
find it useful to have one product (eg. CHARGE) be able to start a second product (eg.
FDTD). The following example will start a new instance of FDTD that runs the script file
runAnalysis.lsf.

Two variations of the command are provided. In the first, a new instance of FDTD
Solution is started and will run the script file runAnalysis.lsf. When this is executed,
the initial instance of the GUI (the one running the system command) will be frozen
while the new instance is running. The first instance will continue running once the
second instance is closed. Tip: you should add an 'exit' command to the end of the
runAnalysis.lsf script so the new instance automatically closes when it reaches the end
of the script.

The second variation allows the first instance of the GUI to continue running while the
second instance is open.

```
system('""C:\Program files\Lumerical\[[verpath]]\bin\fdtd-solutions.exe" -run "C:\temp\runAnalysis.lsf""');  

system('start "name" /B "C:\Program files\Lumerical\[[verpath]]\bin\fdtd-solutions.exe" -run "C:\temp\runAnalysis.lsf"');
```

The following code can be used on Windows OS to launch an FDTD simulation from the
terminal and then immediately close the graphical interface.

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

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ readdata ](./readdata.md) , [ exit ](./exit.md) , [ " ](./minus.md) ,
[ currentfilename ](./currentfilename.md)
