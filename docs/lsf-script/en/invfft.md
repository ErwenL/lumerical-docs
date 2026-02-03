# invfft

Computes the 1D, 2D or 3D inverse Fast Fourier Transform (FFT) of a matrix. In the 1D case the transform is given by 

$$E_x[m]=\text{invfft}(E_w)=\frac{1}{N}\sum_{n-1}^NE_w[n]. e^{-(\frac{2\pi i}{N})(n-1)(m-1)} $$ 

The inverse FFT, FFT and all related functions have an option (option 1 below) that controls the format used to store the frequency domain data. When working with spectral data it is not possible to switch between formats; there are no functions to convert between formats. This implies that if you use option1=n to produce a spectrum with fft, then you must also use option1=n if you want to pass that same spectral data to invfft. Similarly, if you use option1=n for fft, then you also need to use option1=n with fftw to get the proper frequency vector corresponding to your spectrum. invfft and fftk work in the same way. 

**Syntax** |  **Description**  
---|---  
out = invfft(Ew);  |  Returns the inverse fast Fourier transform of Ew. Ew can 1D,2D or 3D.   
out = invfft(Ew,option1,option2);  |  option1  This option controls the format used to store the frequency domain data. The options are: 

  * 1 : the standard FFT (zero frequency is at the first element of the matrix). This is the default option. 
  * 2 : zero frequency is the first element, but only data up to and including the Nyquist frequency is stored. This option is only useful for real valued, 1D time/spatial signals. 
  * 3 : the FFT is shifted so zero frequency is the central element of the spectrum (more precisely, this means the zero frequency point is at element floor(N/2 + 1), where N is the number of samples). 

option2  This option is either a 1, 2 or 3 element vector depending on whether Ex is 1D, 2D or 3D. For each dimension, specify a value of either 0, 1 or N to obtain the desired 0 padding options. 

  * 0: no zero padding 
  * 1: zero padding up to the next power of 2 longer than the length of Ex (default) 
  * N: zero pad up to length N if N > length(Ex), where length of Ex is the length in a specific dimension. If N <= length(Ex), it will zero pad up to the next power of 2 longer than the length of Ex. For the fastest results, N should be a power of 2 and can be entered, for example, as 2^12. 

  
  
**Example**

This example shows that x2=invfft(fft(x)) returns x. x2 will only be equal to x if the standard fft without zero padding is used. In the plot command, 1 is added to x2 so that both lines are visible in the plot. 
    
    
    t=linspace(0,100,1000);
    x=sin(t)+sin(t/10);
    k=fft(x,1,0);
    x2=invfft(k,1,0);
    plot(t,x,x2+1,"t");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ fft ](/hc/en-us/articles/360034926133-fft) , [ fftw ](/hc/en-us/articles/360034926153-fftw) , [ fftk ](/hc/en-us/articles/360034406014-fftk)
