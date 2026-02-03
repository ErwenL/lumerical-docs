# fftk

Returns the spatial wavevector kx associated with the Fourier transform of a function of x. 

$$ k=\text{fftk}(x)=\frac{2\pi}{dx.M}[0,...,(M-1)] $$ 

where M=length(x). 

fftk and all related functions have an option (option 1 below) that controls the format used to store the frequency domain data. When working with spectral data it is not possible to switch between formats; there are no functions to convert between formats. This implies that if you use option1=n to produce a spectrum with fft, then you must also use option1=n if you want to pass that same spectral data to invfft. Similarly, if you use option1=n for fft, then you also need to use option1=n with fftw to get the proper frequency vector corresponding to your spectrum. invfft and fftk work in the same way. 

**Syntax** |  **Description**  
---|---  
out = fftk(x);  |  Returns the spatial wavevector kx associated with a fourier transform of a function of x..   
fftk(x,option1,option2);  |  option1 

  * 1 : the standard FFT (zero frequency is at the first element of the matrix). This is the default option. 


  * 2 : zero frequency is the first element, but frequencies above the Nyquist frequency are removed. 


  * 3 : the FFT is shifted so zero frequency is the central element of the spectrum (more precisely, this means the zero frequency point is at element floor(N/2 + 1), where N is the number of samples). Both positive and negative frequencies are seen 

option2 

  * 0: no zero padding. 
  * 1: zero padding up to the next power of 2 longer than the length of Ex (default). 
  * N: zero pad up to length N if N > length(t). If N <= length(t), it will zero pad up to the next power of 2 longer than the length of t. For the fastest results, N should be a power of 2 and can be entered, for example, as 2^12. 

  
  
**Example**

If Ex is a 2D matrix of spatial field values where Ex contains the field values along the axis vectors x and y, then the following code will image the field and the fourier transform of Ex. 
    
    
    image(x,y,Ex);
    Ix = abs( fft(Ex) )^2; 
    kx = fftk(x); 
    ky = fftk(y); 
    image(kx,ky,Ix); 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ fft ](/hc/en-us/articles/360034926133-fft) , [ fftw ](/hc/en-us/articles/360034926153-fftw) , [ invfft ](/hc/en-us/articles/360034406034-invfft)
