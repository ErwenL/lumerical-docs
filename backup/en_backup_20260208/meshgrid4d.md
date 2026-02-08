# meshgrid4d

Create a 4D meshgrid in any direction. 

**Syntax** |  **Description**  
---|---  
out = meshgrid4d(dim, x1, x2, x3, x4);  |  The 4D meshgrid function.  dim specifies the dimension along which to create the grid  x1,x2,x3,x4 are the position vectors in each direction   
  
**Examples**

Create a 4D frequency vector from a set of position vectors. 
    
    
    x=linspace(-10,10,20);
    y=linspace(-10,10,21);
    z=linspace(-10,10,22);
    f=linspace(0,100,23);
    F=meshgrid4d(4,x,y,z,f); # create meshgrid in 4th (frequency) dimension
    ?size(F);         # size should be equal to the size of each position vector
    result: 
    20 21 22 23 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ meshgridx ](/hc/en-us/articles/360034409334-meshgridx) , [ meshgridy ](/hc/en-us/articles/360034929673-meshgridy) , [ meshgrid3dy ](/hc/en-us/articles/360034409374-meshgrid3dy) , [ meshgrid3dz ](/hc/en-us/articles/360034929713-meshgrid3dz)
