# czt

Returns the chirped z-transform of a set of data. The czt function is often more convenient than the standard fft functions because you can specify an arbitrary range of k. 

$$ E_k[m]=czt(E_x,x,k)=\sum_nE_x[n].e^{ix[n]k[m]} $$ 

$$ E_k[m1,m2]=czt(E_x,x1,x2,k1,k2)=\sum_{n1,n2}E_x[n1,n2].e^{ix1[n1]k1[m1]+ix2[n2]k2[m2]} $$ 

**Syntax** |  **Description**  
---|---  
out = czt(Ex,t,w);  |  Returns the chirped z-transform of Ex, function of t, at each desired angular frequency w. Note that w must be a linearly spaced set of angular frequencies but can cover any range. It is also possible for inverse transform, ie out=czt(Ex,w,t), see the interpolation example below for details. E can be a matrix where one of the two dimensions is the same as length. The Z-transform is computed along the dimension that matches length, and the output vector will be a matrix where the matched dimension is length(kx) and the other dimension is the same as E. This functionality allows to compute multiple 1D Z-transforms with a single function call.   
czt(Ex,x,y,kx,ky);  |  The two dimensional chirped z-transform. kx and ky must be linearly spaced sets of wavenumbers but can cover any range.   
  
**Example**

This example uses the czt function to determine the frequency components of a signal, as shown in the following figure. 
    
    
    t=linspace(0,50,1000);   # sec
    f=linspace(0,3,200);    # Hz
    x_t=sin(t) + cos(t*2*pi);  # x(t)
    x_f=czt(x_t,t,f*2*pi);   # x(f)
    plot(f,abs(x_f),"f (Hz)"); 

The following is an example of Fourier based interpolation. We can use the fftw function to create the w vector (option3, which shifts the data, is required). A factor of 1/N is necessary for the inverse transform. Also, notice the minus sign on the w vector for the inverse transform. It is possible to use czt to re-sample 2D data. 
    
    
    initial_res = 21;
    final_res = 200;
    # Initial data
    t=linspace(-10,10,initial_res);
    y=sin(t)*exp(-t^2/30);
    plot(t,y,"t","y","Initial");
    # fourier transform
    w=fftw(t,3);
    y_w=czt(y,t,w);
    plot(w,abs(y_w)^2,"w","y_w");
    # re-sample data at 10x
    t_hi=linspace(min(t),max(t),final_res);
    y_hi=1/length(w)*czt(y_w,-w,t_hi); # inverse transform
    plot(t_hi,real(y_hi),"t","y","Final");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ fft ](/hc/en-us/articles/360034926133-fft) , [ fftw ](/hc/en-us/articles/360034926153-fftw)
