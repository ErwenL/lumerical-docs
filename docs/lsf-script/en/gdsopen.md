# gdsopen

This function creates a new .gds file and returns a file handle that can be used with the other GdsWriter functions to write the file. The default database units are in 0.1nm and the user units are microns. The GDSII export function works as a group of commands, shown below as an example. For more information, please see [GDSII - Import and export ](/hc/en-us/articles/360034901933-Import-and-export-GDSII) . All gds commands will check that the ratio coordinates/dataBaseUnit does not have a magnitude larger than \\( 2^{31} \\).

**Syntax** |  **Description**  
---|---  
f = gdsopen("filename", "userUnit", "dataBaseUnit") |  Opens a .gds file in the current directory, specifies the size of user units and size of the GDSII file units. f is a file handle to open the GDSII file.  
  
**Parameter** |  **Type** |  **Description**  
---|---|---  
filename |  string |  Name of the GDSII file to export, may also contain a file path.  
userUnit |  number |  Size of user units in GDSII file units.  
databaseUnit |  number |  Size of the GDSII file units in meters.  
  
## Example

This shows an example to export some simple structures to GDSII format via script code
    
    
    f=gdsopen('GDS_export.gds'); 
    # create a .gds file to write code. If the file exits, it will be overwritten.
    gdsbegincell(f,'cell_1');# create a cell named "cell_1"
    gdsaddcircle(f, 5, 0, 0, 1.5e-6);# add a circle
    gdsendcell(f);# finish "cell_1"
    gdsbegincell(f,'cell_2');# create another cell
    gdsaddpoly(f, 5, [0,0; 1.5,0; 1.2,1.3]*1e-6);# add a polygon 
    gdsaddcircle(f, 5, -3e-6, -3e-6, 1.5e-6);# add a circle 
    gdsaddrect(f, 5, -3e-6, 3e-6, 1e-6, 2e-6);# add a rectangle 
    gdsaddref(f, 'cell_1', 3e-6, -3e-6);
    # reference a structure from "cell_1"
    gdsendcell(f);# finish the current cell
    gdsclose(f);# close the current .gds file
    gdsimport('GDS_export.gds','cell_1', 5);
    # show the exported design in a layout environment

An example of script code is available on the webpage.

**See Also**

[ gdsclose ](/hc/en-us/articles/360034927113-gdsclose) , [ gdsbegincell ](/hc/en-us/articles/360034927133-gdsbegincell) , [ gdsendcell ](/hc/en-us/articles/360034406894-gdsendcell) , [ gdsaddpoly ](/hc/en-us/articles/360034927153-gdsaddpoly) , [ gdsaddcircle ](/hc/en-us/articles/360034406914-gdsaddcircle) , [ gdsaddrect ](/hc/en-us/articles/360034406934-gdsaddrect) , [ gdsimport ](/hc/en-us/articles/360034406974-gdsimport) , [ gdsaddref ](/hc/en-us/articles/360034927173-gdsaddref) , [ gdsaddpath ](/hc/en-us/articles/360034406954-gdsaddpath) , [ gdsaddtext](/hc/en-us/articles/360034927193-gdsaddtext), [gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
