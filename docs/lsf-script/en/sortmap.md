# sortmap

The script command sortmap is used to sort matrices in more complex ways than simply
ascending or descending order of the array. It is used to create a map of the sorted
indices of the array that can be reused afterwards to sort the original matrix or other
matrices.

This function was introduced in the 2018a R6 release.

| **Syntax**                   | **Description**                                                                                                                                                                                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = sortmap(A);            | Returns a matrix of indices that map the sorted matrix of A. Complex values are sorted by magnitude and then by angle. A is treated as a linear array for sorting, but out preserves the shape of A. Typically the command is used for Nx1 or 1xN matrices. |
| out = sortmap(A, ascending); | The optional bool argument is set to true by default. When it is false, the sort is done in descending order.                                                                                                                                               |

**Example**

This example shows how to use sortmap instead of sort, and that the results are
equivalent

```
A = [3; 4; 1; 7; 10; -1];
?B = sort(A);
m = sortmap(A);
?D = A(m);
```

This example shows how to sort by ascending imaginary part, real part or magnitude

```
A = [3+1i; 4+0.1i; 1-10i; 7-20i; 10+15i; -1+0i];
m = sortmap(imag(A));
?B = A(m); # sorted by ascending imaginary part
m = sortmap(real(A)); 
?D = A(m); # sort by ascending magnitude
m = sortmap(abs(A)); 
?E = A(m); # sort by ascending magnitude
```

This example shows how 2 different vectors (neff and ng) can be sorted according to
descending neff.

```
neff = [2.3; 2.4; 3.2; 1.45 ];
ng = [4.2; 4.3; 4.8; 4.9 ];
m = sortmap(neff,false);
?neff = neff(m);
?ng = ng(m);
```

This example shows how we can sort 2 vectors of x and y by the closest points to x0,y0

```
x = [4.3; -4; -2; 10; 2.0 ];
y = [ -1;  1;  2;  5;  -4 ];
x0 = 2;
y0 = 2;
m = sortmap( (x-x0)^2 + (y-y0)^2);
x = x(m);
y = y(m);
?[x,y];
```

This example shows how the rows of an NxM matrix can be sorted based on the values in
the 3rd column:

```
A = [ 2, 4, 6;
      3, 2, 1;
      4, 4, 4 ];
m = sortmap(A(:,3));
?A = A(m,:);
```

**See Also**

[ sort ](./sort.md)
