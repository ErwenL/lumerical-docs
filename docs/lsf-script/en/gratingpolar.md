# gratingpolar

Returns the relative strength of all physical grating orders where vector field information is returned in spherical coordinates. This is useful when studying the polarization effects. The data is normalized such that the sum of |Er|^2+|Etheta|^2+ |Ephi|^2 over all grating orders equals 1. See the [grating](/hc/en-us/articles/360034927213) function documentation for information on interpreting N, M, ux, uy for various monitor orientations.

3D simulations: Data is returned in a NxMxPx3 matrix where N,M are the number of grating orders. P is the number of frequency points. The third dimension is Er, Etheta, Ephi.

2D simulations: Data is returned in a NxPx3 matrix where N is the number of grating orders. P is the number of frequency points. The second dimension is Er, Etheta, Ephi.

The results are returned on hemisphere 1m away. For more information on the basis used please refer to [Understanding field polarization in far field projections](/hc/en-us/articles/360034914753)

**Syntax** |  **Description**  
---|---  
out = gratingpolar( "mname", f, index, direction); |  Returns the strength of all physical grating orders from the monitor. Output is in spherical coordinates.  
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
mname |  required |  |  string |  name of the monitor from which far field is calculated  
f |  optional |  1 |  vector |  Index of the desired frequency point. This can be a single number of a vector.  
index |  optional |  value at monitor center |  number |  The index of the material to use for the projection.  
direction |  optional |  direction of max power flow |  number |  Direction: this can be +1 or -1.  
  
**Examples**

This 2D result shows that gratingpolar gives the same result as the grating function when we calculate |Er|^2+|Etheta|^2+ |Ephi|^2.
    
    
    ?Gp=gratingpolar("monitor1");
    result: 
    -3.06956e-017+0i -0.069704-0.32201i 0+0i 
    -3.66784e-018-1.46714e-017i -0.0813186-0.381864i 0+0i 
    2.97089e-017+1.48545e-017i -0.670119-0.442682i 0+0i 
    -4.78864e-018-3.83091e-017i -0.0585844-0.30093i 0+0i 
    ?sum(abs(Gp)^2,2);
    result: 
    0.108549 
    0.152433 
    0.645027 
    0.093991 
    ?G=grating("monitor1");
    result: 
    0.108549 
    0.152433 
    0.645027 
    0.093991 

**See Also**

[List of commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn) , [ gratingperiod1 ](/hc/en-us/articles/360034927253-gratingperiod1) , [ gratingbloch1 ](/hc/en-us/articles/360034407134-gratingbloch1) , [ gratingu1 ](/hc/en-us/articles/360034407094-gratingu1) , [ gratingangle ](/hc/en-us/articles/360034927273-gratingangle) , [ gratingvector ](/hc/en-us/articles/360034407054-gratingvector) , [ Far field projections - Field polarization ](/hc/en-us/articles/360034914753-FFP-Field-polarization)
