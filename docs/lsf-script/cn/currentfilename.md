<!--
Translation from English documentation
Original command: currentfilename
Translation date: 2026-02-03 10:51:43
-->

# currentfilename

返回当前项目文件名和目录。 

**Syntax** |  **Description**  
---|---  
out = currentfilename;  |  以字符串形式返回当前文件名。如果当前文件名未定义，则返回空字符串 "".   
  
**Examples**

Gets the current filename. 
    
    
    ?out=currentfilename;
    C:/Users/myname/Documents/FDTD/myfile.fsp

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [fileexists](../en/fileexists.md)
- [getpath](../en/getpath.md)
- [which](../en/which.md)
- [pwd](../en/pwd.md)
- [fileextension](../en/fileextension.md)
- [filebasename](../en/filebasename.md)
- [filedirectory](../en/filedirectory.md)
- [currentscriptname](../en/currentscriptname.md)
