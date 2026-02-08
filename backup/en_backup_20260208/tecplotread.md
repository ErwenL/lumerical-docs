# tecplotread

Imports data from Tecplot formatted file (text).

**Syntax** |  **Description**  
---|---  
? tecplotread('filename.dat'); |  List all zones ( domains) in the data file.  
? tecplotread('filename.dat','zonename'); |  List all of the data fields associated with the zone.  
out = tecplotread('filename.dat','zonename','dataname'); |  Retrieve the data as an array  
  
**Example**

The following example shows how the tecplotread command can be used to import data from these files into CHARGE. Special field “FETriangle” represents the triangulation and X and Y coordinates of mesh are treated as node data. Names and units depend on original data source but we must convert units to SI (m). 

The first part of the tecplot_import_diode.lsf file reads the data from the example_diode_tecplot.dat file. The following two lines in the script reads in the names of the zones and the data available in the zones of the tecplot file. 
    
    
    filename = 'example_diode_tecplot.dat';  
    zonename = 'Silicon';  
    ?"Available zones: " + tecplotread(filename);  
    ?"Data in zone " + zonename + ": " + tecplotread(filename,zonename);

The next few lines read in the information about the finite element grid. Here t is the connectivity matrix and x, y are the vertex matrices. Notice the coordinate data is converted from units of micron to meter.
    
    
    t = tecplotread(filename,zonename,'FETriangle');  
    x = 1e-6*tecplotread(filename,zonename,'X [um]'); # convert to SI from um to m  
    y = 1e-6*tecplotread(filename,zonename,'Y [um]'); # convert to SI, invert

The following lines then read the doping data.
    
    
    NA_name = 'NA [1/cm3]';  
    ND_name = 'ND [1/cm3]';  
    NA = 1e6*tecplotread(filename,zonename,NA_name); # convert to SI (cm^-3 -- m^-3)  
    ND = 1e6*tecplotread(filename,zonename,ND_name); # convert to SI (cm^-3 -- m^-3)

After reading the data, the code creates unstructured datasets for the doping data and creates geometries and import doping objects. The same task can be performed using the [Dataset builder](/hc/en-us/articles/360034901713-Dataset-builder) in CHARGE once the data has been imported.

**See Also**

[system](/hc/en-us/articles/360034410894-system), [matlabload](/hc/en-us/articles/360034408034-matlabload), [h5read](/hc/en-us/articles/360034407214-h5read)
