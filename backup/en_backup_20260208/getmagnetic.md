# getmagnetic

Returns the sum of the amplitude squares for all magnetic field components, i.e. it returns |Hx|  2  +|Hy|  2  +|Hz|  2  . 

**Syntax** |  **Description**  
---|---  
out = getmagnetic( "monitorname");  |  Returns |Hx|  2  +|Hy|  2  +|Hz|  2  from the monitor.   
getmagnetic( "monitorname", option);  |  The optional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2.   
  
**Examples**

This example creates an image plot of |H|^2 for a z-normal frequency monitor in the x-y plane. 
    
    
    H2=getmagnetic("output");
    x=getdata("output","x");
    y=getdata("output","y");
    image(x,y,H2);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ getelectric ](/hc/en-us/articles/360034409974-getelectric) , [ cwnorm ](/hc/en-us/articles/360034405454-cwnorm) , [ nonorm ](/hc/en-us/articles/360034405434-nonorm)
