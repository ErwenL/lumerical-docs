# setpsfoutput

Specifies the location of the PSF folder and avoids using the netlist location as a reference in the co-simulation. 

By default, INTERCONNECT uses the netlist path to create the PSF path. The  setpsfoutput  command allows the users to specify a location of the PSF folder instead of using the default netlist path. 

**Syntax** |  **Description**  
---|---  
setpsfoutput("path")  |  Specifies the location of the PSF folder.   
  
**Example**

The following script command will import netlist, save file and save output data to a PSF folder in 3 different locations. 
    
    
    static const char* InitScript =
    "new;"
    "historyoff;"
    "setpsfoutput(\"%path3%\");
    "importnetlist(\"%path1%\");"
    "save(\"%path2%\");"
    "edacosimulation;"
    "setnamed('::Root Element','simulation output','psf');"
    "runinitialize;";

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ stlimport ](/hc/en-us/articles/360034924733-stlimport)
