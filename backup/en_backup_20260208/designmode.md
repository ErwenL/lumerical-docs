# designmode

In INTERCONNECT, this script command can be used to determine whether the simulation file is currently in DESIGN mode or in ANALYSIS mode. It is important to use this command to check the status of the project file once it is opened to avoid running into an error during the subsequent operations if the file is not in the desired mode. 

**Syntax** |  **Description**  
---|---  
?designmode;  |  Returns 1 if in DESIGN mode, and 0 if in ANALYSIS mode.   
  
**Example**

The following script commands will first load a project file named "test.icp". The aim of the script is to add a new optical oscilloscope to the existing circuit. However, if the file is in ANALYSIS mode then the "addelement" command will create an error. To avoid this, the script command "designmode" is first used to determine the status of the file. Then an "if/else" statement is used to add the element directly if the file is already in DESIGN mode or to add the element after switching to DESIGN mode first if the file is in ANALYSIS mode. 
    
    
    load("test.icp");
    status = designmode;
    if (status == 1) {
        addelement("Optical Oscilloscope");
    }
    else {
        switchtodesign;
        addelement("Optical Oscilloscope");
    }

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ switchtolayout ](/hc/en-us/articles/360034923993-switchtolayout) , [ layoutmode ](/hc/en-us/articles/360034924033-layoutmode) , [ switchtodesign ](/hc/en-us/articles/360034924013-switchtodesign)
