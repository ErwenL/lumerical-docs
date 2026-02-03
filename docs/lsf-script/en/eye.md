# eye

Creates a 2D identity matrix. 

**Syntax** |  **Description**  
---|---  
I = eye;  |  Returns a 1x1 matrix, value 1.0.   
I = eye(n);  |  Returns nxn identity matrix.   
I = eye(n,m);  |  Returns nxm matrix with ones on main diagonal   
  
**Examples**

Following are some examples and the results of the script command usage. 
    
    
    ?eye;
    result: 
    1 
    ?eye(3);
    result: 
    1 0 0 
    0 1 0 
    0 0 1 
    ?eye(2,3);
    result: 
    1 0 0 
    0 1 0 
    ?eye(3,2);
    result: 
    1 0 
    0 1 
    0 0 

**See Also**

[ Datasets ](/hc/en-us/articles/360034409554-Datasets) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ matlab ](/hc/en-us/articles/360034407974-matlab) , [ matrix ](/hc/en-us/articles/360034929613-matrix)
