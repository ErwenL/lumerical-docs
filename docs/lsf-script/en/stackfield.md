# stackfield

Calculates the fields within a multilayer stack illuminated from below by a plane wave using the analytic transfer matrix method. This function returns the E and H fields (Es, Ep, Hs, Hp). All results are returned in a single dataset as a function of frequency, incidence angle and location in the stack (z).

**Syntax** |  **Description**  
---|---  
field = stackfield(n,d,f); |  n: Refractive index of each layer. Size can be

  * Nlayers: isotropic and non-dispersive
  * Nlayers x Nfreq: isotropic and dispersive
  * Nlayers x 3: anisotropic and non-dispersive
  * Nlayers x Nfreq x 3: anisotropic and dispersive materials are involved.  
NOTE: Only birefringence in z (nx=ny≠nz) is supported. The commands will give an error unless nx=ny.

d: Thickness of each layer. Size is Nlayers. f: Frequency vector with a length of Nfreq.  
field = stackfield(n,d,f,theta,res); |  theta: Angle vector, in degrees. Optional, default is 0. res: resolution in the field result returned. Optional, default is 1000.  
field = stackfield(n,d,f,theta,res,min,max); |  min/max: the min/max position where the user wishes to compute the field. 0 corresponds to the bottom of the stack. Optional, default is the span of the multilayer stack.  
  
**Example**

Calculate the field distribution of a 5 layer stack.
    
    
    f = linspace(c/400e-9, c/1000e-9,100); # frequency vector  
    theta = 0:1:45; # angle vector  
    d = [0; 200e-9; 300e-9; 400e-9; 0]; # 5 layers (including air on top and bottom)  
    nf = length(f);  
    nd = length(d);  
      
    # refractive indices for non-dispersive materials  
    n1 = [1; 1.5; 2.5; 1.5; 1];   
    
    # refractive indices for dispersive materials  
    n2 = matrix(nd,nf);  
    n2(1,1:nf) = 1; # air  
    n2(2,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
    n2(3,1:nf) = getfdtdindex("Si (Silicon) - Palik",f,min(f),max(f));  
    n2(4,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
    n2(5,1:nf) = 1; # air  
      
    field1 = stackfield(n1,d,f); # non-dispersive index data, and theta=0  
    field2 = stackfield(n2,d,f,theta); # dispersive data index data, and theta from 0 to 45 deg  
    
    visualize(field1);  
    visualize(field2);

Here's an example for a birefringent slab in air:
    
    
    N_layers = 3;  
    Nfreqs = 100;  
    res = 1000;  
    n = matrix(N_layers, Nfreqs, 3);  
      
    n(1, :, :) = 1;   # air  
    n(2, :, 1) = 2.1; # nx  
    n(2, :, 2) = 2.1; # ny  
    n(2, :, 3) = 2.5; # nz  
    n(3, :, :) = 1;   # air  
      
    d = [0; 1e-6; 0]; # air/ birefringent slab / air  
    f = linspace(c/1e-6, c/1.5e-6, Nfreqs);  
    theta = 0:1:45;  
      
    field = stackfield(n,d,f,theta,res);   
      
    visualize(field);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ stackrt](/hc/en-us/articles/360034406254-stackrt), [ getfdtdindex](/hc/en-us/articles/360034409694-getfdtdindex), [ visualize](/hc/en-us/articles/360034410514-visualize), [ stackdipole](/hc/en-us/articles/360034926493-stackdipole), [STACK product reference manual](/hc/en-us/articles/360037226394)
