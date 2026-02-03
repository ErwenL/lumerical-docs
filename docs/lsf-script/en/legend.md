# legend

Adds a legend to a line plot.

**Syntax** |  **Description**  
---|---  
legend("legend1","legend2",..., "legendn"); |  Adds a legend to the selected figure. Parameters can be strings, or an array (cell) of strings This function does not return any data.  
  
**Example**

Add a legend using an array of strings.
    
    
    x=linspace(0,10,100);
    y1=sin(x);
    y2=y1^2;
    plot(x,y1,y2,"x","y","title");
      
    # create an array of strings
    leg=cell(2);
    leg{1}="y1";
    leg{2}="y2";
      
    # add legend
    legend(leg);

Using a for loop to add a number to the legend.
    
    
    n=5; # number of legend
    leg=cell(n); # define the array of strings
    y=linspace(10,50,n);
    for (i=1:n){
    leg{i}=num2str(y(i));
    }
      
    # add legend
    legend(leg);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [plot ](/hc/en-us/articles/360034410474-plot) , [ closeall ](/hc/en-us/articles/360034410594-closeall) , [ visualize ](/hc/en-us/articles/360034410514-visualize)
