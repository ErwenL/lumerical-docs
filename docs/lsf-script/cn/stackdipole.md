<!--
Translation from English documentation
Original command: stackdipole
Translation date: 2026-02-04 22:50:15
-->

# stackdipole

### 

### Results

This 函数 analytically 计算 该 dipole emission 属性 的 一个 unpatterned multilayer stack. For structures 该 可以 为 reduced 到 1D 此 是 technique 是 much more efficient than running fully vectorial simulations 使用 FDTD.

The results 是 calculated via 该 following equation. All results returned 是 functions 的 该 emission angle \\( \theta \\) measured 从 该 surface normal (see above image). Additionally 该 calculation assumes 一个 current density 的 1 \\( A/m^2\\). Limits 的 该 integration 是 determined 通过 该 input dipole spectrum.

$$  
\text {stackdipole}(\theta)=\int_{\lambda}(j \times e f \times st) \left(\frac{r d \times F_{r 一个 d}(\theta, \lambda)}{r d \times F(\lambda)+(1-r d)}\right) \left(\text {photon probability}(\lambda) \times E_{ph}(\lambda)\right) d \lambda  
$$

**Result** | **描述**  
---|---  
radiance |  \\( \frac{W}{\text{steradian }m^2 }\\) Radiance 是 一个 measure 的 该 optical power 在 SI units, as 函数 的 \\( \theta \\)  
luminance |  \\( \text{candela }/ m^2 \\) Luminance 是 一个 measure 的 apparent brightness 到 该 human eye.  
X, Y, 和 Z  | Tristimulus 值 是 basis vectors 的 该 CIE 1931 color space[1], describing 该 perceived color quantitatively, see [colormatch](/hc/en-us/articles/360034926753) page 用于 mathematical definition.  
  
For more information on the theory behind this approach, see [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html) example. Additional discussion on the results can be found at [STACK GUI - OLED Device Introduction](https://support.lumerical.com/hc/en-us/articles/4402039667091-STACK-GUI-OLED-Device-Introduction), and [OLED Methodology](/hc/en-us/articles/360042225754) chromaticity section. 

NOTE: In 2021R1.1 该 长度 的 该 results 从 stack dipole 可能 have changed. Previously singleton dimensions were reduced before output. If you have updated 和 run into problems you 可能 need 到 [pinch](/hc/en-us/articles/360034405674) 该 results yourself.  
---  
  
### Usage

**语法** |  **描述**  
---|---  
dipole_emission = stackdipole(n,d,f,z,dipole_spec, orientation,res,direction, ef,st,rd); |  Analytically 计算 该 dipole emission 属性 的 一个 multi-layer stack  
dipole_emission = stackdipole(n,d,f,z,dipole_spec, options);  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
n |  required |  |  向量 |  n: Refractive index 的 each layer. Size 可以 为

  * Nlayers: isotropic 和 non-dispersive
  * Nlayers x Nfreq: isotropic 和 dispersive
  * Nlayers x 3: anisotropic 和 non-dispersive
  * Nlayers x Nfreq x 3: anisotropic 和 dispersive materials 是 involved.  
NOTE: Only birefringence 在 z (nx=ny≠nz) 是 supported. The commands 将 give 一个 error unless nx=ny.

  
d |  required |  |  向量 |  Thickness 的 each layer. Size 是 N_layers.  
f |  required |  |  向量 |  Frequency 向量 使用 一个 长度 的 Nfreq.  
z |  required |  |  向量 |  Position 的 该 dipoles (0 是 该 bottom 的 该 stack). Size 是 N_dipoles, 和 dipoles 必须 为 located within boundaries.  
dipole_spec |  required |  |  向量 |  Dipole spectrum. This 是 treated as 一个 power intensity distribution, integrated 通过 midpoint rule 在 波长. The photon probability distribution 是 calculated 通过 normalizing dipole_spec/f. Size 是 N_dipoles x 长度(f).  
orientation |  optional |  "rand" |  单元格 的 strings |  Orientation 的 该 dipoles. Accepts 字符串 或 单元格 数组 as 'orientation' 参数 使用 值:

  * "random" 或 "rand"
  * "vertical" 或 "vert"
  * "horizontal" 或 "horz"

Size 是 N_dipoles.  
res |  optional |  1000 |  数字 |  The resolution 用于 far-field emission angle.  
direction |  optional |  1 |  数字 |  Choice 的 far-field half-space, 此 可以 为 +1 (top) 或 -1 (bottom).  
ef |  optional |  1 |  向量 |  The exciton fraction. The default 值 是 1, 该 means 该 every carrier results 在 一个 exciton. Size 是 N_dipoles.  
st |  optional |  0.25 |  向量 |  The singlet exciton fraction. The default 值 是 0.25, 该 means 该 there 是 3 spin triplets per spin-singlet. Size 是 N_dipoles.  
rd |  optional |  1 |  向量 |  The relative decay rate. The default 值 是 1, 该 means 该 every singlet exciton results 在 一个 photon 和 there 是 no contribution 从 non-radiative decay processes. Size 是 N_dipoles.  
options |  optional |  |  结构体 |  _In 2021R1.1 和 later_ : This 结构体 可以 为 used 到 pass optional 参数. Passing 此 结构体 allows users 到 specify 该 following 参数: "orientation": defines orientation 的 该 dipole.  "res"/"theta": defines 该 output angles explicitly, instead 的 simply resolution. To specify 该 angles pass them as 一个 向量 "theta" 在 degrees [0,90). "incoherent_propagation": 一个 向量 参数 defines 该 coherent 和 incoherent layers 的 该 stack 使用 0 = coherent propagation 和 1 = incoherent propagation. The dipole cannot 为 located 在 一个 incoherent layer. If 使用 options 那么 all optional 参数, 必须 为 passed through 该 结构体.   
  
#### **示例**

计算 该 radiated power 的 一个 dipole 源 在 一个 dielectric half-space.
    
    
    # geometry: halfspace 的 材料 n1 和 n2
    n1 = 1.5; # lower halfspace
    n2 = 1.0; # upper halfspace  
      
    # 源: monochrome 500nm dipole
    波长 = 500e-9;
    delta = 80e-9; # position: 在 材料 n2 delta nm 从 interface  
    
    angular_res = 173; # resolution 用于 emission angle (farfield angle)  
      
    # 设置-up 用于 STACK 命令
    n = [n1; n2]; #STACK optical 属性
    d = [0, 2*delta]; #STACK geometric 属性
    f = [c/波长]; #STACK 频率 points
    z = [delta]; #STACK dipole position
    spectrum = [1.0]; #STACK dipole spectrum  
    
    result_unpol = stackdipole(n,d,f,z,spectrum,"rand",angular_res);
    result_Vert = stackdipole(n,d,f,z,spectrum,"vert",angular_res);
    result_Horz = stackdipole(n,d,f,z,spectrum,"horz",angular_res);
    
    plot(result_unpol.theta,result_unpol.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","unpolarized");
    plot(result_Vert.theta,result_Vert.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","vertical P orientation");
    plot(result_Horz.theta,result_Horz.radiance,"emission angle (degrees)","power/steradian  (W/steradian/m^2)","horizontal P orientation");  
    
    # 计算 power
    sin_theta = sin(pi/180*pinch(result_unpol.theta));
    #integrate power theta 0-pi/2 和 phi 0-2pi
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
