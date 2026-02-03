# getmodeindex

This function returns the material index of a material in the database as it will be used in an actual MODE simulation. 

Many materials (such as Sampled Materials) have properties that depend on frequency. Using getmodeindex, you can obtain the refractive index as a function of the specified frequency, f, as it will be used in MODE calculations. 

Note that the fit result depends on the fit parameters, Max coefficients and Tolerance set for the material, thus getfdtdindex result depends on those parameters as well. Tips for setting these parameters can be found at [ Modifying the material fits ](/hc/en-us/articles/360034915053-Modifying-the-Material-Fits) . 

**Syntax** |  **Description**  
---|---  
out = getmodeindex( "materialname", f);  |  Returns the complex index of the material with the given name. The index is returned for the specified frequency f. This result is identical to getindex unless the optional arguments fitsampled and fitanalytic are used. All frequency units are in Hz.   
getmodeindex("materialname", f,component);  |  Optional argument component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.   
getmodeindex("materialname", f,component, fitsampled, fitanalytic, fmin, fmax);  |  Optional arguments to specify if Sampled Materials or Analytic Materials should be fitted using Lumerical's multi-coefficient model (MCM), which is commonly used in FDTD simulations. If either of these options are set to 1 (true) then you must supply a minimum and maximum frequency for fitting. The MCM is typically used in MODE for 

  * Sampled Materials when calculating waveguide dispersion, and for 
  * Analytic Materials only for the purpose of using precisely the same materials in both FDTD and MODE simulations. 

The default values are 0 (false) for fitsampled and fitanalytic.   
  
**Example**

This example shows how to get material (n,k) data with the getindex and getmodeindex functions. In this case, we compare the experimental data to the MODE multi-coefficient fit of the that data that would be used in the simulation. 
    
    
    material="Si (Silicon) - Palik";   # material 
    source_min_f=c/700e-9;      # source min frequency
    source_max_f=c/400e-9;      # source max frequency
    f_vector=linspace(source_max_f,source_min_f,100);
    # get experimental data
    n_exp=getindex(material,f_vector);
    # get MODE multi-coefficient fit of experimental data
    n_mode=getmodeindex(material,f_vector,1,1,0,source_min_f,source_max_f);
    # plot results
    plot(c/f_vector*1e9,real(n_exp),real(n_mode),"wavelenth (nm)","n",material);
    legend("experimental data","MODE fit");
    plot(c/f_vector*1e9,imag(n_exp),imag(n_mode),"wavelenth (nm)","k",material);
    legend("experimental data","MODE fit");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getindex ](/hc/en-us/articles/360034409674-getindex) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial)
