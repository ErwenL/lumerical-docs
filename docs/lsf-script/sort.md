# sort

Sorts a matrix in ascending or descending order. Complex values are sorted by magnitude and then by angle. For more complex sorting methods, see the  sortmap  function. 

This function was introduced in the 2018a R6 release. 

**Syntax** |  **Description**  
---|---  
out = sort(A);  |  Returns the sorted matrix of A, in ascending order. Complex values are sorted by magnitude and then by angle. A is treated as a linear array for sorting, but out preserves the shape of A. Typically the command is used for Nx1 or 1xN matrices.   
out = sort(A, ascending);  |  The optional bool argument is set to true by default. When it is false, the sort is done in descending order.   
  
**Example**

This example shows a simple sort. For more complex usage, see  sortmap  . 
    
    
    A = [3, 4, 1, 7, 10, -1];
    ?B = sort(A);
    ?D = sort(A, false);

**See Also**

[ sortmap ](/hc/en-us/articles/360034926873-sortmap)
