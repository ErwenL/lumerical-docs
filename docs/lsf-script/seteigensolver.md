# seteigensolver

Mode sources, mode expansion monitors, and ports in FDTD and MODE, and each individual cell in EME have embedded eigensolvers. This script command makes it possible to set the properties of that eigensolver without using the GUI.

Changing any values of the embedded eigensolver with this command will automatically invalidate any existing mode data. This means that new updates based on overlap calculations with previous modes will fail after using this command. Therefore please call this command before making any calls to updatesourcemode or updatemodes.

**Syntax** |  **Description**  
---|---  
?seteigensolver; |  Returns a list of the properties of the embedded eigensolver  
seteigensolver("property",value); |  This will set the eigensolver properties of the currently selected objects. Value can be a number or string. This function does not return any data.  
  
**Example**

  1. Change the radius of curvature for a mode expansion calculation, and calculate the first 10 modes which can be subsequently used for mode expansion. Please open  ring_resonator2.lms  from the [ ring resonator example ](**%20to%20be%20defined%20**) using the varFDTD solver in MODE:


    
    
    select("expansion");
    
    
    seteigensolver("bent waveguide",true);
    seteigensolver("bend radius",10e-6);
    updatemodes(1:10);

2\. Change the number of trial modes for cell 1 in EME:
    
    
    select("EME::Cells::cell_1");  
    seteigensolver("number of trial modes",25);

Also see the examples in the [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) , and [ addport ](/hc/en-us/articles/360034924793-addport) script functions.

**See Also**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ addmode ](/hc/en-us/articles/360034924353-addmode) , [ addmodeexpansion ](/hc/en-us/articles/360034924573-addmodeexpansion) , [ addport ](/hc/en-us/articles/360034924793-addport) , [ clearsourcedata ](/hc/en-us/articles/360034929093-clearsourcedata) , [ clearmodedata ](/hc/en-us/articles/360034408774-clearmodedata) , [ clearportmodedata ](/hc/en-us/articles/360034409194-clearportmodedata) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ geteigensolver ](/hc/en-us/articles/360034408794-geteigensolver) , [ updatemodes ](/hc/en-us/articles/360034929073-updatemodes) , [ updatesourcemode ](/hc/en-us/articles/360034408754-updatesourcemode) , [ updateportmodes ](/hc/en-us/articles/360034409174-updateportmodes)
