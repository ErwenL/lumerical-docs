# integrate

Returns the integral over the specified dimension of a matrix.

Integrals over singleton dimensions will return zero (i.e. the area under a single point
is zero). See integrate2 for an alternate behavior.

| **Syntax**                          | **Description**                                                                                                                                                                                                                                                |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = integrate(A, n, x1);          | Integrates A over the nth dimension in the matrix. x1 is the corresponding position vector for that dimension.                                                                                                                                                 |
| out = integrate(A, d, x1, x2, ...); | Calculates the integral of A over the specified list of dimension(s) d. d is a vector containing the dimensions over which to integrate. xi are the position vectors corresponding to the dimensions of A over which the integration is occurring. For example |

- power = integrate(A,1:2,x,y) will integrate A over an x-y surface.

**Example**

In the following example, the integrate command is used to integrate y=x^2 from 0 to 3,
where the function is sampled at the points x=0,1,2,3. The integrate function will
determine dx from the position vector x. For reference, the value of this integral for
the continuous function y=x^2 (as opposed to the discrete samples in this example) is 9.
Reducing dx will make this discrete integral approach the continuous result.

Advanced note: The actual calculation in this very simple example will be 0.5*0 + 1*1 +
1*4 + 0.5*9 = 9.5, as illustrated in the figure below. It is interesting to note that
the first and last points have a factor of 0.5\*dx because they are at the edge of the
integration range. Without the factor of 0.5 applied to those points, the integral would
effectively be calculated from x=-0.5 to x=3.5

```
?x=0:3;
y=x^2;
?integrate(y,1,x);
result: 
0 
1 
2 
3 
result: 
9.5 
```

Next, we demonstrate that the integrate function correctly treats non-uniform sampling.
The portion of the function from 0 to 2 is evaluated with a dx=1, while a dx of 0.2 is
used from 2 to 3. In this case, the integrate function will calculate 0.5*0 + 1*1 +
0.6*4 + 0.2*4.84 + 0.2*5.76 + 0.2*6.76 + 0.2*7.84 + 0.1*9;

```
?x=[[0:1]; [2:0.2:3]];
y=x^2;
?integrate(y,1,x);
result: 
0 
1 
2 
2.2 
2.4 
2.6 
2.8 
3 
result: 
9.34 
```

Lastly, this example shows how to calculate the power transmitted through a y-normal
monitor by integrating the Poynting vector. To get transmitted power, we want to
integrate the real part of the normal component of the poynting vector (Py). The Py data
matrix will have size N x x N y x N z x N f , where Nx, Ny, Nz are the number of mesh
point in each direction. If the monitor is Y-normal, Ny=1. Nf is the number of frequency
points collected by the monitor. After integrating over the X and Z direction, we are
basically left with a 1D function of the transmitted power vs frequency.

```
Py = getdata("Monitor1","Py");
x = getdata("Monitor1","x");
y = getdata("Monitor1","y");
z = getdata("Monitor1","z");
f = getdata("Monitor1","f");
power = 0.5 * integrate( real(Py), [1,3], x,z );
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ integrate2 ](./integrate2.md) , [ conv2 ](./conv2.md) , [ max ](./max.md) ,
[ min ](./min.md) , [ interp ](./interp.md) , [ find ](./find.md) ,
[ pinch ](./pinch.md) , [ round ](./round.md) , [ getdata ](./getdata.md) ,
[ sum ](./sum.md) , [ length ](./length.md)
