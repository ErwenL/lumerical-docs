# mczfit

Fits a variable gain filter to a family of gain curve data, where each curve in the family corresponds to a value of carrier density, producing a file of gain filter coefficients to be used by the TWLM element.

**Syntax** |  **Description**  
---|---  
out=mczfit(inputfilename, outputfilebase, centrefrequency, samplerate, maxnumcoef, tol, maxiter, rectangular, rolloff); |  Fits a variable gain filter to a family of gain curve data, where each curve in the family corresponds to a value of carrier density, producing a file of gain filter coefficients to be used by the TWLM element. " **inputfilename** " is a string containing the name of the input data file (including the suffix). The format of the input data is specified below. " **outputfilename** " is a string containing the name (excluding the suffix) of the file containing the gain filter coefficients. " **centrefrequency** " is the center frequency of the frequency band for which the gain fitting is to be performed. " **samplerate** " is the bandwidth of the frequency band for which the gain fitting is to be performed. " **maxnumcoef** " is the maximum number of filter coefficients to be used to fit to the data. " **tol** " is the tolerance " **rectangular** " is a bool value, it defines the data format. "true" represents 'real' and 'imaginary' format; "false" represents polar coordinate format with 'amplitude' and 'phase' " **maxiter** " is the maximum number of iterations used in fitting to the data. " **rolloff** " is the fraction of the bandwidth over which the input frequency data is rolled off to the average of the two values at the band edges.  
  
**Implementation detail**

The format of the data file is as follows:
    
    
    (1, Nc)
    carrierdensity_1, carrierdenisty_2, …, carrierdensity_Nc
    (Ns, Nc+1)
    freq_1gain_1_1gain_1_2…gain_1_Nc
    freq_2gain_2_1gain_2_2…gain_2_Nc
    ……………
    freq_Nsgain_Ns_1gain_Ns_2…gain_Ns_Nc

where the parameters are defined in the table below:

Nc |  The number of gain curvers  
---|---  
Ns |  The number of frequency samples  
carrierdensity_j |  The carrier density corresponding to the j-th gain curve  
freq_i |  The i-th frequency sample  
gain_i_j |  The gain value for the i-th frequency sample in the j-th curve  
  
Notes:

  1. The frequencies must be ordered in ascending order, such that frequency_1 is the lowest and frequency_Ns is the highest 
  2. The gain curves and carrier densities must be ordered in descending order of carrier density. That is, carrierdensity_1 is the largest carrier density and carrierdensity_Nc is the lowest carrier density, and gain_i_1 is the gain for the largest carrier density and i-th frequency sample and gain_i_Nc is the gain for the lowest carriest density and i-th frequency sample. 



The return values are listed in the table below:

fit_out |  A struct with fields  
---|---  
frequency |  A column vector of the frequency sample points  
input |  A matrix with the column vectors containing the input frequency response to be fit for each operating point  
operatingPoint |  A row vector containing the input operating points corresponding to the input frequency responses in the columns of the input matrix  
operatingPointInterpolated |  A row vector containing values of the linearly interpolated values of operating points between the input values of operating points  
output |  A matrix with the column vectors containing the fit frequency response for each input operating point  
outputInterpolated |  A matrix with the column vectors containing the fit frequency response for each linearly interpolated operating point contained in row vector ‘operatingPointInterpolated’.  
  
Note:

This script function also produces a gain filter coefficients to be used by the TWLM element. The name of the file will be outputfilename.mcfdb. 

**Example**

Please refer to the application example page [ Gain Fitting ](/hc/en-us/articles/360042820953) for the detailed usage of this command.

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ mcfit ](/hc/en-us/articles/360034930333-mcfit)
