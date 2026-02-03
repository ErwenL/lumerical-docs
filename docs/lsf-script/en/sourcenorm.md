# sourcenorm

Returns the source normalization spectrum used to normalize data in the cwnorm state for standard fourier transform quantities. See the [Units and normalization](/hc/en-us/articles/360034397034) page for more information. 

**Syntax** |  **Description**  
---|---  
out = sourcenorm(f); |  Returns the source normalization spectrum used to normalize data in the cwnorm state at the vector of frequency points f. (f is the frequency in Hz) If the normalization state is set to 'CWNorm (average)': $$ s(\omega)=\operatorname{sourcenorm}(\omega)=\frac{1}{N} \sum_{s o u r c e s} \int \exp (i \omega t) s_{j}(t) d t $$

  * \\(s_{j}(t)\\): the time signal of the jth active source in the object tree
  * N is the number of active sources then

If the normalization state is set to 'CWNorm (first)': $$ s(\omega)= \int \exp (i \omega t) s_{1}(t) d t $$  
out = sourcenorm(f, name); |  When you enter an additional argument for the source name, it uses the specific source of your choice, rather than the first source or the average of all the sources in the object tree.  
  
**Example**

This example shows how to reproduce the source spectrum figures shown in the Frequency/Wavelength tab of the source property window.
    
    
    lambda1 = 0.4e-6; # start wavelength  
    lambda2 = 0.7e-6; # end wavelength  
    f=linspace(c/lambda2,c/lambda1,1000);  
    
    # get the source spectrum  
    spectrum=sourcenorm(f);  
    spectrum=abs(spectrum)^2;  
    spectrum=spectrum/max(spectrum);  
    
    # get the source time domain signal  
    time = getdata("source","time");  
    time_signal = getdata("source","time_signal");  
    
    plot(c/f*1e6,spectrum, "wavelength (um)","spectrum vs wavelength");  
    plot(f/1e12,spectrum, "frequency (THz)","spectrum vs frequency");  
    plot(time*1e15,time_signal,"time (fs)","amplitude","Source time signal"); 

**See Also**

[sourcenorm2_avg](/hc/en-us/articles/360034405474-sourcenorm2-avg), [sourcenorm2_pavg](/hc/en-us/articles/360034405494-sourcenorm2-pavg), [sourcepower](/hc/en-us/articles/360034925313-sourcepower), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [nonorm](/hc/en-us/articles/360034405434-nonorm), [Units and normalization](/hc/en-us/articles/360034397034)
