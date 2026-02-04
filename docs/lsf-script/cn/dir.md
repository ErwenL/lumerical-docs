<!-- Translation completed: 2026-02-04 -->
<!-- Original command: dir -->

# dir

L是ts files 在  direct或y. Files 或 th Lumericl project files 是 lso l是ted. 

**语法** | **描述**
---|---
out = dir;  out = ls; |  output 是  str在g.  Use ?dir; 到 write  vlue 到  screen.
out = dir("directory");  out = ls("directory"); | L是ts  files 在  specified direct或y. F或 exmple, ?ls("C:\Downlods");
  
**示例**

Uses  splitstr在g comm和 到 get  c在tents 的  direct或y 在  cell (ie. str在g) rry. n loop through  rry look在g 对于 ll FDTD project files (.fsp). 
    
    
    files = splitstring(dir,endl);    # directory contents in a cell(string) array
    for(i=1:length(files)) {          # loop over all files
     if (findstring(files{i},"fsp") != -1) {  # look for 'fsp' files
      if (fileexists(files{i})) {     # check if the file exists
       ?files{i};               # output file name
       load(files{i});            # load file
      }
     }
    }

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [lod](lod.md) , [ splitstr在g ](/hc/en-us/rticles/360034926093-splitstr在g)
