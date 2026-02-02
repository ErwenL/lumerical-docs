# polyand

Combines two polygons into one using the Boolean 'and' operation. 

The polygon vertices are contained in a single matrix of dimension Nx2 (or 2xN), where N >= 3 is the number of vertices. The dimension 2 corresponds to the x,y positions. For example, a square of side length 1 can be described by V = [ 0,0; 1,0; 1,1; 0,1] or V = [ 0,1,1,0;0,0,1,1]. 

**Syntax** |  **Description**  
---|---  
V3 = polyand(V1,V2);  |  Returns a new polygon, V3, that is the 'and' of V1 and V2.   
  
**Example**

In this example, we create two polygons and then show how the different Boolean operations can be done. We set up a mesh and use the inpoly function so that we can image the polygons and easily see the result. 
    
    
    # set up a mesh for imaging polygons with the inpoly command
    x = linspace(-1,3,200);
    y = linspace(-1,3,200);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    # enter 2 polygons and the polygon boolean operations
    V1 = [ 0,0; 1,0; 1,1; 0,1];
    V2 = [ 0,0; 2,2; 0,2];
    V3 = polyand(V1,V2);
    V4 = polyor(V1,V2);
    V5 = polydiff(V1,V2);
    V6 = polydiff(V2,V1);
    V7 = polyxor(V2,V1);
    # image all the polygons
    image(x,y,inpoly(V1,X,Y),"x","y","V1");
    image(x,y,inpoly(V2,X,Y),"x","y","V2");
    image(x,y,inpoly(V3,X,Y),"x","y","V1 and V2");
    image(x,y,inpoly(V4,X,Y),"x","y","V1 or V2");
    image(x,y,inpoly(V5,X,Y),"x","y","V1 - V2");
    image(x,y,inpoly(V6,X,Y),"x","y","V2 - V1");
    image(x,y,inpoly(V7,X,Y),"x","y","V1 xor V2");

The results are shown in the following images 

|   
---|---  
|   
|   
|   
  
Note: Other 2D or 3D objects  This command only works for 2D polygons. For other 2D or 3D objects, user may use the [ mesh order ](/hc/en-us/articles/360034915233-Mesh-Order) to combine multiple overlapped objects   
---  
  
**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ polyor ](/hc/en-us/articles/360034406114-polyor) , [ polydiff ](/hc/en-us/articles/360034926313-polydiff) , [ polyxor ](/hc/en-us/articles/360034406134-polyxor) , [ polyarea ](/hc/en-us/articles/360034926213-polyarea) , [ centroid ](/hc/en-us/articles/360034406074-centroid) , [ polyintersect ](/hc/en-us/articles/360034926233-polyintersect) , [ inpoly ](/hc/en-us/articles/360034926253-inpoly) , [ polygrow ](/hc/en-us/articles/360034406094-polygrow) , [ mesh order ](/hc/en-us/articles/360034915233-Mesh-Order)
