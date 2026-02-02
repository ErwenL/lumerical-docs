# fileexists

Checks if a file exists. The file extension (ie, .fsp, .lms, etc) must be specified. By default, the entire path will be searched. 

**Syntax** |  **Description**  
---|---  
out = fileexists("filename");  |  Returns 1 if the file exists  Returns 0 if the file does not exist.   
out = fileexists("c:\temp\file.txt");  |  Search for a file not in the path   
  
**Examples**

Checks if a file exists before opening it. 
    
    
    filename="simulation.fsp";
    if (fileexists(filename)) {
     load(filename);
    }

Load a simulation project file, if it exists. First check current directory, then check up one directory. 
    
    
    filename="simulation.fsp";
    if (fileexists(file)) {
     load(filename);
    } else {
     file = "../"+file;
     if (fileexists(file)) {
      load(filename);
     } else {
      ?"File not found.";
     }
    }

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getpath ](/hc/en-us/articles/360034411054-getpath) , [ which ](/hc/en-us/articles/360034411094-which) , [ pwd ](/hc/en-us/articles/360034931773-pwd) , [ load ](/hc/en-us/articles/360034410834-load) , [ loaddata ](/hc/en-us/articles/360034411214-loaddata) , [ write ](/hc/en-us/articles/360034411134-write) , [ readdata ](/hc/en-us/articles/360034411234-readdata) , [ currentfilename ](/hc/en-us/articles/360034931793-currentfilename) , [ rm ](/hc/en-us/articles/360034931533-rm) , [ exist ](/hc/en-us/articles/360034410914-exist)
