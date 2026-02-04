<!--
Translation from English documentation
Original command: dir
Translation date: 2026-02-04 22:49:48
-->

# dir

Lists files 在 一个 directory. Files other than Lumerical project files 是 also listed. 

**语法** |  **描述**  
---|---  
out = dir;  out = ls;  |  The output 是 一个 字符串.  Use ?dir; 到 write 该 值 到 该 screen.   
out = dir("directory");  out = ls("directory");  |  Lists 该 files 在 该 specified directory. For example, ?ls("C:\Downloads");   
  
**示例**

Uses 该 splitstring 命令 到 获取 该 contents 的 一个 directory 在 一个 单元格 (ie. 字符串) 数组. Then loop through 该 数组 looking 用于 all FDTD project files (.fsp). 
    
    
    files = splitstring(dir,endl);    # directory contents 在 一个 单元格(字符串) 数组
    用于(i=1:长度(files)) {          # loop over all files
     如果 (findstring(files{i},"fsp") != -1) {  # look 用于 'fsp' files
      如果 (fileexists(files{i})) {     # check 如果 该 文件 exists
       ?files{i};               # output 文件 name
       load(files{i});            # load 文件
      }
     }
    }

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ load ](/hc/en-us/articles/360034410834-load) , [ splitstring ](/hc/en-us/articles/360034926093-splitstring)
