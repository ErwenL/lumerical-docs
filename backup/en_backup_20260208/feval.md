# feval

Evaluates a string as script file. This function is useful for running script files that are not in your path and files with spaces in the name. 

**Syntax** |  **Description**  
---|---  
feval(filename);  |  Execute string containing the name of a script file.  This function does not return any data.   
  
**Example**

Run the script file C:\temp\example.lsf. 
    
    
    feval("C:\temp\example.lsf");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ eval ](/hc/en-us/articles/360034926013-eval) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
