# stackpurcell

## Results

Analytically calculates the Purcell factor and far-field emission power density for a
multilayer stack. For more information on the theory behind this approach, see
[Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html)
example. The usage for this command is very similar to [stackdipole](./stackdipole.md),
but the result returned in this case is a struct that contains the following datasets.
The power_density is functions of the emission angle \\( \\theta \\) measured from the
surface normal (see above image).

| **Result** | **Description**                                                                                                                                                                                                                                                                                            |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| power      | Power [normalized] _Attribute:_ purcell_factor. This is the total power of a monochromatic dipole at the specified position and emission frequency divided by the power that it would radiate in a homogeneous medium. _Parameters:_ dipole/z, f/lambda                                                    |
| density    | Power [normalized/steradian] _Attributes:_ upward, downward, upward_into_air, downward_into_air. This is the power density per unit solid angle, as function of far field emission angle, also normalized to the power that would radiate in a homogeneous medium. _Parameters:_ theta, dipole/z, f/lambda |

For more information on the theory behind this approach, see
[Stack dipole half-space](https://optics.ansys.com/hc/en-us/articles/360042713433)
example. Additional discussion on the results can be found at
[STACK GUI - OLED Device Introduction.](https://support.lumerical.com/hc/en-us/articles/4402039667091-STACK-GUI-OLED-Device-Introduction)

## Usage

| **Syntax**                                     | **Description**                                                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| result = stackpurcell(n,d,f,z,orientation,res) | Analytically calculates the Purcell factor and far-field emission power density of a multi-layer stack |
| result = stackpurcell(n,d,f,z,options)         |                                                                                                        |
| **Parameter**                                  |                                                                                                        |
| ---                                            | ---                                                                                                    |
| n                                              | required                                                                                               |

- Nlayers: isotropic and non-dispersive
- Nlayers x Nfreq: isotropic and dispersive
- Nlayers x 3: anisotropic and non-dispersive
- Nlayers x Nfreq x 3: anisotropic and dispersive materials are involved.\
  NOTE: Only birefringence in z (nx=ny≠nz) is supported. The commands will give an error
  unless nx=ny.

d | required | | vector | Thickness of each layer. Size is N_layers.\
f | required | | vector | Frequency vector.\
z | required | | vector | Position of the dipoles (0 is the bottom of the stack). Size
is N_dipoles, and dipoles must be located within boundaries.\
orientation | optional | "rand" | cell of strings | Orientation of the dipoles. Accepts
string or cell array as 'orientation' argument with values:

- "random" or "rand"
- "vertical" or "vert"
- "horizontal" or "horz"

Size is N_dipoles.\
res | optional | 1000 | number | The resolution for far-field emission angle.\
options | optional | | struct | _In 2021R1.1 and later_ : This struct can be used to
pass optional arguments. Passing this struct allows users to specify the following
parameters: "orientation": defines orientation of the dipole. "res"/"theta": defines the
output angles explicitly, instead of simply resolution. To specify the angles pass them
as a vector "theta" in degrees \[0,90). "incoherent_propagation": a vector argument
defines the coherent and incoherent layers of the stack with 0 = coherent propagation
and 1 = incoherent propagation. The dipole cannot be located in an incoherent layer. If
using options then all optional arguments, must be passed through the struct.

## Example

Explore the effect of the dipole position on the angular distribution of the far-field
emission:

```
### Use stackpurcell to explore the position of dipole in a multilayer stack  
# frequency range  
N_freq = 101;  
lambda = linspace(380e-9,780e-9,N_freq); # 380nm to 780nm  
f = c/lambda;  
  
# Intialize multilayer geometry  
n = matrix(5,N_freq);  
d = matrix(5,1);  
#Define optical and geometric layer propertie  
n(1,1:N_freq) = getfdtdindex("Al (Aluminium) - Palik",f,f(1),f(N_freq)); d(1) = 0; # bottom substrate  
# Note: this reads the material properties from FDTD material database. If you are using another product, please enter (n,k) explicitly  
n(2,1:N_freq) = 1.85; d(2) = 60e-9;  
n(3,1:N_freq) = 1.9; d(3) = 220e-9;  
n(4,1:N_freq) = 1.8; d(4) = 120e-9;  
n(5,1:N_freq) = 1.53; d(5) = 0; # top substrate (glass)  
  
# dipole positions/orientations  
N_dipole= 51; # number of dipoles  
z = linspace( d(2)+1e-10, d(2)+d(3)+1e-10, N_dipole ); # consider positions only within middle dielectric layer  
orientation = cell(N_dipole); # consider only randomly oriented dipoles  
for(ii = 1:N_dipole){  
orientation{ii} = "rand";}  
  
# angular_res: resolution for emission angle (farfield angle)  
res = 198;  
result = stackpurcell(n,d,f,z,orientation,res); # result is a struct  
  
# plot Purcell factor for dipole located at the middle of the layer  
purcell = pinch(result.power.purcell_factor); # size is Ndipole by Nfreqs  
plot(lambda*1e9, pinch(purcell,1,round(N_dipole/2)),'wavelength (nm)','Purcell factor');  
  
# plot far field power density at center frequency  
theta = pinch(result.density.theta);  
density = pinch(result.density.upward_into_air); # size is res by Ndipole by Nfreqs  
image(theta, z*1e+9, pinch(density,3,round(N_freq/2)), "far-field angle (degrees)", "dipole position (nm)", num2str(f(round(N_freq/2))*1e-12)+"THz into Air");  
  
  



# In 2020R1.2  
incoherent_propagation = [0, 0, 1, 0, 0];  
options={ "res": 1000, "orientation": 'rand',"incoherent_propagation":incoherent_propagation};  
stackpurcell(n,d,f,z,options);  
#or  
options={ "theta": linspace(0,45,100) , "orientation": 'vert', "incoherent_propagation":incoherent_propagation};  
stackpurcell(n,d,f,z,options);
```

**See Also**

[Stack optical solver overview](https://optics.ansys.com/hc/en-us/articles/360037226394),
[ stackrt](./stackrt.md), [ stackfield](./stackfield.md),
[ stackdipole](./stackdipole.md),
[Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html),
[OLED slab mode analysis](https://apps.lumerical.com/oleds_slab_mode_analysis_of_a_oled_l.html)
