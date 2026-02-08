# scriptautorun

Disable or enable running script files automatically by typing the script name.

**Syntax** |  **Description**  
---|---  
scriptautorun(option); |  The options are

  * 0: disables automatic running of script files
  * 1: enables automatic running of script files

  
  
**Examples**

The following examples assume you have created a script file called hello_world.lsf that prints the message "hello". You will get the error message "Error: prompt line 3: hello_world is not a valid function or variable name" when running the following commands because scriptautorun is disabled.
    
    
    clear;
    scriptautorun(0); #disable autorun
    hello_world;

When you enable scriptautorun the script file is executed and the message "hello" will appear in the script prompt.
    
    
    clear;
    scriptautorun(1); #enable autorun
    hello_world;

If scriptautorun is disabled you can still run script files using the function feval.
    
    
    clear;
    scriptautorun(0); #disable autorun
    feval("hello_world");

**See Also**

[ List of commands](/hc/en-us/articles/360037228834), [ feval](/hc/en-us/articles/360034405934-feval)
