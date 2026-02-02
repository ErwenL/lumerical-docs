# runstartupscripts

Runs the start-up scripts.

**Syntax** |  **Description**  
---|---  
runstartupscripts; |  Runs the start-up scripts in the order of:

  1. global shared startup script
  2. global $(PRODUCT) startup script
  3. local shared start-up script
  4. local $(PRODUCT) start-up script

  
  
**Examples**

The following examples runs the "runstartupscripts" in INTERCONNECT with the scripts in "Shared Startup.lsf" and "INTERCONNECT Startup.lsf" as below, respectively:
    
    
    # Shared Startup.lsf
    clear;
    ?a = 1;
    # INTERCONNECT Startup.lsf
    clear;
    ?b = 2;

The output result:
    
    
    runstartupscripts;
    Shared Startup;
    result: 
    1  
    Running script: /Users/$(Username)/.config/Lumerical/INTERCONNECT Startup.lsf
    INTERCONNECT Startup;
    result: 
    2  

**See Also**

[ List of commands](/hc/en-us/articles/360037228834), [ feval](/hc/en-us/articles/360034405934-feval)
