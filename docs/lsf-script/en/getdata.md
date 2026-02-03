# getdata

Get raw data from a simulation object. In most cases, it is more convenient to get a complete dataset with [ getresult](/hc/en-us/articles/360034409854-getresult), rather than getting individual data elements with getdata.

Remember to run the simulation before using getdata.

For FDTD and MODE:

**Syntax** |  **Description**  
---|---  
?getdata; |  Returns names of all objects with data.  
?getdata("monitor") |  Returns list of of data within the simulation object.  
out = getdata( "monitor", "dataname"); |  Gets data from a monitor. For example, you can use

  * Ex = getdata("monitor1","Ex");

to get the Ex field data from monitor1.  
out = getdata( "monitor", "dataname", option); |  The optional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. For Propagator simulations in MODE, this options also allow users to choose whether to expand the data to the correct size for dimensions where the field component is zero. Option 1 will return a singleton value of 0 for the field component in that dimension, and option 2 will return a matrix (composed of zeros) that matches the size of the other field components.  
  
For CHARGE, HEAT, DGTD, FEEM:

**Syntax** |  **Description**  
---|---  
?getdata; |  Returns names of all objects with data.  
?getdata("monitor") |  Returns list of of results within the simulation object.  
?getdata( "monitor", "result"); |  Returns list of of data within the simulation object result.  
out = getdata( "monitor", "result", "dataname"); |  Gets the simulation data.  
  
For INTERCONNECT: The getdata command is available in INTERCONNECT for compatibility with other Lumerical products, but it's best to use the getresult script function to access INTERCONNECT simulation data.

**Examples**

This example shows how to use getdata to check which data is available.
    
    
    ?getdata;
    ?getdata("monitor");
    > monitor
    > source
    > 
    > x y z surface_normal dimension f Ex Ey Ez
    > Hx Hy Hz power 

Next, we use getdata to create a image plot of Ex(x,y). We also show how getresult can be used to create the same figure.
    
    
    # get raw data with getdata
    x=getdata("monitor","x");
    y=getdata("monitor","y");
    z=getdata("monitor","z");
    f=getdata("monitor","f");
    Ex=getdata("monitor","Ex");
    # select first frequency point of Ex data, then create plot
    ?size(Ex);
    Ex = pinch(Ex,4,1); 
    image(x*1e6,y*1e6,Ex,"x (um)","y (um)","Ex");
    # use getresult to get all of the E field data in a single command
    E=getresult("monitor","E");
    # select first frequency point of Ex data, then create plot
    ?size(E.Ex);
    Ex = pinch(E.Ex,4,1); # select first frequency point to plot
    image(E.x*1e6,E.y*1e6,Ex,"x (um)","y (um)","Ex"); 

Get a list of data in the 'Device region' object, then get the 'n' carrier concentration data.
    
    
    ?getdata("Device region");
    ?getdata("Device region","active");
    n=getdata("Device region","active","n");
    ?size(n);
    > active drain source
    > n p Ei Ec Ev Efn Efp log10(N) mun mup 
    > result: 
    >  2826 1 9 1 
    

**See Also**

[getresult](/hc/en-us/articles/360034409854-getresult), [havedata](/hc/en-us/articles/360034930213-havedata), [getelectric](/hc/en-us/articles/360034409974-getelectric), [getmagnetic](/hc/en-us/articles/360034930293-getmagnetic), [nonorm](/hc/en-us/articles/360034405434-nonorm), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [getsweepdata](/hc/en-us/articles/360034409794-getsweepdata), [getsweepresult](/hc/en-us/articles/360034409814-getsweepresult)
