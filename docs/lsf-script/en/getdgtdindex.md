# getdgtdindex

Returns the complex refractive index of a material in the Materials Group with material fit that will be used in a DGTD simulation. 

Many materials (such as sampled materials) have properties that depend on frequency. Using getdgtdindex, you can specify frequency range, and the fitting routine will find a best fit of the material data over that range. The refractive index evaluated at the specified frequencies is then returned. 

Note that the fit result depends on the fit parameters, Max coefficients and Tolerance set for the material, thus getdgtdindex result depends on those parameters as well. Tips for setting these parameters can be found at [ Modifying the material fits ](/hc/en-us/articles/360034915053-Modifying-the-Material-Fits) . 

**Syntax** |  **Description**  
---|---  
out = getdgtdindex( "materialname", f, fmin, fmax);  |  Returns the complex index of the material with the given name. The index is returned for the specified frequency f. Similar to getindex, but you also specify fmin and fmax, the span of frequency of the DGTD simulation. All frequency units are in Hz.   
  
**Examples**

This example shows how to get material (n,k) data with the getindex and getdgtdindex functions. In this case, we compare the experimental data to the DGTD fit of the that data that will be used in the simulation. 

Note that the material "Au (Gold) - CRC" with optical material properties must already exist in the Materials Group before running the script. 
    
    
    material="Au (Gold) - CRC";   # material 
    source_min_f=c/700e-9;      # source min frequency
    source_max_f=c/400e-9;      # source max frequency
    f_vector=linspace(source_max_f,source_min_f,100);
    # get experimental data
    n_exp=getindex(material,f_vector);
    # get DGTD fit of experimental data
    n_dgtd=getdgtdindex(material,f_vector,source_min_f,source_max_f);
    # plot results
    plot(c/f_vector*1e9,real(n_exp),real(n_dgtd),"wavelenth (nm)","n",material);
    legend("experimental data","DGTD fit");
    plot(c/f_vector*1e9,imag(n_exp),imag(n_dgtd),"wavelenth (nm)","k",material);
    legend("experimental data","DGTD fit");
    # output index data to text file
    data=matrix(100,5);
    data(1:100,1)=c/f_vector*1e9;
    data(1:100,2)=real(n_exp);
    data(1:100,3)=imag(n_exp);
    data(1:100,4)=real(n_dgtd);
    data(1:100,5)=imag(n_dgtd);
    write(material+".txt","wavelength_nm exp_n exp_k dgtd_n dgtd_k");
    write(material+".txt",num2str(data));

**See Also**

[ adddgtdsolver ](/hc/en-us/articles/360034925013-adddgtdsolver)
