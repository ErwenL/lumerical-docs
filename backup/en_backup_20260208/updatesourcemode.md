# updatesourcemode

Updates the mode profile of selected mode source. If there is no mode profile stored in the source, then the mode with the highest effective index will be selected. If a mode is already stored in the source, then the mode with the best overlap with the old mode will be selected. Note that the mode source must be selected before running this command.

**Syntax** |  **Description**  
---|---  
?updatesourcemode; |  Updates mode profile of the selected Mode source. Returns the fraction of electromagnetic fields that overlap between the old and the new mode  
?updatesourcemode(mode_number); |  Updates the mode source and selects the desired mode number. For example, updatesourcemode(1); will calculate the fundamental mode. Please note that making this call will force a recalculation of a mode, even if the same mode has previously been calculated. In addition, making this call will force the mode selection method to become "user select". This optional argument was introduced in FDTD 8.6.3 and MODE 6.5.3.  
NOTE: Saving simulation files before using updatesourcemode If you have a script file which updates the simulation mesh, then you should use the [save script command](/hc/en-us/articles/360034410814-save) before updating the source mode. This will ensure that the mesh has been updated before the new mode is calculated.  
---  
NOTE: overlap The fraction of electromagnetic fields that overlap between the two modes is given by the expression below. It is also the fraction of power from mode2 that can propagate in mode1. For more information, please see [overlap script command](/hc/en-us/articles/360034405254-overlap). $$ \text { overlap }=\operatorname{Re}\left[\frac{\left(\int \vec{E}_{1} \times \vec{H}_{2}^{*} \cdot d \vec{S}\right)\left(\int \vec{E}_{2} \times \vec{H}_{1}^{*} \cdot d \vec{S}\right)}{\int \vec{E}_{1} \times \vec{H}_{1}^{*} \cdot d \vec{S}}\right] \frac{1}{\operatorname{Re}\left(\int \vec{E}_{2} \times \vec{H}_{2}^{*} \cdot d \vec{S}\right)} $$  
---  
  
**Example**

Select the source, then update the mode profile. Once the mode profile has been updated, output the mode effective index and visualize the mode field profile.
    
    
    # update the source mode profile  
    select("source");  
    updatesourcemode;  
    
    # get the mode profile and effective index  
    n=getresult("source","neff");  
    ?"Effective index = " + num2str(n.neff);  
    field=getresult("source","mode profiles");  
      
    visualize(field);

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [addmode](/hc/en-us/articles/360034924353-addmode), [clearsourcedata](/hc/en-us/articles/360034929093-clearsourcedata), [clearmodedata](/hc/en-us/articles/360034408774-clearmodedata), [getresult](/hc/en-us/articles/360034409854-getresult), [overlap](/hc/en-us/articles/360034405254-overlap), [expand](/hc/en-us/articles/360034926653-expand), [seteigensolver](/hc/en-us/articles/360034929113-seteigensolver), [geteigensolver](/hc/en-us/articles/360034408794-geteigensolver), [updatemode](/hc/en-us/articles/360034929073-updatemodes), [updateportmodes](/hc/en-us/articles/360034409174-updateportmodes)
