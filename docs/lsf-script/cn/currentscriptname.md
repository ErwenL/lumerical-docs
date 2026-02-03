<!--
Translation from English documentation
Original command: currentscriptname
Translation date: 2026-02-03 10:53:20
-->

# currentscriptname

返回当前脚本文件名和目录。 

**Syntax** |  **Description**  
---|---  
out = currentscriptname;  |  以字符串形式返回当前脚本文件名。如果在脚本提示符中输入，则返回字符串 "prompt".   
  
**Examples**

获取当前脚本文件名。 
    
    
    ?out=currentscriptname;
    C:/Users/myname/Documents/FDTD/myfile.lsf

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [fileexists](../en/fileexists.md)
- [getpath](../en/getpath.md)
- [which](../en/which.md)
- [pwd](../en/pwd.md)
- [fileextension](../en/fileextension.md)
- [filebasename](../en/filebasename.md)
- [filedirectory](../en/filedirectory.md)
- [currentfilename](../en/currentfilename.md)
