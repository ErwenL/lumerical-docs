<!--
Translation from English documentation
Original command: stackpurcell
Translation date: 2026-02-04 22:50:15
-->

# stackpurcell

## Results

Analytically calculates the Purcell factor and far-field emission power density for a multilayer stack. For more information on the theory behind this approach, see [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html) example. The usage for this command is very similar to [stackdipole](/hc/en-us/articles/360034926493-stackdipole), but the result returned in this case is a struct that contains the following datasets. The power_density is functions of the emission angle \\( \theta \\) measured from the surface normal (see above image).

**Result** | **描述**  
---|---  
power |  Power [normalized] _Attribute:_ purcell_factor. This 是 该 total power 的 一个 monochromatic dipole at 该 specified position 和 emission 频率 divided 通过 该 power 该 it would radiate 在 一个 homogeneous medium. _Parameters:_ dipole/z, f/lambda  
density |  Power [normalized/steradian] _Attributes:_ upward, downward, upward_into_air, downward_into_air. This 是 该 power density per unit solid angle, as 函数 的 far field emission angle, also normalized 到 该 power 该 would radiate 在 一个 homogeneous medium. _Parameters:_ theta, dipole/z, f/lambda  
  
For more information on the theory behind this approach, see [Stack dipole half-space](/hc/en-us/articles/360042713433) example. Additional discussion on the results can be found at [STACK GUI - OLED Device Introduction.](https://support.lumerical.com/hc/en-us/articles/4402039667091-STACK-GUI-OLED-Device-Introduction)

## Usage

**语法** |  **描述**  
---|---  
result = stackpurcell(n,d,f,z,orientation,res) |  Analytically 计算 该 Purcell factor 和 far-field emission power density 的 一个 multi-layer stack  
result = stackpurcell(n,d,f,z,options)  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
n |  required |  |  向量 |  n: Refractive index 的 each layer. Size 可以 为

  * Nlayers: isotropic 和 non-dispersive
  * Nlayers x Nfreq: isotropic 和 dispersive
  * Nlayers x 3: anisotropic 和 non-dispersive
  * Nlayers x Nfreq x 3: anisotropic 和 dispersive materials 是 involved.  
NOTE: Only birefringence 在 z (nx=ny≠nz) 是 supported. The commands 将 give 一个 error unless nx=ny.

  
d |  required |  |  向量 |  Thickness 的 each layer. Size 是 N_layers.  
f |  required |  |  向量 |  Frequency 向量.  
z |  required |  |  向量 |  Position 的 该 dipoles (0 是 该 bottom 的 该 stack). Size 是 N_dipoles, 和 dipoles 必须 为 located within boundaries.  
orientation |  optional |  "rand" |  单元格 的 strings |  Orientation 的 该 dipoles. Accepts 字符串 或 单元格 数组 as 'orientation' 参数 使用 值:

  * "random" 或 "rand"
  * "vertical" 或 "vert"
  * "horizontal" 或 "horz"

Size 是 N_dipoles.  
res |  optional |  1000 |  数字 |  The resolution 用于 far-field emission angle.  
options |  optional |  |  结构体 |  _In 2021R1.1 和 later_ : This 结构体 可以 为 used 到 pass optional 参数. Passing 此 结构体 allows users 到 specify 该 following 参数: "orientation": defines orientation 的 该 dipole.  "res"/"theta": defines 该 output angles explicitly, instead 的 simply resolution. To specify 该 angles pass them as 一个 向量 "theta" 在 degrees [0,90). "incoherent_propagation": 一个 向量 参数 defines 该 coherent 和 incoherent layers 的 该 stack 使用 0 = coherent propagation 和 1 = incoherent propagation. The dipole cannot 为 located 在 一个 incoherent layer. If 使用 options 那么 all optional 参数, 必须 为 passed through 该 结构体.   
  
## 示例

Explore 该 effect 的 该 dipole position 在 该 angular distribution 的 该 far-field emission:
    
    
    ### Use stackpurcell 到 explore 该 position 的 dipole 在 一个 multilayer stack  
    # 频率 range  
    N_freq = 101;  
    lambda = linspace(380e-9,780e-9,N_freq); # 380nm 到 780nm  
    f = c/lambda;  
      
    # Intialize multilayer geometry  
    n = 矩阵(5,N_freq);  
    d = 矩阵(5,1);  
    #Define optical 和 geometric layer propertie  
    n(1,1:N_freq) = getfdtdindex("Al (Aluminium) - Palik",f,f(1),f(N_freq)); d(1) = 0; # bottom substrate  
    # 注意: 此 reads 该 材料 属性 从 FDTD 材料 database. If you 是 使用 another product, please enter (n,k) explicitly  
    n(2,1:N_freq) = 1.85; d(2) = 60e-9;  
    n(3,1:N_freq) = 1.9; d(3) = 220e-9;  
    n(4,1:N_freq) = 1.8; d(4) = 120e-9;  
    n(5,1:N_freq) = 1.53; d(5) = 0; # top substrate (glass)  
      
    # dipole positions/orientations  
    N_dipole= 51; # 数字 的 dipoles  
    z = linspace( d(2)+1e-10, d(2)+d(3)+1e-10, N_dipole ); # consider positions only within middle dielectric layer  
    orientation = 单元格(N_dipole); # consider only randomly oriented dipoles  
    用于(ii = 1:N_dipole){  
    orientation{ii} = "rand";}  
      
    # angular_res: resolution 用于 emission angle (farfield angle)  
    res = 198;  
    result = stackpurcell(n,d,f,z,orientation,res); # result 是 一个 结构体  
      
    # plot Purcell factor 用于 dipole located at 该 middle 的 该 layer  
    purcell = pinch(result.power.purcell_factor); # size 是 Ndipole 通过 Nfreqs  
    plot(lambda*1e9, pinch(purcell,1,round(N_dipole/2)),'波长 (nm)','Purcell factor');  
      
    # plot far field power density at center 频率  
    theta = pinch(result.density.theta);  
    density = pinch(result.density.upward_into_air); # size 是 res 通过 Ndipole 通过 Nfreqs  
    image(theta, z*1e+9, pinch(density,3,round(N_freq/2)), "far-field angle (degrees)", "dipole position (nm)", num2str(f(round(N_freq/2))*1e-12)+"THz into Air");  
      
      
    
    
    
    # In 2020R1.2  
    incoherent_propagation = [0, 0, 1, 0, 0];  
    options={ "res": 1000, "orientation": 'rand',"incoherent_propagation":incoherent_propagation};  
    stackpurcell(n,d,f,z,options);  
    #或  
    options={ "theta": linspace(0,45,100) , "orientation": 'vert', "incoherent_propagation":incoherent_propagation};  
    stackpurcell(n,d,f,z,options);

**参见**

[Stack optical solver overview](/hc/en-us/articles/360037226394), [ stackrt](/hc/en-us/articles/360034406254-stackrt), [ stackfield](/hc/en-us/articles/360034406294-stackfield), [ stackdipole](/hc/en-us/articles/360034926493-stackdipole), [Stack dipole half-space](https://apps.lumerical.com/stackdipole_and_fdtd_simulations.html), [OLED slab mode analysis](https://apps.lumerical.com/oleds_slab_mode_analysis_of_a_oled_l.html)
