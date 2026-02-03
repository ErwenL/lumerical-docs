# gratingm

Returns a vector of the grating order numbers (i.e. zeroeth order, first order) corresponding to the data from the grating function. gratingn gives the order numbers for the first dimension of the data (2D and 3D). gratingm gives the order numbers for the 2nd dimension (3D only). See the grating function documentation for information on interpreting N, M, ux, uy for various monitor orientations. 

**Syntax** |  **Description**  
---|---  
out = gratingm( "monitorname",...);  |  Same arguments as grating function.   
  
**Example**

This example calculates various grating quantities. 
    
    
    mname="T";       # monitor name
    N=gratingn(mname);   # grating order numbers
    M=gratingm(mname);
    u1=gratingu1(mname);  # grating unit vectors (can be converted to theta,phi)
    u2=gratingu2(mname);
    G=grating(mname);   # power to each order (fraction of transmitted power)
    T=transmission(mname); # total power transmitted through monitor (fraction of source power)
    # Print all grating orders to prompt. Results will sum to 1.
    # Then normalize grating results to the injected source power.
    ?G;  # grating results
    ?G*T; # normalized to source power
    # find strength and direction of 0,0 grating order
    nx=find(N,0); # find 0th grating order
    ny=find(M,0); # find 0th grating order
    ?"Grating order 0,0 strength: " + num2str( G(nx,ny) );
    ?"Grating order 0,0 direction: Ux=" +num2str(u1(nx)) + " Uy=" +num2str(u2(ny));
    # image all grating orders, using log scale
    image(u1,u2,G,"ux","uy","Grating order strength","logplot");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ grating ](/hc/en-us/articles/360034927213-grating) , [ gratingn ](/hc/en-us/articles/360034407014-gratingn)
