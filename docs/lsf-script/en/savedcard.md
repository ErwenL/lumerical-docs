# savedcard

Saves d-card data to a Lumerical data file (ldf) file. D-cards are generally used to store monitor data, but can also be used to store data from solver objects.

Data is saved in the nonorm state. See the [ units and normalization ](https://optics.ansys.com/hc/en-us/articles/360034397034) section of the reference guide for more information.

**Syntax** |  **Description**  
---|---  
savedcard("filename"); |  Saves all current d-cards (local and global) to the specified ldf file. This function does not return any data.  
savedcard("filename", "name1", "name2",...); |  Saves only the d-cards with the specified names, "name1", "name2", etc.  
  
**Examples**

This example shows how to save all data from the monitor named xy_monitor.
    
    
    ?getdata; # view all d-cards
    savedcard("monitor_data","::model::xy_monitor");

This example shows how to save the required data after performing a frequency sweep in MODE. This is equivalent to the GUI option "Export for Interconnect".
    
    
    savedcard("FileName", "::model::FDE::data::frequencysweep");

**See Also**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ copydcard ](https://optics.ansys.com/hc/en-us/articles/360034930233-copydcard) , [ savedata ](https://optics.ansys.com/hc/en-us/articles/360034411174-savedata) , [ loaddata ](https://optics.ansys.com/hc/en-us/articles/360034411214-loaddata) , [ matlabsave ](https://optics.ansys.com/hc/en-us/articles/360034928113-matlabsave)
