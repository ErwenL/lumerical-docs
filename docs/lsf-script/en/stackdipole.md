# stackdipole

### 

### Results

This function analytically calculates the dipole emission properties of an unpatterned multilayer stack. For structures that can be reduced to 1D this is technique is much more efficient than running fully vectorial simulations with FDTD.

The results are calculated via the following equation. All results returned are functions of the emission angle \\( \theta \\) measured from the surface normal (see above image). Additionally the calculation assumes a current density of 1 \\( A/m^2\\). Limits of the integration are determined by the input dipole spectrum.

$$  
\text {stackdipole}(\theta)=\int_{\lambda}(j \times e f \times st) \left(\frac{r d \times F_{r a d}(\theta, \lambda)}{r d \times F(\lambda)+(1-r d)}\right) \left(\text {photon probability}(\lambda) \times E_{ph}(\lambda)\right) d \lambda  
$$

**Result** | **Description**  
---|---  
radiance |  \\( \frac{W}{\text{steradian }m^2 }\\) Radiance is a measure of the optical power in SI units, as function of \\( \theta \\)  
luminance |  \\( \text{candela }/ m^2 \\) Luminance is a measure of apparent brightness to the human eye.  
X, Y, and Z  | Tristimulus values are basis vectors of the CIE 1931 color space[1], describing the perceived color quantitatively, see [colormatch](/hc/en-us/articles/360034926753) page for mathematical definition.  
  
For more information on the theory behind this approach, see [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html) example. Additional discussion on the results can be found at [STACK GUI - OLED Device Introduction](https://support.lumerical.com/hc/en-us/articles/4402039667091-STACK-GUI-OLED-Device-Introduction), and [OLED Methodology](/hc/en-us/articles/360042225754) chromaticity section. 

NOTE: In 2021R1.1 the length of the results from stack dipole may have changed. Previously singleton dimensions were reduced before output. If you have updated and run into problems you may need to [pinch](/hc/en-us/articles/360034405674) the results yourself.  
---  
  
### Usage

**Syntax** |  **Description**  
---|---  
dipole_emission = stackdipole(n,d,f,z,dipole_spec, orientation,res,direction, ef,st,rd); |  Analytically calculates the dipole emission properties of a multi-layer stack  
dipole_emission = stackdipole(n,d,f,z,dipole_spec, options);  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
n |  required |  |  vector |  n: Refractive index of each layer. Size can be

  * Nlayers: isotropic and non-dispersive
  * Nlayers x Nfreq: isotropic and dispersive
  * Nlayers x 3: anisotropic and non-dispersive
  * Nlayers x Nfreq x 3: anisotropic and dispersive materials are involved.  
NOTE: Only birefringence in z (nx=ny≠nz) is supported. The commands will give an error unless nx=ny.

  
d |  required |  |  vector |  Thickness of each layer. Size is N_layers.  
f |  required |  |  vector |  Frequency vector with a length of Nfreq.  
z |  required |  |  vector |  Position of the dipoles (0 is the bottom of the stack). Size is N_dipoles, and dipoles must be located within boundaries.  
dipole_spec |  required |  |  vector |  Dipole spectrum. This is treated as a power intensity distribution, integrated by midpoint rule in wavelength. The photon probability distribution is calculated by normalizing dipole_spec/f. Size is N_dipoles x length(f).  
orientation |  optional |  "rand" |  cell of strings |  Orientation of the dipoles. Accepts string or cell array as 'orientation' argument with values:

  * "random" or "rand"
  * "vertical" or "vert"
  * "horizontal" or "horz"

Size is N_dipoles.  
res |  optional |  1000 |  number |  The resolution for far-field emission angle.  
direction |  optional |  1 |  number |  Choice of far-field half-space, this can be +1 (top) or -1 (bottom).  
ef |  optional |  1 |  vector |  The exciton fraction. The default value is 1, which means that every carrier results in an exciton. Size is N_dipoles.  
st |  optional |  0.25 |  vector |  The singlet exciton fraction. The default value is 0.25, which means that there are 3 spin triplets per spin-singlet. Size is N_dipoles.  
rd |  optional |  1 |  vector |  The relative decay rate. The default value is 1, which means that every singlet exciton results in a photon and there is no contribution from non-radiative decay processes. Size is N_dipoles.  
options |  optional |  |  struct |  _In 2021R1.1 and later_ : This struct can be used to pass optional arguments. Passing this struct allows users to specify the following parameters: "orientation": defines orientation of the dipole.  "res"/"theta": defines the output angles explicitly, instead of simply resolution. To specify the angles pass them as a vector "theta" in degrees [0,90). "incoherent_propagation": a vector argument defines the coherent and incoherent layers of the stack with 0 = coherent propagation and 1 = incoherent propagation. The dipole cannot be located in an incoherent layer. If using options then all optional arguments, must be passed through the struct.   
  
#### **Example**

Calculate the radiated power of a dipole source in a dielectric half-space.
    
    
    # geometry: halfspace of material n1 and n2
    n1 = 1.5; # lower halfspace
    n2 = 1.0; # upper halfspace  
      
    # source: monochrome 500nm dipole
    wavelength = 500e-9;
    delta = 80e-9; # position: in material n2 delta nm from interface  
    
    angular_res = 173; # resolution for emission angle (farfield angle)  
      
    # set-up for STACK command
    n = [n1; n2]; #STACK optical properties
    d = [0, 2*delta]; #STACK geometric properties
    f = [c/wavelength]; #STACK frequency points
    z = [delta]; #STACK dipole position
    spectrum = [1.0]; #STACK dipole spectrum  
    
    result_unpol = stackdipole(n,d,f,z,spectrum,"rand",angular_res);
    result_Vert = stackdipole(n,d,f,z,spectrum,"vert",angular_res);
    result_Horz = stackdipole(n,d,f,z,spectrum,"horz",angular_res);
    
    plot(result_unpol.theta,result_unpol.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","unpolarized");
    plot(result_Vert.theta,result_Vert.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","vertical P orientation");
    plot(result_Horz.theta,result_Horz.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","horizontal P orientation");  
    
    # calculate power
    sin_theta = sin(pi/180*pinch(result_unpol.theta));
    #integrate power theta 0-pi/2 and phi 0-2pi
    ?total_power_pVert_upward = (0.5*pi)*(2*pi)*integrate(sin_theta*result_Vert.radiance,1,linspace(0,1,angular_res));
    
    
    # In 2020R1.3  
    options={ "res": 173, "orientation": 'rand', "incoherent_propagation": incoherent_propagation};  
    result = stackdipole(n,d,f,z,spectrum,options);  
      
    options={ "theta": linspace(0,30,100), "orientation": 'rand', "incoherent_propagation": incoherent_propagation};  
    result = stackdipole(n,d,f,z,spectrum,options);

### Related publications

  1. CIE Proceedings (1932), 1931. Cambridge: Cambridge University Press.



### See also

[Stack optical solver overview](/hc/en-us/articles/360037226394), [ stackrt](/hc/en-us/articles/360034406254-stackrt), [ stackfield](/hc/en-us/articles/360034406294-stackfield), [ stackpurcell](/hc/en-us/articles/360034926513-stackpurcell), [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html), [OLED slab mode analysis ](https://apps.lumerical.com/oleds_slab_mode_analysis_of_a_oled_l.html)
