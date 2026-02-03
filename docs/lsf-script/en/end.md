# end

Specifies the last index of an array. 

**Syntax** |  **Description**  
---|---  
y=x(3:end);  |  y will be the submatrix of x, from the 3rd element to the last element.   
  
**Examples**

Create a vector, then access a portion of that matrix. 
    
    
    a=l:5;     # a will be vector (1, 2, 3, 4, 5)
    ?b=a(4:end);  # b will be vector (4, 5) 

Retrieve elements from matrices using 'end' to mean last index. You may use 'end' in any mathematical expression that results in indexing. Nested use of 'end' should work properly. 
    
    
    A = randmatrix(5,4);
    ?A(3:end,2);      # equivalent to A(3:5,2)
    ?A(1:end-2,2);    # equivalent to A(3:5-2,2)
    ?A(end-1:-1:1,2); # equivalent to A(5-1:-1:1,2)
    ?A(1:end);        # equivalent to A(1:20) and A(:)
    B = [1,0,1,1];
    ?A( sum(B(2:end)):end, 1);  # equivalent to A( sum(B(2:4)):5, 1)
    ?end+4;           # error: "context error - 'end' may only be used when indexing a matrix"

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ linspace ](/hc/en-us/articles/360034409254-linspace) , [ : ](/hc/en-us/articles/360034929533--) . 
