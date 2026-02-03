# runsetup

Runsetup forces the setup scripts of structure and analysis groups to run. 

In most cases, it is not necessary to use this function, as group setup scripts automatically re-run at the end of script, if the object has been modified. It is only necessary to use this function when you need to force the setup script to run before the end of your script file. 

**Syntax** |  **Description**  
---|---  
runsetup;  |  Forces setup scripts of groups to run.   
  
**Examples**

We use the runsetup command to force the group setup script to run before the script is finished, This allows us to get the properties of a child of the group. 
    
    
    # Create a structure group. 
    deleteall;
    addstructuregroup;
    adduserprop("radius",2,0.5e-6);
    myscript =      "addcircle; \n";
    myscript = myscript + "copy(1e-6); \n";
    myscript = myscript + "selectall; \n";
    myscript = myscript + "set(\"radius\",radius);";
    set("name","dimer");
    set("script",myscript); 
    # Try to get the radius of the circle
    # objects within the group. This command will fail
    # without the runsetup function, which forces the 
    # group setup script to run.
    runsetup;
    ?getnamed("dimer::circle","radius");

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ get ](/hc/en-us/articles/360034928873-get) , [ set ](/hc/en-us/articles/360034928773-set) , [ runanalysis ](/hc/en-us/articles/360034409874-runanalysis)
