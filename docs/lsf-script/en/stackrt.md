# stackrt

Calculates the reflection and transmission of a plane wave through a multi-layer stack using the analytic transfer matrix method. This function returns the fraction of transmitted and reflected power (Ts, Tp, Rs, Rp), and the complex reflection and transmission coefficients (ts, tp, rs, rp), for both S and P polarizations. All results are returned in a single dataset as a function of frequency and incidence angle (optional).

NOTE: From 2022 R1.2, stackrt script command supports fully anisotropic and dispersive materials by specifying the nine values of the second-order refractive index tensor. For anisotropic materials, the polarization of reflected light could vary from its incident polarization. The suffix **sp** and **ps** denote how polarization is changed in the returned power and coefficients. **sp** stands for **s** incident and **p** reflected/transmitted.

To calculate the fields within the stack, please see [ stackfield](/hc/en-us/articles/360034406294-stackfield).

**Syntax** |  **Description**  
---|---  
RT = stackrt(n,d,f); |  n: Refractive index of each layer. Size can be

  * Nlayers: isotropic and non-dispersive
  * Nlayers x Nfreq: isotropic and dispersive
  * Nlayers x 3: anisotropic and non-dispersive
  * Nlayers x Nfreq x 3: anisotropic and dispersive materials are involved.  
NOTE: Only birefringence in z (nx=ny≠nz) is supported. The commands will give an error unless nx=ny.
  * Nlayers x Nfreq x 9: anisotropic and dispersive materials are involved.  
NOTE: We flatten the second-order refractive index tensor into an array. The third dimension indicates the position in the tensor. For example, the position index "1", "2", "3", "4" and "5" corresponds to n11, n21, n31, n12 and n22, respectively.

d: Thickness of each layer. Size is Nlayers. f: Frequency vector with a length of Nfreq.  
RT = stackrt(n,d,f,theta); |  theta: Angle vector, in degrees. Optional.  
  
For more information on the complex coefficients see [Stack optical solver overview](/hc/en-us/articles/360034914653).

### Example 1: Five-layer stack with isotropic materials

Calculate the reflection, transmission, and field distribution from a 5 layer stack.
    
    
    f = linspace(c/400e-9, c/1000e-9,100); # frequency vector  
    theta = 0:1:45; # angle vector  
    d = [0; 200e-9; 300e-9; 400e-9; 0]; # air/SiO2/Si/SiO2/air  
    nf = length(f);  
    nd = length(d);  
      
    # refractive index of each layer (non-dispersive)  
    n1 = [1; 1.5; 2.5; 1.5; 1];   
      
    # refractive index of each layer (dispersive)  
    n2 = matrix(nd,nf);  
    n2(1,1:nf) = 1; # air  
    n2(2,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
    n2(3,1:nf) = getfdtdindex("Si (Silicon) - Palik",f,min(f),max(f));  
    n2(4,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
    n2(5,1:nf) = 1; # air  
      
    RT1 = stackrt(n1,d,f); # non-dispersive index data, and theta=0  
    RT2 = stackrt(n2,d,f,theta); # dispersive data index data, and theta from 0 to 45 deg  
      
    visualize(RT1);  
    visualize(RT2);  
      
    plot(RT1.lambda*1e6,RT1.Rp,RT1.Rs,RT1.Tp,RT1.Ts,"wavelength (um)","Power","non-disperisive, theta=0");  
    legend("Rp","Rs","Tp","Ts");  
    image(RT2.lambda*1e6,RT2.theta,RT2.Rp,"wavelength (um)","theta (deg)","Rp, dispersive example");

### Example 2: Birefringent slab in air
    
    
    N_layers = 3;  
    Nfreqs = 100;  
    n = matrix(N_layers, Nfreqs, 3);  
      
    n(1, :, :) = 1;   # air  
    n(2, :, 1) = 2.1; # nx  
    n(2, :, 2) = 2.1; # ny  
    n(2, :, 3) = 2.5; # nz  
    n(3, :, :) = 1;   # air  
      
    d = [0; 1e-6; 0]; # air/ birefringent slab / air  
    f = linspace(c/1e-6, c/1.5e-6, Nfreqs);  
    theta = 0:1:45;  
      
    RT = stackrt(n,d,f,theta);  
      
    visualize(RT);

### Example 3: A fully anisotropic and dispersive slab in air

Download and run the attached script stackrt_anisotropic.lsf. 

Please note that we use the Euler angle definition shown in lines 32-46 in the script file to rotate a diagonalized permittivity matrix and then derive the refractive index matrix.

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ stackfield ](/hc/en-us/articles/360034406294-stackfield) , [ multilayer stack calculations ](/hc/en-us/articles/360034914653) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex) , [ visualize ](/hc/en-us/articles/360034410514-visualize)
