# []

Specify matrix element by element. 

**Command** |  **Description**  
---|---  
x = [u11,...,u1N; u21,...,u2N; uM1,...,uMN]  |  Create an N by M matrix. Columns are separated with semicolons. Elements in a row are separated with commas. The entries can either be scalars or matrices of compatible dimension.   
  
**Examples**
    
    
    ?x=[1,2;3,4;5,6];
    result: 
    1 2 
    3 4 
    5 6
    ?x(1:3,1);
    result: 
    1 
    3 
    5   
    a=matrix(2,2,2); 
    a(1,1)=1;
    a(2,2)=2;
    b=a+1;
    ?c=[a,b];
    result(i,j,1):
    1 0 2 1 
    0 2 1 3 
    result(i,j,2):
    0 0 1 1 
    0 0 1 1 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ linspace ](/hc/en-us/articles/360034409254-linspace) , [ matrix ](/hc/en-us/articles/360034929613-matrix) , [ Accessing and assigning matrix elements ](/hc/en-us/articles/360034409414-Accessing-and-assigning-matrix-elements)
