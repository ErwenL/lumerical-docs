# fft

Computes the 1D, 2D, or 3D Fast Fourier Transform (FFT) of a matrix. In the 1D case, the
transform is given by

$$ E_w[m]=\\text{fft}(E_x)=\\sum\_{n-1}^NE_x[n]. e^{(\\frac{2\\pi i}{N})(n-1)(m-1)} $$

The FFT, inverse FFT, and all associated functions have an option (option 1 below) that
controls the format used to store the frequency domain data. When working with spectral
data it is not possible to switch between formats; there are no functions to convert
between formats. This implies that if you use option 1=n to produce a spectrum with
\[[||fft]\], then you must also use option 1=n if you want to pass that same spectral
data to \[[||invfft]\]. Similarly, if you use option1 = n for \[[||fft]\], then you also
need to use option 1=n with \[[||fftw]\] to get the proper frequency vector
corresponding to your spectrum. \[[||invfft]\] and \[[||fftk]\] work in the same way.

| **Syntax**                     | **Description**                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------- |
| out = fft(Ex);                 | Returns the fast Fourier transform of Ex. Ex can be 1D, 2D or 3D.                                 |
| out = fft(Ex,option1,option2); | option1 This option controls the format used to store the frequency domain data. The options are: |

- 1 : the standard FFT (zero frequency is at the first element of the matrix). This is
  the default option.
- 2 : zero frequency is the first element, but only data up to and including the Nyquist
  frequency is stored. This option is only useful for real-valued, 1D time/spatial
  signals.
- 3 : the FFT is shifted so zero frequency is the central element of the spectrum (more
  precisely, this means the zero frequency point is at the element floor(N/2 + 1), where
  N is the number of samples).

option2 This option is either a 1, 2 or 3 element vector depending on whether Ex is 1D,
2D or 3D. For each dimension, specify a value of either 0, 1 or N to obtain the desired
0 padding options.

- 0: no zero padding.
- 1: zero padding up to the next power of 2 longer than the length of Ex (default).
- N: zero pad up to length N if N > length(Ex), where the length of Ex is the length in
  a specific dimension. If N \<= length(Ex), it will zero pad up to the next power of 2
  longer than the length of Ex. For the fastest results, N should be a power of 2 and
  can be entered, for example, as 2^12.

## Note: FFT Conventions There are different, but equivalent conventions for defining Fourier transforms. Lumerical defines the forward FFT using a positive sign in the exponential term, and the inverse FFT using a negative sign in the exponential term. However, some other packages (e.g. MATLAB) use the opposite convention, with a negative sign in the exponential for the forward FFT and a positive sign in the exponential for the inverse FFT. To convert between the different FFT conventions, switch the \[[||invfft]\] and \[[||fft]\] and rescale the results. For a signal y with N elements, this can be done as follows: fft(y,1,0) (Lumerical) \\(\\Longleftrightarrow\\) ifft(y)\*N (MATLAB) invfft(y,1,0) (Lumerical) \\(\\Longleftrightarrow\\) fft(y)/N (MATLAB)

### Example

This example transforms a time signal with 60 and 100 rad/s angular frequency components
into the frequency domain. The function \[[||fftw]\] is used to get the correct
frequency vector. If this was a spatial signal, then \[[||fftk]\] should be used in
place of \[[||fftw]\].

```
t=linspace(0,1,1000);    # time signal
w1=100;           # frequency, in rad/s
w2=60;            # frequency, in rad/s
x=0.5*(sin(w1*t)+sin(w2*t)); # the signal
plot(t,x,"time","signal");
o1=2;            # option 1
o2=1;            # option 2
y=fft(x,o1,o2);       # fft
w=fftw(t,o1,o2);       # frequency signal
plot(w,abs(y),"freq (rad/sec)","amplitude");
```

This example shows how to calculate the FFT of the electric field intensity (i.e.,
combining all three field components) recorded by a time monitor in the attachment. If
you want to filter the high-frequency data, set option1 to 2.

```
# get data from point time monitor
m = "time";
t = getdata(m,"t");
Ex = getdata(m,"Ex");
Ey = getdata(m,"Ey");
Ez = getdata(m,"Ez");
# option1 = 1 -> standard fft
# option1 = 2 -> remove high frequency data
option1 = 2;
# do fft of each component
f  = fftw(t, option1)/2/pi;
Exw = fft(Ex, option1);  # fft each component separately
Eyw = fft(Ey, option1);
Ezw = fft(Ez, option1);
E2w = abs(Exw)^2+abs(Eyw)^2+abs(Ezw)^2; # combine field components
plot(f/1e12,E2w,"f (THz)","|E(f)|^2","fft E^2 intensity"); 
```

The following figures show the resulting plot for both the standard transform and the
option to remove the high-frequency data (option1 = 1 or 2).

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ invfft ](./invfft.md) ,
[ fftw ](./fftw.md) , [ fftk ](./fftk.md) , [ czt ](./czt.md)
