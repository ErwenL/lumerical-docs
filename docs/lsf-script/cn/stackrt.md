<!--
Translation from English documentation
Original command: stackrt
Translation date: 2026-02-04 22:50:15
-->

# stackrt

计算 该 reflection 和 transmission 的 一个 plane wave through 一个 multi-layer stack 使用 该 analytic transfer 矩阵 method. This 函数 返回 该 fraction 的 transmitted 和 reflected power (Ts, Tp, Rs, Rp), 和 该 complex reflection 和 transmission coefficients (ts, tp, rs, rp), 用于 both S 和 P polarizations. All results 是 returned 在 一个 single dataset as 一个 函数 的 频率 和 incidence angle (optional).

NOTE: From 2022 R1.2, stackrt 脚本 命令 supports fully anisotropic 和 dispersive materials 通过 specifying 该 nine 值 的 该 second-order refractive index tensor. For anisotropic materials, 该 polarization 的 reflected light could vary 从 its incident polarization. The suffix **sp** 和 **ps** denote 如何 polarization 是 changed 在 该 returned power 和 coefficients. **sp** stands 用于 **s** incident 和 **p** reflected/transmitted.

To 计算 该 fields within 该 stack, please see [ stackfield](/hc/en-us/articles/360034406294-stackfield).

**语法** |  **描述**  
---|---  
RT = stackrt(n,d,f); |  n: Refractive index 的 each layer. Size 可以 为

  * Nlayers: isotropic 和 non-dispersive
  * Nlayers x Nfreq: isotropic 和 dispersive
  * Nlayers x 3: anisotropic 和 non-dispersive
  * Nlayers x Nfreq x 3: anisotropic 和 dispersive materials 是 involved.  
NOTE: Only birefringence 在 z (nx=ny≠nz) 是 supported. The commands 将 give 一个 error unless nx=ny.
  * Nlayers x Nfreq x 9: anisotropic 和 dispersive materials 是 involved.  
NOTE: We flatten 该 second-order refractive index tensor into 一个 数组. The third 维度 indicates 该 position 在 该 tensor. For example, 该 position index "1", "2", "3", "4" 和 "5" corresponds 到 n11, n21, n31, n12 和 n22, respectively.

d: Thickness 的 each layer. Size 是 Nlayers. f: Frequency 向量 使用 一个 长度 的 Nfreq.  
RT = stackrt(n,d,f,theta); |  theta: Angle 向量, 在 degrees. Optional.  
  
For more information 在 该 complex coefficients see [Stack optical 求解器 overview](/hc/en-us/articles/360034914653).

### 示例 1: Five-layer stack 使用 isotropic materials

计算 该 reflection, transmission, 和 field distribution 从 一个 5 layer stack.
    
    
    f = linspace(c/400e-9, c/1000e-9,100); # 频率 向量  
    theta = 0:1:45; # angle 向量  
    d = [0; 200e-9; 300e-9; 400e-9; 0]; # air/SiO2/Si/SiO2/air  
    nf = 长度(f);  
    nd = 长度(d);  
      
    # refractive index 的 each layer (non-dispersive)  
    n1 = [1; 1.5; 2.5; 1.5; 1];   
      
    # refractive index 的 each layer (dispersive)  
    n2 = 矩阵(nd,nf);  
    n2(1,1:nf) = 1; # air  
    n2(2,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
    n2(3,1:nf) = getfdtdindex("Si (Silicon) - Palik",f,min(f),max(f));  
    n2(4,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
    n2(5,1:nf) = 1; # air  
      
    RT1 = stackrt(n1,d,f); # non-dispersive index 数据, 和 theta=0  
    RT2 = stackrt(n2,d,f,theta); # dispersive 数据 index 数据, 和 theta 从 0 到 45 deg  
      
    visualize(RT1);  
    visualize(RT2);  
      
    plot(RT1.lambda*1e6,RT1.Rp,RT1.Rs,RT1.Tp,RT1.Ts,"波长 (um)","Power","non-disperisive, theta=0");  
    legend("Rp","Rs","Tp","Ts");  
    image(RT2.lambda*1e6,RT2.theta,RT2.Rp,"波长 (um)","theta (deg)","Rp, dispersive example");

### 示例 2: Birefringent slab 在 air
    
    
    N_layers = 3;  
    Nfreqs = 100;  
    n = 矩阵(N_layers, Nfreqs, 3);  
      
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

### 示例 3: A fully anisotropic 和 dispersive slab 在 air

Download 和 run 该 attached 脚本 stackrt_anisotropic.lsf. 

Please note 该 we use 该 Euler angle definition shown 在 lines 32-46 在 该 脚本 文件 到 rotate 一个 diagonalized permittivity 矩阵 和 那么 derive 该 refractive index 矩阵.

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ stackfield ](/hc/en-us/articles/360034406294-stackfield) , [ multilayer stack calculations ](/hc/en-us/articles/360034914653) , [ getfdtdindex ](/hc/en-us/articles/360034409694-getfdtdindex) , [ visualize ](/hc/en-us/articles/360034410514-visualize)
