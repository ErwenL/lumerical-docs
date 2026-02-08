# pinch

Removes singleton dimensions from a matrix.

| **Syntax**      | **Description**                                                                            |
| --------------- | ------------------------------------------------------------------------------------------ |
| out = pinch(x); | Removes all singleton dimensions. For example, if x is a matrix of dimension 1x1x1xM, then |

- y=pinch(x);

will return a Mx1 matrix where

- y(i) = x(1,1,1,i);

pinch(x,i); | Removes a specified dimension. If x is an NxMxKxP matrix then

- y=pinch(x,2);

will return an NxKxP matrix where

- y(i,j,k) = x(i,1,j,k)

pinch(x,i,j); | Removes a specified dimension but keeps a specific index for the
dimension being removed. If x is an NxMxKxP matrix then

- y=pinch(x,2,4);

will return an NxKxP matrix where

- y(i,j,k) = x(i,4,j,k)

**Example**

This example shows how pinch can be used to remove singleton dimensions from a matrix.
The matrix command is used to create a 6x1x4x1 matrix. Applying the pinch function to
this matrix will remove the two singleton dimensions, resulting in a 6x4 matrix.

```
x=matrix(6,1,4,1);
?size(x);
result: 
6 1 4 1 
?size(pinch(x));
result: 
6 4 
```

Suppose the power monitor named "field" is a 2D monitor in the XY plane set to record
multiple frequency points between 200THz and 300THz. In this case, the variable Ex will
be a 4D matrix, where the dimensions are length(X) by length(Y) by length(Z) by
length(F). Since this is a 2D monitor in the XY plane, there will be only one Z
position, which means the length of the third dimension (Z) will be 1.

With the pinch and find commands, we can select a particular frequency to be imaged.
First, the find command is used to determine the index of the frequency value closest to
250THz. Next, the pinch command is used to select the data in Ex corresponding to that
frequency. A second pinch command is used to remove the singleton Z dimension. The end
result is the 2D matrix Ex(x,y) at a specific value of z and f.

```
m="field";      # monitor name
x=getdata(m,"x");  # get monitor data
y=getdata(m,"y");
z=getdata(m,"z");
f=getdata(m,"f");
Ex=getdata(m,"Ex");
fi=find(f,250e12);  # find the index that corresponds to f=250THz
Ex=real(Ex);     # take real part of Ex    
?"Size of x: "+num2str(length(x)); # print the matrix size to the screen
?"Size of y: "+num2str(length(y));
?"Size of z: "+num2str(length(z));
?"Size of f: "+num2str(length(f));
?"Size of Ex: "+num2str(size(Ex));
to_plot=pinch(Ex,4,fi);   # select frequency. Size will be length(x) by length(y) by length(z)
to_plot=pinch(to_plot);   # remove singleton z dimension. Size will be length(x) by length(y)
image(x*1e6,y*1e6,to_plot, "x (um)","y (um)","Ex at "+num2str(f(fi)/1e12)+ " THz" ); 
```

**See Also**

[ List of commands](../lsf-script-commands-alphabetical.md), [ find](./find.md),
[ size](./size.md), [ flip](./flip.md)
