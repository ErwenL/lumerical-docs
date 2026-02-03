# meshgridx

Create a 2D meshgrid in the x direction 

**Syntax** |  **Description**  
---|---  
out = meshgridx(x,y);  |  If x and y are single column (or single row vectors), of dimension nX1 and mX1 respectively, the command 

  * X = meshgridx(x,y); 

Will create a 2D matrix of dimension nXm where X(i,j)=x(i).   
  
**Examples**

This example uses the image function to show the output of meshgrid. See the image function help for another example that uses meshgrid. 
    
    
    x=linspace(0,10,100);
    y=linspace(0,10,10);
    image(x,y,meshgridx(x,y),"x","y","meshgridx");
    image(x,y,meshgridy(x,y),"x","y","meshgridy");

The following figures show the output of the the example code. 

This example uses the mesh grid functions to create an image plot of a 2D gaussian function Z(x,y)=exp( -x^2-y^2). 
    
    
    x=linspace(-3,3,100); 
    y=x; 
    X=meshgridx(x,y); 
    Y=meshgridy(x,y); 
    Z=exp( -X^2 -Y^2); 
    image(x,y,Z);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ image ](/hc/en-us/articles/360034931253-image) , [ meshgridy ](/hc/en-us/articles/360034929673-meshgridy) , [ meshgrid3dx ](/hc/en-us/articles/360034929693-meshgrid3dx)
