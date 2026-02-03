# try

Allows the execution of the script to continue even though an error occurs within a block. 

**Syntax** |  **Description**  
---|---  
try {  Command1;  Command2;  ...  }  |  Runs the block of commands. If an error occurs, the error message is displayed and the script continues.   
try {  Command1;  Command2:  ...  } catch(errMsg);  |  Runs the block of commands. If an error occurs, the error message is stored in the variable "errMsg" and the script continues.   
  
**Examples**

An error message will be displayed, but the script will continue: 
    
    
    a=1;
    try {
     ?C;
    }
    ?a;
    Error: prompt line 3: C is not a valid function or variable name
    Result:
    1

No error message will be displayed, but it will be stored in the variable errMsg: 
    
    
    a=1;
    try {
     ?C;
    } catch(errMsg);
    ?a;
    ?errMsg;
    Result:
    1
    Error: prompt line 3, C is not a valid function or variable name

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ if ](/hc/en-us/articles/360034408294-if)
