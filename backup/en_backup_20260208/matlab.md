# matlab

Runs a MATLAB command from the Lumerical script prompt. This gives access to extended mathematical and visualization functionality from the Lumerical script environment. If the MATLAB script integration is not enabled, this function will return an error. 

The first time a MATLAB function (matlab, matlabget or matlabput) is called, a MATLAB session will be started and a connection will be established with the Lumerical scripting environment. Once this connection is established, MATLAB commands can be run using the matlab function. It is important to understand that the MATLAB and the Lumerical script variable workspaces are completely separate and independent. A MATLAB command cannot act on a variable defined in the Lumerical workspace, and vice-versa. Variables must be passed between the workspaces using the matlabget and matlabput functions. At any time you may examine the MATLAB workspace or interact with the MATLAB environment by typing commands at the MATLAB script prompt. The working directory of the MATLAB instance is always set to match the working directory of the Lumerical application. 

The output from the MATLAB commands will be printed at the Lumerical script prompt. One limitation of the matlab function is that no error reporting is provided to either the Lumerical script prompt or the MATLAB prompt. MATLAB commands should be tested by typing them directly into the MATLAB prompt before they are called from a Lumerical script. The output buffer length is roughly 1e5 characters. Additional output will be truncated. 

When you have a long sequence of MATLAB commands, you may find it more convenient to save them in a MATLAB m-file. Then, you can simply call the m-file by running a single command. 

See [ MATLAB integration setup ](/hc/en-us/articles/360026142074) for installation and configuration instructions. Additional tips (particularly for plotting data in Matlab) can be found in the [ MATLAB ](/hc/en-us/articles/360034416614) section of the online help.   
---  
**Syntax** |  **Description**  
---|---  
matlab("command");  |  command: a string containing one or more valid MATLAB commands.   
matlab("  command_1  command_2  ");  |  Multi-line strings can be used in script files to contain a block of MATLAB commands. Multi-line strings are not supported at the script command prompt.   
  
**Examples**

This example will show how to use MATLAB's "surf" command to make a surface plot of the real part of Ex. It assumes that the variables x, y, Ex are already defined in the Lumerical workspace. 
    
    
    matlabput(x,y,Ex);
    matlab("surf(y,x,real(Ex))");

This example shows how multiple MATLAB commands can be included in a single matlab function call. A log-spaced vector is created in MATLAB, then imported into the Lumerical workspace. 
    
    
    matlab("
     % create a logspaced vector
     x_min = 1
     x_max = 4
     x = logspace(x_min,x_max,1000)
    ");
    matlabget(x);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ matlabget ](/hc/en-us/articles/360034407994-matlabget) , [ matlabput ](/hc/en-us/articles/360034408014-matlabput) , [ MATLAB integration setup ](/hc/en-us/articles/360026142074) , [ MATLAB ](/hc/en-us/articles/360034416614)
