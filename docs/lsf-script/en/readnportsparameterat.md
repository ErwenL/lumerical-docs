# readnportsparameterat

Interpolates the [S-Parameter sweep](https://optics.ansys.com/hc/en-us/articles/360036107934-The-S-parameter-sweep) file with the specified parameter values.

**Syntax** |  **Description**  
---|---  
M = readnportsparameterat(“filename”, sweep_param) |  Interpolates the S-Parameter sweep file with the specified parameter values, using the spline interpolation method. filename: S-Parameter sweep file. sweep_param: specified sweep parameters, usually in the format of a matrix.  
M = readnportsparameterat“filename”, sweep_param, opt)  |  Interpolates the S-Parameter sweep file with the specified parameter values, using interpolation options set in the structure named opt. filename: S-Parameter sweep file. sweep_param: specified sweep parameters, usually in the format of a matrix. opt: Structure setting interpolation options. The structure fields are described in the table below.  
  
The option structure has the following fields, the spelling of each field is case-sensitive.

**Field** |  **Description**  
---|---  
method |  The method used for interpolation. The following options are supported:

  * spline: Spline interpolation method, this is the default method.
  * Geodesic: Geodesic interpolation method which ensures smooth transitions. When geodesic interpolation is selected, a similarity check is performed on original data points near the interpolated point used for the interpolation, if these points are not sufficiently similar, the data is coarse and a warning is displayed. This method cannot be used for extrapolation.

  
passivity |  Whether passivity is enforced for the s-parameter data prior to interpolation. This field only affects results when “geodesic” is selected as the interpolation method. When data is non-passive, a warning message is always displayed. The following options are supported:

  * enforce: Ensures S-matrix is passive by making sure that the induced 2-norm of the s-parameters is less than 1. This is the default method.
  * ignore: Ignores passivity of the s-parameters and interpolates as-is.

  
  
**Note** : For more information on how passivity is enforced, see this [Knowledge Base](https://optics.ansys.com/hc/en-us/articles/360059772393-S-parameter-passive-workflow-guide#toc_4) article.

**Example**

The following script interpolates the S-Parameter file " coupler_s_parameter_sweep.txt " with the specified parameters that defined in a matrix named "sweep_param". Then this interpolated s-parameter can be assigned to a s-parameter element.
    
    
    #Here, the variables radius, Lc, and gap has been set previously  
    sweep_param = matrix( 3 );  
    sweep_param(1)=radius;  
    sweep_param(2)=Lc;  
    sweep_param(3)=gap;  
    ?M = readnportsparameterat("coupler_s_parameter_sweep.txt", sweep_param );

The following script interpolates the same S-Parameter file, but with the geodesic option and ignoring passivity.
    
    
    ?M = readnportsparameterat("coupler_s_parameter_sweep.txt", sweep_param, {"method":"geodesic", "passivity":"ignore"});

**See Also**

[ convertnportsparametersweep ](/hc/en-us/articles/360034409234-convertnportsparametersweep)
