<!--
Translation from English documentation
Original command: splitstring
Translation date: 2026-02-04 22:50:15
-->

# splitstring

Splits 一个 long 字符串 into 一个 series 的 substrings, 其中 该 substrings 是 stored 在 一个 单元格 (i.e., 字符串) 数组. 

**语法** |  **描述**  
---|---  
s2 = splitstring(s1,endl);  |  Split 该 字符串 S1 into 一个 series 的 strings, 使用 该 end 的 line character as 该 delimiter between strings. S2 是 一个 单元格 数组.   
  
**示例**

Use 该 splitstring 命令 到 获取 该 contents 的 一个 directory 在 一个 单元格 (i.e., 字符串) 数组. Then loop through 该 数组 looking 用于 all FDTD project files (.fsp). 
    
    
    files = splitstring(dir,endl);        # directory contents 在 一个 单元格 (字符串) 数组
    用于(i=1:长度(files)) {           # loop over all files
     如果 (findstring(files{i},"fsp") != -1) {  # look 用于 'fsp' files
      如果 (fileexists(files{i})) {       # check 如果 该 文件 exists (ie. it's 一个 文件 和 not 一个 directory)
       ?files{i};               # output 文件 name
       load(files{i});            # load 文件
      }
     }
    }

A similar example 用于 getting 该 names 的 all monitors 在 一个 仿真. Loop through all monitors, checking 如果 they contain 一个 result named 'E'. If so, save 该 数据 到 一个 文件. 
    
    
    mNames = splitstring(getresult,endl);
     
    用于 (i=1:长度(mNames)) {
     如果 (haveresult(mNames{i},"E")) {
      E=getresult(mNames{i},"E");   # 获取 一个 result 从 该 监视器
     } 否则 {
      E = mNames{i} + " did not contain 该 specified 数据.";
     }
     文件名 = "文件"+num2str(i);
     savedata(文件名,E);     # save 数据 到 ldf files
    }

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 长度 ](/hc/en-us/articles/360034925653-长度) , [ substring ](/hc/en-us/articles/360034926033-substring) , [ findstring ](/hc/en-us/articles/360034405954-findstring) , [ replace ](/hc/en-us/articles/360034926053-replace) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ 单元格 ](/hc/en-us/articles/360034929913-单元格) , [ dir ](/hc/en-us/articles/360034410854-dir) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
