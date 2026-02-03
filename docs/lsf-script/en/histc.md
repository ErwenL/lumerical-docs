# histc

Creates a histogram plot. 

**Syntax** |  **Description**  
---|---  
out = histc(y);  |  Creates a histogram plot of y.  Returns the figure number.   
histc(y,n);  |  Creates a histogram plot of y, using n bins.  Returns the figure number.   
histc (y,n, "x label", "y label", "title");  |  Creates a histogram plot of y, using n bins, with axis labels and a title.  Returns the figure number.   
  
**Example**

These are scripts for creating simple histograms. 
    
    
    #Creates a histogram plot of y.
    y = randmatrix(1,10);
    y = y*10;
    out = histc(y);
    #Creates a histogram plot of y, using n bins.
    #Returns the figure number.
    y = randmatrix(1,10);
    y = y*10;
    n = 5;
    out = histc(y,n);
    #Creates a histogram plot of y, using n bins, with axis labels and a title.
    histc (y,n, "x label", "y label", "title");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ histogram ](/hc/en-us/articles/360034409314-histogram) , [ legend ](/hc/en-us/articles/360034931233-legend) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ closeall ](/hc/en-us/articles/360034410594-closeall) , [ visualize ](/hc/en-us/articles/360034410514-visualize)
