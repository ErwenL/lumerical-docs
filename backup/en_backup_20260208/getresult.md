# getresult

Get results from simulation objects. Results will be returned as datasets.

**Syntax** |  **Description**  
---|---  
?getresult("monitor_name"); |  Returns the names of all the results for the monitor. All the dataset and scalar matrix results will be returned in this case.  
R = getresult("monitor_name","T"); |  Returns the result T from the monitor. T is a dataset.  
  
**Examples**

This example shows how to get the electric field dataset from a monitor. We then apply a number of operations to the dataset, such as finding the maximum |E|^2 value, viewing the dataset with the visualizer, and creating a plot of Ex at the first frequency point.

Note that E is a dataset, rather than a simple matrix based variable. Data within the dataset can be accessed with the '.' operator, as shown below.
    
    
    # get Electric field dataset
    E=getresult("monitor","E");
    # output dataset value to prompt
    ?E;
    # check size of position vectors and data matrices
    ?size(E.f);
    ?size(E.Ex);
    # find maximum |E|^2 value 
    ?max(E.E2);
    # view dataset with visualizer
    visualize(E);
    # select first frequency point of Ex data, then create plot
    Ex = pinch(E.Ex,4,1); 
    image(E.x*1e6,E.y*1e6,Ex,"x (um)","y (um)","Ex");
     E vs x, y, z, lambda/f
     result: 
     5 1 
     result: 
     343 255 1 5 
     result: 
     3.223651 

**See Also**

[ List of commands](/hc/en-us/articles/360037228834), [ haveresult](/hc/en-us/articles/360034409894-haveresult), [ Dataset introduction](/hc/en-us/articles/360034409554-Datasets), [ "." operator](/hc/en-us/articles/360034925773-dot), [ visualize](/hc/en-us/articles/360034410514-visualize), [ getdata](/hc/en-us/articles/360034409834-getdata), [ rectilineardataset](/hc/en-us/articles/360034409474-rectilineardataset), [ matrixdataset](/hc/en-us/articles/360034409454-matrixdataset), [ getattribute](/hc/en-us/articles/360034409534-getattribute), [ addattribute](/hc/en-us/articles/360034409494-addparameter), [ splitstring ](/hc/en-us/articles/360034926093-splitstring)
