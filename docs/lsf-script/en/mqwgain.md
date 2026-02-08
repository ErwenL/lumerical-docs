# mqwgain

The script command mqwgain calculates gain and spontaneous emission for TE and TM modes
in multiple quantum well structures using the 4x4 k.p electronic band structure method
[1-3]. The conduction band is parabolic, while heavy and light hole valence bands are
mixed according to the 4x4 k.p method and they are nonparabolic.

The solver includes a material database of common III-V semiconductors, ternary alloys,
and quaternary alloys. Material properties may be generated automatically for arbitrary
alloy compositions or may be input manually. The supported materials are listed in the
table below:

| **III-V semiconductors** | **Ternary alloys** | **Quaternary Alloys** |
| ------------------------ | ------------------ | --------------------- |
| AlAs                     | AlxGa1-xAs         | InxGa1-xAsyP1-y       |
| GaAs                     | AlxGa1-xP          | AlxGayIn1-x-yAs       |
| InAs                     | AlxIn1-xP          |                       |
| AlP                      | GaAsxP1-x          |                       |
| GaP                      | InxAl1-xAs         |                       |
| InP                      | InAsxP1-x          |                       |
| InxGa1-xAs               |                    |                       |
| InxGa1-xP                |                    |                       |

When database materials are used, the properties of ternary alloys P(AxB1−xD) are
interpolated from the corresponding properties of the base materials (P(AD) and P(BD))
according to the formula

$$ P\\left(A_x
B\_{1-x}D\\right)=xP\\left(AD\\right)+\\left(1-x\\right)P\\left(BD\\right)+x\\left(1-x\\right)C,
$$

where x is the composition fraction and C is the bowing parameter (quadratic
coefficient).

Quaternary alloys of type AxB1-xCyD1-y (two group III and two group V elements) are
composed from the interpolation of ternary alloy constituents \[4\]:

$$
P\\left(A_xB\_{1-x}C_yD\_{1-y}\\right)=\\frac{x\\left(1-x\\right)\\left[\\left(1-y\\right)P\\left(A_xB\_{1-x}D\\right)+yP\\left(A_xB\_{1-x}C\\right)\\right]+y\\left(1-y\\right)\\left[xP\\left(AC_yD\_{1-y}\\right)+\\left(1-x\\right)P\\left(BC_yD\_{1-y}\\right)\\right]}{x\\left(1-x\\right)+y\\left(1-y\\right)},
$$

for composition fractions x and y. For example, a combination of the properties of
InxGa1−xP, InxGa1−xAs, InAsyP1−y, and GaAsyP1−y is used to define the properties of
InxGa1−xAsyP1−y.

Quaternary alloys of type AxByC1-x-yD (three group III elements and one group V element)
are composed from the interpolation of ternary alloy constituents \[4\]:

$$
P\\left(A_xB_yC\_{1-x-y}D\\right)=\\frac{xyP\\left(A\_{1-u}B_uD\\right)+y(1-x-y)P\\left(B\_{1-v}C\_{v}D\\right)+x(1-x-y)P\\left(A\_{1-w}C\_{w}D\\right)}{xy+y(1-x-y)+x(1-x-y)},
$$

for composition fractions x and y and u = (1-x+y)/2, v = (2-x-2y)/2, w = (2-2x-y)/2. For
example, a combination of the properties of Al1-uGauAs, Ga1-vInvAs, and Al1-wInwAs, is
used to define the properties of AlxGayIn1-x-yAs.

| **Syntax**                                                         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| result = mqwgain(stack_properties, simulation_parameters, config); | stack_properties: struct with fields that define MQW stack geometry and material properties. simulation_parameters: struct with fields that define simulation parameters for which the output will be calculated. config: struct with fields that configure the behavior of the simulation. result: struct or a cell of structs in case of multiple partitions, where each struct contains 4 datasets: spatial band diagram, band structure in (E,k) space, spatial wave functions for each (E,k) state, and emission coefficients. |
| result = mqwgain(stack_properties, simulation_parameters);         | same as above, but using all default values for the fields in the config struct.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Stack properties

**stack_properties** is a struct with the following fields:

| **Field** | **Default**                                         | **Units** | **Type** | **Description**                                                                                                                                                                                                                                 |
| --------- | --------------------------------------------------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| gamma     |                                                     | eV        | Scalar   | Linewidth broadening due to intraband relaxation rate. Represents full width at half maximum of a Lorentzian.                                                                                                                                   |
| neff      |                                                     |           | Matrix   | Effective index vs. frequency. Two-column matrix: the first column is the frequency (Hz), and the second column is the effective index. Effective index values will be linearly interpolated onto the photon frequency grid for the simulation. |
| length    |                                                     | m         | Matrix   | The thickness of each layer, Nx1 array (N layers)                                                                                                                                                                                               |
| material  |                                                     |           | Cell     | Material definitions, length N cell array. See below for a description of options to specify material properties.                                                                                                                               |
| strain    | 0                                                   | (a0-a)/a  | Matrix   | Strain in each layer as a fraction, negative values for compressive strain. Nx1 array (N layers).                                                                                                                                               |
| vb        | Not included                                        |           | Struct   | Specification for valence band absolute energy. If not defined, then material.vb field is used by default.                                                                                                                                      |
| eps       | quantum mechanical average over MQW stack materials |           | Scalar   | Relative static permittivity. Needed when exciton model is used.                                                                                                                                                                                |

**stack_properties.material** is a cell array (one element per layer) where each element
is a struct. The struct can be defined in 2 ways.

First, automatically generated by calling [ buildmqwmaterial ](./buildmqwmaterial.md)
script command:

| **Coefficient** | **Units** | **Description**                                                          |
| --------------- | --------- | ------------------------------------------------------------------------ |
| eg              | eV        | Band gap                                                                 |
| ep              | eV        | Energy parameter for the optical matrix element                          |
| me              | 1/m0      | Electron effective mass                                                  |
| gamma1          |           | Luttinger parameter                                                      |
| gamma2          |           | Luttinger parameter                                                      |
| gamma3          |           | Luttinger parameter                                                      |
| ac              | eV        | Conduction band deformation potential                                    |
| av              | eV        | Valence band deformation potential                                       |
| b               | eV        | Valence band deformation potential                                       |
| c11             | N/m2      | Elastic stiffness coefficient                                            |
| c12             | N/m2      | Elastic stiffness coefficient                                            |
| lc              | m         | Lattice constant                                                         |
| vb              | eV        | Valence band absolute energy (all layers should have a common reference) |
| eps             |           | Relative static permittivity                                             |

Second, using **stack_properties.material:**

| **Coefficient**   | **Type** | **Description**                                 |
| ----------------- | -------- | ----------------------------------------------- |
| database_material | String   | Name of the material                            |
| x                 | 0        | Material composition (if ternary or quaternary) |
| y                 | 0        | Material composition (if quaternary)            |

## Stack properties

**stack_properties.vb** is a struct with the following fields:

| **Field** | **Default** | **Units** | **Type** | **Description**                                                                                                    |
| --------- | ----------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| method    | palankovski |           | String   | Method for calculating valence band offsets. If “direct” is specified, the offsets must be provided (see offsets). |
| offsets   |             | eV        | Matrix   | Directly specified valence band offsets, Nx1 array (N layers).                                                     |

**simulation_parameters** is a struct with the following fields:

| **Field**       | **Default**               | **Units** | **Type** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------- | ------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T               |                           | K         | Scalar   | Simulation temperature. This parameter is ignored when the exciton model is used and full depletion of the quantum wells is assumed (valence band full, conduction band empty).                                                                                                                                                                                                                                                                                                                                           |
| V               |                           | V         | Matrix   | Electrostatic potential vs. position. A two-column matrix, with position (m) specified in the first column and potential (eV) specified in the second column. Potential values will be linearly interpolated onto the simulation grid. The first layer is assumed to start at z=0.                                                                                                                                                                                                                                        |
| kt              | linspace(0,2*pi/a*0.1,51) | 1/m       | Matrix   | Transverse k values are used in the band structure calculation. When the exciton model is turned on only the number of kt points is considered, while the values are ignored and instead defined based on a special quadrature method used by the solver.                                                                                                                                                                                                                                                                 |
| stackpartitions | empty matrix              |           | Matrix   | Matrix of size (number of partitions) x 2, where each row represents the start and end layer index for one partition using 1-based indexing. Start and end layers should be barriers. For example, [1,3;3,5] represents two partitions where the first partition contains layers (1,2,3) and the second partition contains layers (3,4,5), where layers 1, 3, and 5 represent barriers.                                                                                                                                   |
| cden            |                           | 1/m3      | Matrix   | Carrier density array. Matrix of size (number of partitions) x (number of different density profiles). If there is more than one partition this enables defining spatially dependent density, where each partition has a different density. If there is no partitioning, each density profile is a scalar representing the average density over the entire stack. This parameter is ignored when the exciton model is used and full depletion of the quantum wells is assumed (valence band full, conduction band empty). |
| phfreq          |                           | Hz        | Matrix   | Photon frequency array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

**config** is a struct with the following fields:

| **Field**          | **Default** | **Units** | **Type**         | **Description**                                                                                                                                                                                                                                                                          |
| ------------------ | ----------- | --------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bcs                | See below   | See below | Struct           | Boundary conditions struct.                                                                                                                                                                                                                                                              |
| dz                 | 1e-10       | m         | Scalar           | Grid spacing ≥ 1Å.                                                                                                                                                                                                                                                                       |
| numeigenvalues     | 30          |           | Scalar           | The maximum number of bands to calculate by the eigensolver at each kt.                                                                                                                                                                                                                  |
| numqwsubbandsCB    | 2           |           | Scalar           | The maximum number of conduction subbands to use for exciton mixing. Increasing this value results in a more accurate but longer simulation. In general, around 2-4 subbands per coupled well should be used.                                                                            |
| numqwsubbandsVB    | 2           |           | Scalar           | The maximum number of valence subbands to use for exciton mixing. Increasing this value results in a more accurate but longer simulation. This does not include spin, so the actual number of subbands is 2x this value. Generally, around 2-4 subbands per coupled well should be used. |
| numqwsubbands      | 2           |           | Scalar           | The maximum number of subbands (both conduction and valence) to use for exciton mixing. (This field is deprecated. Recommend using numqwsubbandsCB/VB instead.)                                                                                                                          |
| materialdb         |             |           | String or struct | A string specifying the path to the material database or empty struct for the default database.                                                                                                                                                                                          |
| cbvalley           | Gamma       |           | String           | Choose the conduction band valley for interpolation of material properties: “Gamma”, “X”, “L”, or “All” (default is “Gamma”; option “All” uses the lowest band gap to select).                                                                                                           |
| reusebandstructure | false       |           | Boolean          | If there is partitioning and this option is true, the MQW band structure calculated in the first partition will be reused in all other partitions, reducing simulation time. This is a good approximation whenever partitions have a similar band diagram (up to a constant shift).      |
| exciton            | false       |           | Boolean          | Turns on exciton model.                                                                                                                                                                                                                                                                  |
| wfthetadependence  | false       |           | Boolean          | Turns on the angular dependence of the exciton wave function in the plane of quantum wells.                                                                                                                                                                                              |

**config.bcs** is a struct with the following fields:

| **Field**      | **Default**                                   | **Units**        | **Type** | **Description**                                                                                                                                                                                                                                                                            |
| -------------- | --------------------------------------------- | ---------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| pmlactive      | false                                         |                  | Boolean  | Enable perfectly matched layer at boundaries.                                                                                                                                                                                                                                              |
| pmlcutoff      | [1e-2,1e-2]                                   |                  | Matrix   | Threshold ratio (PML probability density)/(MQW probability density), one for conduction and one for valence bands, to reject eigenstates with excess conduction and valence band probability densities located in the PMLs, 2x1 array. The QW bound states are those below this threshold. |
| pmllength      | [10e-9,10e-9]                                 | m                | Matrix   | PML thickness for left and right boundaries, 2x1 array.                                                                                                                                                                                                                                    |
| pmlcoefficient | \[0.5+1i*0.5,0.5+1i*0.5,-1+1i*1.4,-1+1i*1.4\] |                  | Matrix   | PML complex coordinate stretching coefficients. First two elements are for left and right PML for the conduction band and the other two for the valence band.                                                                                                                              |
| hwcutoff       | [5e-4,5e-4]                                   | \\( A^{-3/2} \\) | Matrix   | Threshold wave function slope, one for conduction and one for valence bands, to reject eigenstates that do not decay enough at the left and right hard-wall boundaries, 2x1 array. The QW bound states are those below this threshold.                                                     |

**result** is a cell of structs for each partition if there is partitioning, or a struct
if there is no partitioning, where structs contain the following fields:

| **Syntax**    | **Type** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| banddiagram   | dataset  | Conduction and valence band edge including strain, but not including quantum confinement effects (i.e. subbands).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| bandstructure | dataset  | (E,kt) band diagram for conduction and valence bands. With the exciton model turned off the attributes are: conduction_band, valence_band_lo, and valence_band_up, where the 4x4 k.p basis in the valence band is transformed into two 2x2 bases (lo for lower and up for upper). For more information look at references [1] and [2]. With the exciton model turned on the attributes are: conduction_band, valence_band, with the 4x4 k.p basis in the valence band (the basis is not transformed). Parameters are kt and subband.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| wavefunction  | dataset  | Spatial wavefunction for each (E,kt) point. With the exciton model turned on the attributes are: conduction_band_1, valence_band_lo_1, valence_band_lo_2, valence_band_up_1, valence_band_up_2, where the 4x4 k.p basis in the valence band is split into two 2x2 bases (lo for lower and up for upper) and the vectors in each 2x2 basis are designated with 1 and 2. For more information look at references [1] and [2]. With the exciton model turned on the attributes are: conduction_band_1, valence_band_1, valence_band_2, valence_band_3, valence_band_4, with the 4x4 k.p basis in the valence band (the basis is not transformed) and the vectors in the 4x4 basis designated with 1, 2, 3, and 4. Parameters are coordinate, kt, and subband.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ome           | dataset  | Optical matrix element. With excitons turned off: Magnitude squared of the momentum matrix element divided by the free electron mass. In the units of \\(eV\\). Attributes are ome_lo_TE, ome_lo_TM, ome_up_TE, ome_up_TM, where TE and TM designate optical modes and up and lo refer to the 2x2 bases, same as for the bandstructure and wavefunction. Parameters are kt (transverse wave vector), CBsubband (conduction band subband index) and VBsubband (valence band subband index). With excitons turned on: Oscillator strength per unit area in the units of \\(1/nm^2\\). Attributes are ome_TE and ome_TM where TE and TM designate optical modes. Parameters are the exciton orbital quantum number (orbital) and angular momentum quantum number (angularMomentum).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| emission      | dataset  | Gain and spontaneous emission coefficients in the units of [1/m]. Attributes are: spontaneous_TE, spontaneous_TM, stimulated_TE, stimulated_TM, where TE and TM stand for electromagnetic modes. Parameters are: frequency/energy/wavelength and ndensity (charge density). Emission coefficients are calculated for the total stack thickness, including barriers. If only the quantum well thickness is of interest, excluding barriers, these coefficients should be scaled by multiplying with (total length)/(total QW length). It is important to ensure that emission coefficients apply only to the thickness used for the calculation of the mode overlap with the gain region. When using partitioning, there will be overlapping barriers between different partitions, e.g. simulation_parameters.stackpartitions = [1,3;3,5], where 1, 3, and 5 are barriers. In that case emission coefficients for each partition again apply to the total thickness of that partition, meaning there may be some double-counting with respect to the mode overlap region thickness. To avoid this, emission coefficients can be scaled to apply to quantum wells only, or to apply to a portion of the partition that does not overlap with adjacent partitions. When the exciton model is turned on the attributes become: absorption_TE, absorption_TM. These represent the absorption coefficients (negative gain) in the units of [1/m]. The spontaneous emission is not calculated due to the assumption of the depleted carrier density in the quantum wells. |
| ex            | dataset  | Exciton energies Ex. Exciton energies are a function of exciton orbital quantum number (orbital) and angular momentum quantum number (angularMomentum).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| phix          | dataset  | Exciton wavefunctions PhiX in the momentum (in-plane wavevector) space. The wave function coefficients are parametrized in terms of conduction band subband index (cSubband), valence band subband index (vSubband), transverse wave vector (kt), and angular momentum quantum number (angularMomentum), and orbital quantum number (orbital).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Material Definitions

Material parameters are important for the accurate calculation of the MQW band structure
and emission characteristics. Many parameters are used to model the optical and
electronic material behavior. Some parameters for alloys of compound semiconductors are
not available from experiments and must be generated from interpolation of known values.
Experimental results may depend on growth conditions and layer thickness, and adjustment
of some material parameters may be necessary to obtain agreement with measurements.

Lumerical provides a default material database with the MQW gain solver. These
parameters are used automatically when the layer materials are defined by a name and
composition fraction. The following code sets the material in layer 2 as Al 0.41 Ga 0.59
As

```
materials = cell(3); 
#... 
materials{2} = struct; 
materials{2}.database_material = "AlGaAs"; 
materials{2}.x = 0.41; 
```

You can also choose to use your own material database (in the same format) instead of
the default material database supplied by Lumerical. By specifying the path of that
database in the simulation configuration struct, you can instruct the solver to use
those material definitions, e.g.

```
config.materialdb = "/home/auser/myfolder/my_material_db.json"; 
```

Using this approach, the material parameters of the compound semiconductors can be
modified, but the default interpolation used by the solver will still be applied to
generate parameters for ternary and quaternary semiconductors. The assignment of
materials to layers does not change.

Alternately, a material definition can be read directly from a material database
(default or custom) and loaded as a struct into the script workspace using the
[buildmqwmaterial ](./buildmqwmaterial.md) command. For example,

```
mymat = buildmqwmaterial("/home/auser/myfolder/my_material_db.json", 300, "InAlAs", 0.47);  
```

will read the necessary properties from the material database and build a material
definition at T=300K with composition fraction x=0.47 for In 0.47 Al 0.53 As. The result
is a structure with the coefficients required by the MQW solver. A struct with these
fields can be assigned to a material layer and used directly by the solver, e.g.

```
materials = cell(3); 
#... 
materials{2} = buildmqwmaterial("/home/auser/myfolder/my_material_db.json", 300, "InAlAs", 0.47);
```

### References

[1] D. Ahn et al., J. Appl. Phys. 64, 4056 (1988)

[2] S. L. Chuang, Physics of Optoelectronic Devices

[3] Chuang, Phys. Rev. B, 43, 9649 (1991)

[4] Vurgaftman et al., J. Appl. Phys., 89, 5815 (2001)

[5] C. Y.-P. Chao et al., Phys. Rev. B, 48, 8210 (1993)

### See Also

[ buildmqwmaterial](./buildmqwmaterial.md),
[mqwindex](https://optics.ansys.com/hc/en-us/articles/360041072553),
[edge emitting laser example](https://apps.lumerical.com/mqw-edge-emitting-laser.html),
[MQW product reference manual](https://optics.ansys.com/hc/en-us/articles/360038463833)
