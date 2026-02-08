# corrcoef

Calculates the correlation matrix. The input can be one matrix, which contains the
observations of a set of random variables, or two matrices, each one representing a
vector of observations.

| **Syntax**                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| corrcoef(A); corrcoef(A, B); | Calculate the correlation matrix. R = corrcoef(A) returns the matrix of correlation coefficients for A, where the columns of A represent random variables and the rows represent observations. R = corrcoef(A, B) returns the correlation coefficients between two random variables A and B. If A and B are vectors of observations with equal length, corrcoef(A, B) is the 2-by-2 correlation matrix; if A and B are matrices of observations, corrcoef(A, B) treats A and B as vectors and is equivalent to corrcoef(A(1:lenght(A)), B(1:length(B))). A and B must have equal size. |

**Example**

The following examples illustrate how to find the covariance matrix.

```
A = [1,2;3,4];
B = [1.1,2.7; 2.5, 4.3];
?corrcoef(A,B);
?corrcoef(A(1:length(A)),B(1:length(B)));
result: 
1  0.92621  
0.92621  1  
result: 
1  0.92621  
0.92621  1  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ cov ](./cov.md) ,
[ corrtransf ](./corrtransf.md)
