# zbfexport

Exports data from a frequency field or field and power monitor to Zemax *.zbf file. This command can be also used to export data from a d-card to Zemax file. The return value of this command is the origin (x, y and z coordinates) of the monitor exported to the *.zbf file.

**Syntax** |  **Description**  
---|---  
output = zbfexport("monitorname"); |  Export data from monitorname. By default, the first frequency point is exported. This function returns the origin of the monitor exported to the *.zbf file, in the format of an array with the x, y and z coordinates of the monitor origin.  
zbfexport("monitorname",f); |  Exports the frequency point specified by the index f.  
zbfexport("monitorname",f,"filename"); |  Exports to the specified "filename" without opening the file browser window.  
[[Note:]] The Zemax zbf file requires the data to be saved on a uniform grid of dimensions with a power of 2 (with \\(2^n \times 2^m\\) points). The dataset will be interpolated on a grid with \\(n\\) and \\(m\\) defined so the mesh step is equal to or less than the smallest mesh step in the original data.  
---  
  
### Example #1

Export data from monitor "beam_profile" to a .zbf file for Zemax. The monitor had more than one frequency point, so we elected to export the third frequency point.
    
    
    ?zbfexport("beam_profile",3,"test_export.zbf");
    result:
    1e-07
    3e-07
    0

### Example #2

Export data from dcard named "global_mode1" to a .zbf file for Zemax. The d-card has one frequency point, so we use f index =1.
    
    
    zbfexport("global_mode1",1,"testfileDcard.zbf");

**See Also**

[ zbfload ](/hc/en-us/articles/360034928273-zbfload) , [ zbfread ](/hc/en-us/articles/360034408154-zbfread) , [ zbfwrite ](/hc/en-us/articles/360034928293-zbfwrite) , [ List of commands ](/hc/en-us/articles/360037228834)
