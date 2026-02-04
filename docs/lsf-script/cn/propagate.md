<!--
Translation from English documentation
Original command: propagate
Translation date: 2026-02-04 22:50:14
-->

# propagate

计算 该 resulting mode profile 的 一个 arbitrary mode after it has propagated through 一个 waveguide 用于 some distance. This 是 done 通过 decomposing 该 mode into modes supported 通过 该 waveguide. Each supported mode 是 那么 propagated through 该 waveguide. The resulting modes 是 那么 added coherently 到 give 该 final mode profile. The modes used 在 此 calculation 是 obtained 从 one 或 more FDE simulations.

See 该 [ overlap ](/hc/en-us/articles/360034405254-overlap) 函数 用于 more details about overlap 和 coupling calculations.

**语法** | **描述**  
---|---  
out = propagate(mode, d, n1, n2); | 

  * mode: 该 name 的 该 监视器 containing 该 mode 到 propagate
  * d: distance 到 propagate
  * n1: minimum index
  * n2: maximum index
  * out: 该 name 的 该 resulting dataset created 通过 该 propagate 命令

  
out = propagate(mode, d, n1, n2, x, y); |  Mode alignment 可以 为 adjusted before propagate 是 calculated.

  * x offset
  * y offset

  
  
**示例**

This example 是 adapted 从 该  polarization_rotator.lsf  从 [ polarization rotation](/hc/en-us/articles/360042799593). You 可以 download  waveguideA.lms  和  waveguideB.lms  从 该 [ polarization rotation](/hc/en-us/articles/360042799593) page.

The following 脚本 takes 该 first mode 在 该 mode list 从 waveguide A 和 propagates 此 mode 在 waveguide B 一个 distance 的 L_rotation. It generates 一个 plot 的 |E|^2 用于 该 mode 从 waveguide A 和 该 mode after propagation 在 waveguide B.
    
    
    # find 该 indices 的 该 top 2 modes 的 waveguide B  
    n1 = getdata("mode1","neff");  
    n2 = getdata("mode2","neff");  
    lambda_0 = c/getdata("mode1","f");  
    
    # estimate 该 propagation 长度 required 到 rotate polarization  
    L_rotation = lambda_0/2/real(n1-n2);  
    
    # propagate 通过 L_rotation  
    mode_L = propagate("TE_A",L_rotation,n1,n2);  
    
    ?getdata(mode_L,"accounted_transmission");  
    result:   
    0.845998   
    
    ?getdata(mode_L); # 到 see 一个 list 的 该 available 数据  
    f x y z num_modes Ex Ey Ez Hx  
    Hy Hz accounted_transmission accounted_reflection 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) , [ expand ](/hc/en-us/articles/360034926653-expand)
