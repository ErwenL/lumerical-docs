# integrate2

Very similar to the standard integrate function, except that singleton dimensions are
ignored.

As described in the integrate function description, integrating over dimensions with a
single value (singleton dimensions) returns zero because the area under a single point
is zero. In some cases, particularly when you are not sure which dimensions are
singleton, this behavior can cause difficulties. The integrate2 function automatically
ignores all dimensions with a size of one, which avoids the problem of a zero valued
integrals due to singleton dimensions.

| **Syntax**                           | **Description**                                                                                                                                                                                                                                                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = integrate2(A, 1, x1);          | Integrates A over the first dimension in the matrix. x1 is the corresponding position vector.                                                                                                                                                                                                                           |
| out = integrate2(A, d, x1, x2, ...); | Calculates the integral of A over the specified dimension(s) d. d is a vector containing the dimensions over which to integrate. xi is the position vector corresponding to the dimensions of A over which the integration is occurring. If any of the xi vectors only have 1 element, integrate returns 0. For example |

- power = integrate2(A,1:2,x,y) will integrate A over an x-y surface.

**Example**

In the following example, we compare the integrate and integrate2 commands when
integrating over matrices with singleton dimensions.

```
# create 3D matrix of results: data(x,y,z) where
# there are 50 'x' sample points, 1 'y' sample points
# and 40 'z' sample points. This is typical of data
# from a 2D monitor oriented in the XZ plane.
x=linspace(-5,5,50);
y=0;
z=linspace(-3,3,40);
X=meshgrid3dx(x,y,z);
Z=meshgrid3dz(x,y,z);
data = X^2 + Z^2;
image(x,z,data,"x","z","data");
?integrate2(data, [1,2,3], x,y,z); # Integrate2 ignores singleton dimension, giving non-zero result.
?integrate (data, [1,2,3], x,y,z); # Result is zero because of the singleton dimension
?integrate (data, [1,3] , x,z ); # Get the same result as integrate2 by integrating over x and z, but not y.
> result: 
> 680.653 
> result: 
> 0 
> result: 
> 680.653 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ integrate ](./integrate.md) , [ conv2 ](./conv2.md) , [ max ](./max.md) ,
[ min ](./min.md) , [ interp ](./interp.md) , [ find ](./find.md) ,
[ pinch ](./pinch.md) , [ round ](./round.md) , [ getdata ](./getdata.md) ,
[ sum ](./sum.md) , [ length ](./length.md)
