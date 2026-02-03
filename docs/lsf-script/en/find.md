# find

Searchs for entries in a matrix that meet some condition. The indices of those values are returned. For multi-dimensional matrices, the find function will still return a single index. This is useful when using the output from find in a loop.

**Syntax** |  **Description**  
---|---  
out = find(x,n); |  Will return the index of the first element in x that corresponds to the closest value to 'n'.  
out = find(x==n); |  Will return the index of all elements in x that have a value exactly equal to 'n'. If 0 is returned, indicates that no element of value 'n' was found.  
out = find(x); |  Will return the index of all non-zero elements in x. If 0 is returned, indicates that no element of non-zero value was found.  
out = find(x>n); |  Will return the indices of all values of x that are greater than 'n'.  
out = find((x>=n) & (x<m)) |  Will return the indices of all values of x that are greater than or equal to 'n', AND less than 'm'.  
  
**Example**

The following two examples show the basic output from the find function.
    
    
    x = -2:7;
    ?find(x>5);
    result: 
    9 
    10
    x = linspace(0,10e-6,100);
    ?x( find(x,5e-6) );
    result: 
    5.05051e-006 

This example shows the equivalent usage of the find function for the example above but with one argument rather than two:
    
    
    minDiff=min(abs(x-5e-6));
    closestIndices=find(abs(x-5e-6)==minDiff);
    ?x(closestIndices(1));
    result: 
    5.05051e-006  

This example shows the output of find for multi-dimensional data. A single index is returned. Data can be accessed from a matrix in the same manner.
    
    
    x = matrix(2,2);
    x(2,2) = 7;
    ?find(x,7);
    result:
    4
    ?x(4);
    result:
    7

This example shows how to use the find function to set all values in a matrix that are larger than 10 to exactly 10.
    
    
    x = linspace(0,20,200);
    y = sin(x)*11;
    y2 = y;
    n = find(y>10);
    y(n) = y(n)*0+10;
    plot(x,y,y2);

This example shows how to convert the single index returned by the find function into individual i,j,k matrix indices. This particular example returns the index value of the maximum intensity value, given a particular monitor data.
    
    
    #Get the monitor data
    E = getresult("monitor","E");
    #Get the position and frequency data from the dataset E
    x = E.x;
    y = E.y;
    f = E.f;
    #Get the length of the properties
    nx = length(x);
    ny = length(y);
    nz = length(z);
    nf = length(f);
    #Get the intensity values
    e2 = E.E2;
    #Get the maximum intensity value
    indexE2 = find(e2, max(e2));
    #Create the grids that will be used to extract the actual position values
    X = meshgrid3dx(x,y,f);
    Y = meshgrid3dy(x,y,f);
    F = meshgrid3dz(x,y,f);
    #Create the grids that will be used to extract the index values
    X2 = meshgrid3dx(1:nx,1:ny,1:nf);
    Y2 = meshgrid3dy(1:nx,1:ny,1:nf);
    F2 = meshgrid3dz(1:nx,1:ny,1:nf);
    #Output the values of the position and the index
    ?X(indexE2);
    ?Y(indexE2);
    ?F(indexE2);
    ?X2(indexE2);
    ?Y2(indexE2);
    ?F2(indexE2);

This example shows another way of how to convert the single index returned by the find function into individual i,j,k matrix indices.
    
    
    # create example matrix
    a = randmatrix(3,4,5);
    # find matrix index of value closest to 0.5
    index = find(a,0.5);
    ?"Single index access: a("+num2str(index)+") = "+num2str(a(index));
    # convert index to row, col indices 
    matrix_size = size(a);
    indices = matrix(length(matrix_size));
    # do for each dimension
    for (i = 1:length(matrix_size)) { 
     mod_dividend = index;
     mod_divisor = matrix_size(i);
     mod_remainder = mod(mod_dividend,mod_divisor);
     if (mod_remainder == 0) { mod_remainder = matrix_size(i); }
     indices(i) = mod_remainder;
     # remove this dimension from further calculations
     index = (index+(matrix_size(i)-mod_remainder))/matrix_size(i);
    }
    ?"multi indice access: a("+num2str(indices(1))+","+
                  num2str(indices(2))+","+
                  num2str(indices(3))+")="+
                  num2str(a(indices(1),indices(2),indices(3)));

**See Also**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ pinch ](https://optics.ansys.com/hc/en-us/articles/360034405674-pinch) , [ findpeaks ](https://optics.ansys.com/hc/en-us/articles/360034925933-findpeaks) , [ integrate ](https://optics.ansys.com/hc/en-us/articles/360034405814-integrate) , [ length ](https://optics.ansys.com/hc/en-us/articles/360034925653-length) , [ size ](https://optics.ansys.com/hc/en-us/articles/360034405654-size) , [ mod ](https://optics.ansys.com/hc/en-us/articles/360034926373-mod) , [ meshgrid3dx ](https://optics.ansys.com/hc/en-us/articles/360034929693-meshgrid3dx) , [ meshgrid3dy ](https://optics.ansys.com/hc/en-us/articles/360034409374-meshgrid3dy) , [ meshgrid3dz ](https://optics.ansys.com/hc/en-us/articles/360034929713-meshgrid3dz)
