<!--
Translation from English documentation
Original command: stackfield
Translation date: 2026-02-04 22:50:15
-->

# stackfield

计算 该 fields within 一个 multilayer stack illuminated 从 below 通过 一个 plane wave 使用 该 analytic transfer 矩阵 method. This 函数 返回 该 E 和 H fields (Es, Ep, Hs, Hp). All results 是 returned 在 一个 single dataset as 一个 函数 的 频率, incidence angle 和 location 在 该 stack (z).

**语法** |  **描述**  
---|---  
field = stackfield(n,d,f); |  n: Refractive index 的 each layer. Size 可以 为

  * Nlayers: isotropic 和 non-dispersive
  * Nlayers x Nfreq: isotropic 和 dispersive
  * Nlayers x 3: anisotropic 和 non-dispersive
  * Nlayers x Nfreq x 3: anisotropic 和 dispersive materials 是 involved.  
NOTE: Only birefringence 在 z (nx=ny≠nz) 是 supported. The commands 将 give 一个 error unless nx=ny.

d: Thickness 的 each layer. Size 是 Nlayers. f: Frequency 向量 使用 一个 长度 的 Nfreq.  
field = stackfield(n,d,f,theta,res); |  theta: Angle 向量, 在 degrees. Optional, default 是 0. res: resolution 在 该 field result returned. Optional, default 是 1000.  
field = stackfield(n,d,f,theta,res,min,max); |  min/max: 该 min/max position 其中 该 用户 wishes 到 compute 该 field. 0 corresponds 到 该 bottom 的 该 stack. Optional, default 是 该 span 的 该 multilayer stack.  
  
**示例**

计算 该 field distribution 的 一个 5 layer stack.
    
    
    f = linspace(c/400e-9, c/1000e-9,100); # 频率 向量  
    theta = 0:1:45; # angle 向量  
    d = [0; 200e-9; 300e-9; 400e-9; 0]; # 5 layers (including air 在 top 和 bottom)  
    nf = 长度(f);  
    nd = 长度(d);  
      
    # refractive indices 用于 non-dispersive materials  
    n1 = [1; 1.5; 2.5; 1.5; 1];   
    
    # refractive indices 用于 dispersive materials  
    n2 = 矩阵(nd,nf);  
    n2(1,1:nf) = 1; # air  
    n2(2,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
    n2(3,1:nf) = getfdtdindex("Si (Silicon) - Palik",f,min(f),max(f));  
    n2(4,1:nf) = getfdtdindex("SiO2 (Glass) - Palik",f,min(f),max(f));  
    n2(5,1:nf) = 1; # air  
      
    field1 = stackfield(n1,d,f); # non-dispersive index 数据, 和 theta=0  
    field2 = stackfield(n2,d,f,theta); # dispersive 数据 index 数据, 和 theta 从 0 到 45 deg  
    
    visualize(field1);  
    visualize(field2);

Here's 一个 example 用于 一个 birefringent slab 在 air:
    
    
    N_layers = 3;  
    Nfreqs = 100;  
    res = 1000;  
    n = 矩阵(N_layers, Nfreqs, 3);  
      
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

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ stackrt](/hc/en-us/articles/360034406254-stackrt), [ getfdtdindex](/hc/en-us/articles/360034409694-getfdtdindex), [ visualize](/hc/en-us/articles/360034410514-visualize), [ stackdipole](/hc/en-us/articles/360034926493-stackdipole), [STACK product reference manual](/hc/en-us/articles/360037226394)
