# farfieldsettings

Sets the parameters available in the Far field settings window for far field calculations. To get the available parameters for far field settings, as is shown below, right click on a frequency-domain field monitor and visualize the far field. then select the Far field settings.   
  
---  
**Syntax** |  **Description**  
---|---  
farfieldsettings("property", value);  |  Set the far field filter settings for far field calculations. These settings are applied to all far field projections.  Value can be a number or string. This function does not return any data.   
  
**Example**
    
    
    farfieldsettings("far field filter",0.2);farfieldsettings("override near field mesh",1);
    farfieldsettings("near field samples per wavelength",5);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldfilter ](/hc/en-us/articles/360034930613-farfieldfilter) , [ setanalysis ](/hc/en-us/articles/360034925113-setanalysis) (for farfield settings in FDE) 
