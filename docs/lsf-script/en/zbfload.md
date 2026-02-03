# zbfload

Loads data from Zemax zbf file into a d-card called "zbf_data". If "zbf_data" already exists in the deck, it will be called "zbf_data_2". After loading a zbf file with zbfload command, you can extract any of the following data: 

• Ex, Ey, Ez, Hx, Hy, Hz, x, y, z 

• frequency, wavelength, index 

Note that the H fields are calculated during the load operation in Lumerical tools using the index from the original zbf file. Similarly, the longitudinal component in direction of propagation is not supported by the zbf format and it is populated with zero values during the load operation. 

**Syntax** |  **Description**  
---|---  
zbfload  |  Select the file to load with the file browser.  This function does not return any data.   
zbfload("filename");  |  Loads data from a zbf file called "filename" without a file browser.   
zbfload("filename", propagation axis)  |  Loads data from a zbf file called "filename" without a file browser for a specified propagation axis. The propagation axis is an integer value that indicates the x, y and z axis.   
zbfload("filename", propagation axis, offset);  |  Loads data from a zbf file called "filename" without a file browser for a specified propagation axis with the specified offset. The offset is a floating number array that indicates the x, y and z coordinates shift of the load-in data to the original data.   
  
###  Example 

We have data from Zemax saved in a file named "myZemaxBeam.zbf". We use zbfload command to load the Zemax data into FDE deck for further analysis using Lumerical tools. 
    
    
    zbfload("myZemaxBeam.zbf");
    ?getdata;
     ::zbf_data
    ?getdata("zbf_data");
     f  wavelength  index  x  y  z  Ex  Ey  Ez
     Hx  Hy  Hz 
    Ex = getdata("zbf_data","Ex");
    x = getdata("zbf_data","x"); 
    y = getdata("zbf_data","y"); 
    image(x,y,pinch(real(Ex)));

Result of zbfload operation in Eigensolver Analysis window: 

We have data from Zemax saved in a file named "myZemaxBeam.zbf". We use zbfload command to load the Zemax data twice, the first time without offset and the second time with the [x, y, z] offset as [1e-7, 3e-7, 0]. 
    
    
    zbfload("myZemaxBeam.zbf");
    Ex = getdata("zbf_data", "Ex");
    x = getdata("zbf_data", "x");
    y = getdata("zbf_data", "y");
    image(x, y, pinch(real(Ex)));

The load in E field of zbf_data: 
    
    
    offset = [0.0000001, 0.0000003, 0];
    zbfload("myZemaxBeam.zbf", 3, offset);
    Ex = getdata("zbf_data", "Ex");
    x = getdata("zbf_data", "x");
    y = getdata("zbf_data", "y");
    image(x, y, pinch(real(Ex)));

The load in E field of zbf_data with offset: 

**See Also**

[ zbfexport ](/hc/en-us/articles/360034928253-zbfexport) , [ zbfread ](/hc/en-us/articles/360034408154-zbfread) , [ zbfwrite ](/hc/en-us/articles/360034928293-zbfwrite) , [ List of commands ](/hc/en-us/articles/360037228834)
