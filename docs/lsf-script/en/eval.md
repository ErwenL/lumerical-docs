# eval

Executes a string containing Lumerical's scripting language. 

**Syntax** |  **Description**  
---|---  
eval(string);  |  Executes the Lumerical script commands in string.  This function does not return any data.   
  
**Example**

Execute a string as a command. 
    
    
    eval("x=1+2;");
    ?x;
    3

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ feval ](/hc/en-us/articles/360034405934-feval) , [ str2num ](/hc/en-us/articles/360034405914-str2num) , [ num2str ](/hc/en-us/articles/360034925993-num2str) , [ lower ](/hc/en-us/articles/360034405974-lower) , [ upper ](/hc/en-us/articles/360034926113-upper) , [ toscript ](/hc/en-us/articles/360034405994-toscript)
