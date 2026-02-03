# propagate

Calculates the resulting mode profile of an arbitrary mode after it has propagated through a waveguide for some distance. This is done by decomposing the mode into modes supported by the waveguide. Each supported mode is then propagated through the waveguide. The resulting modes are then added coherently to give the final mode profile. The modes used in this calculation are obtained from one or more FDE simulations.

See the [ overlap ](/hc/en-us/articles/360034405254-overlap) function for more details about overlap and coupling calculations.

**Syntax** | **Description**  
---|---  
out = propagate(mode, d, n1, n2); | 

  * mode: the name of the monitor containing the mode to propagate
  * d: distance to propagate
  * n1: minimum index
  * n2: maximum index
  * out: the name of the resulting dataset created by the propagate command

  
out = propagate(mode, d, n1, n2, x, y); |  Mode alignment can be adjusted before propagate is calculated.

  * x offset
  * y offset

  
  
**Examples**

This example is adapted from the  polarization_rotator.lsf  from [ polarization rotation](/hc/en-us/articles/360042799593). You can download  waveguideA.lms  and  waveguideB.lms  from the [ polarization rotation](/hc/en-us/articles/360042799593) page.

The following script takes the first mode on the mode list from waveguide A and propagates this mode in waveguide B a distance of L_rotation. It generates a plot of |E|^2 for the mode from waveguide A and the mode after propagation in waveguide B.
    
    
    # find the indices of the top 2 modes of waveguide B  
    n1 = getdata("mode1","neff");  
    n2 = getdata("mode2","neff");  
    lambda_0 = c/getdata("mode1","f");  
    
    # estimate the propagation length required to rotate polarization  
    L_rotation = lambda_0/2/real(n1-n2);  
    
    # propagate by L_rotation  
    mode_L = propagate("TE_A",L_rotation,n1,n2);  
    
    ?getdata(mode_L,"accounted_transmission");  
    result:   
    0.845998   
    
    ?getdata(mode_L); # to see a list of the available data  
    f x y z num_modes Ex Ey Ez Hx  
    Hy Hz accounted_transmission accounted_reflection 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) , [ expand ](/hc/en-us/articles/360034926653-expand)
