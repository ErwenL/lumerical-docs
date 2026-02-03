# mapfind

Returns the nearest value from a file containing a map of values. It returns the string value located at the specified nearest point. 

**Syntax** |  **Description**  
---|---  
out = mapfind (filename,x,y);  |  Find the nearest value from a file containing a map of values. It returns the string value located at the nearest point (x,y).   
out = mapfind (filename,x,y,z);  |  Find the nearest value from a file containing a map of values. It returns the string value located at the nearest point (x,y,z).   
out = mapfind (filename,x,y,z,w);  |  Find the nearest value from a file containing a map of values. It returns the string value located at the nearest point (x,y,z,w).   
  
**Example**

Load the effective index associated to a given waveguide width and height from a text file in the current working directory. The file contains the effective index for different values of width and height, separated by “,”. For example: 

width, height, neff 

4.9e-007,2.1e-007,2.38997 

4.9e-007,2.12222e-007,2.39885 

4.9e-007,2.14444e-007,2.40796 

4.9e-007,2.16667e-007,2.41618 

The first row contains the column headers (optional), and the next four rows contain data. The command mapfind is used as follows: 
    
    
    # Width and height we are looking for:
    waveguide_width = 4.9e-007;
    waveguide_height = 2.1e-007;
    # Find the effective index of the closest width-height combination (value is returned as a string):
    sneff = mapfind( "neff_map.txt", waveguide_width, waveguide_height );
    #convert the string sneff to a value
    ?neff = str2num(sneff);
    result: 
    2.38997  

**See Also**

[ read ](/hc/en-us/articles/360034931933-read) , [ readdata ](/hc/en-us/articles/360034411234-readdata)
