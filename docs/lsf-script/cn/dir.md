<!--
Translation from English documentation
Original command: dir
Translation date: 2026-02-03 23:07:24
-->

# dir

列出目录中的文件。Lumerical项目文件以外的文件也会列出。 

**Syntax** |  **Description**  
---|---  
out = dir;  out = ls;  |  输出为字符串。使用?dir;将值写入屏幕。   
out = dir("directory");  out = ls("directory");  |  列出指定目录中的文件。例如，?ls("C:\Downloads");   
  
 **示例**

 使用splitstring命令获取目录内容，存储在cell（即字符串）数组中。然后遍历数组查找所有FDTD项目文件（.fsp）。
    
    
    files = splitstring(dir,endl);    # directory contents in a cell(string) array
    for(i=1:length(files)) {          # loop over all files
     if (findstring(files{i},"fsp") != -1) {  # look for 'fsp' files
      if (fileexists(files{i})) {     # check if the file exists
       ?files{i};               # output file name
       load(files{i});            # load file
      }
     }
    }

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [load](./load.md)
- [splitstring](./splitstring.md)
