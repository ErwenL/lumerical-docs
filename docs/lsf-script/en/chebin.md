# chebin

Returns the Chebyshev interpolation of a sampled function. Chebyshev interpolation is
useful for accurately interpolating a smooth function using a very small number of
samples. The key requirement for this type of interpolation to work is that the function
is sampled on the Chebyshev roots grid.

| **Syntax**               | **Description**                                                                                                                                                                                                                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| chebin(f,x,xi,xmin,xmax) | Interpolates the function f onto the xi points. It assumes that f contains the samples of the function taken on the Chebyshev roots grid specified in x; x must be constructed by the call # x = chpts(xmin,xmax,NumPts), otherwise an error is returned. |

**Example**

See example for the chpts command.

**See Also**

[dcht](./dcht.md),[chpts](./chpts.md),[icht](./chebin.md)
