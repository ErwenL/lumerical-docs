# matlabsave

## Notes

  * Starting with Lumerical 2024 R1, MATLAB Linux libraries are no longer packaged with the Lumerical Applications
  * We still support MATLAB file load and save for versions 7 and greater
  * See this [KB for more information](https://optics.ansys.com/hc/en-us/articles/360026142074#toc_3). 



Save Lumerical workspace variables to MATLAB .mat data files.

**Syntax** |  **Description**  
---|---  
matlabsave(""); |  Save all workspace variables to a .mat file that has the same name as the simulation file. This function does not return any data.  
matlabsave("filename"); |  Saves all workspace variables to the specified .mat file.  
matlabsave("filename", var1, ..., varN); |  Saves the specified workspace variables to the .mat file.  
  
**Examples**

Simple example:
    
    
    x=1:10;
    y=x^2;
    matlabsave("x_squared_data", x, y);

Save data from a monitor named xy_monitor. The data is first obtained with script functions such as getdata and transmission. These workspace variables are then saved with the matlabsave function. Note that complex file names can be created with the num2str command. This is useful when doing parameter sweeps where a unique file name is required for each point in the sweep.
    
    
    # get raw matrix data from the simulation
    mname="xy_monitor";       # monitor name
    x=getdata(mname,"x");      # position vectors associated with Ex fields
    y=getdata(mname,"y");      # position vectors associated with Ex fields
    Ex=getdata(mname,"Ex");     # Ex fields at monitor
    T=transmission(mname);     # Power transmission through monitor
     
    # save matrix variables x, y, Ex, T and i to a data file
    i=1;
    filename="results_"+num2str(i); # set filename. i could be a loop counter variable.
    matlabsave(filename, x,y,Ex,T,i); 

Save a Lumerical dataset (eg. Electric field vs x,y,z,f) to a .mat file. Lumerical datasets will be imported into Matlab using the struct data type.
    
    
    # get electric field dataset from the simulation
    mname="xy_monitor";       # monitor name
    E=getresult(mname,"E");     # E fields at monitor
     
    # save dataset to mat file
    filename="ElectricField";
    matlabsave(filename, E); 

**See Also**

[MATLAB](https://optics.ansys.com/hc/en-us/articles/360034923913-MATLAB-script-integration)[ script integration – Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360034923913-MATLAB-script-integration)

[matlabput](https://optics.ansys.com/hc/en-us/articles/360034408014-matlabput), [matlabsavelegacy](https://optics.ansys.com/hc/en-us/articles/360034928133-matlabsavelegacy), [matlabload](https://optics.ansys.com/hc/en-us/articles/360034408034-matlabload), [vtksave](https://optics.ansys.com/hc/en-us/articles/360034411354-vtksave)
