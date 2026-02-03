# debug

Opens the debug utility window. This command is useful for debugging purposes. When this command is used, script will run to the line before the  debug  command. Then user can start to call other commands to test commands that have been run. Once the utility window is closed, the script lines will continue to run. Multiple  debug  commands are allowed. 

**Syntax** |  **Description**  
---|---  
debug;  |  Opens the debug utility window. This command can also be used in the analysis script.   
  
**Examples**

This example shows how to use the  debug  command. This below example shows an error on line 3. 
    
    
    x=linspace(1,10,10);
    y=linspace(1,10,5);
    ?x*y;
    Error: prompt line 3: matrix arguments of * are not the same size
    x=linspace(1,10,10);
    y=linspace(1,10,5);
    debug; # opens the debug utility window.
    ?x*y;

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834)
