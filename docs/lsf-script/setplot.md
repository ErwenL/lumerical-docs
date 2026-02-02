# setplot

Sets the plot properties of a figure. 

**Syntax** |  **Description**  
---|---  
?setplot;  |  Creates a string which lists all figure properties for the figure that is currently selected. Unless the selectfigure() command was called, the most recently created plot will be selected.   
setplot("property", "property value");  |  Set the desired property of the currently selected figure to property value.   
  
**Example**

This example uses the script command setplot to see the properties of a line plot figure, then adds a title to the figure. 
    
    
    plot(1:10,(1:10)^2);
    ?setplot;
    x min
    x max
    y min
    y max
    title
    x label
    y label
    legend position
    setplot("title","my figure");   #add a title to the figure

This example creates an image plot of a 10x10 matrix of random numbers between zero and one, then sets the color bar limits to 0.2 - 0.8 with the setplot command. 
    
    
    data=randmatrix(10,10);
    image(1:10,1:10,data);
    setplot("colorbar min",0.2);
    setplot("colorbar max",0.8);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ image ](/hc/en-us/articles/360034931253-image) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ visualize ](/hc/en-us/articles/360034410514-visualize)
