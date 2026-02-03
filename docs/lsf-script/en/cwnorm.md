# cwnorm

Uses CW normalization. All simulation data will be normalized to the injected source power. Most users prefer to do their analysis in the CW normalization state, since it removes any effect caused by the finite pulse length of the source. It also converts the units of all electromagnetic fields to be the same as in the time domain. Note, this command works in both the Layout and Analysis mode.

This function controls the checkbox located in Settings - Normalization state.

**Syntax** |  **Description**  
---|---  
cwnorm; |  Use CW normalization. Uses the first active source in the Object tree; This function does not return any data.  
cwnorm(norm_option) |  norm_option: 1 (first source), 2 (average of all sources)  
  
**Example**

This example shows how to switch to the cwnorm state.
    
    
    cwnorm; # normalized to the first active source  
      
    cwnorm(1); # normalized to the first active source  
    cwnorm(2); # normalized to the average of all the sources

**See Also**

[nonorm](/hc/en-us/articles/360034405434-nonorm), [Units and normalization](/hc/en-us/articles/360034397034), [Frequency Domain Normalization](/hc/en-us/articles/360034394234-Frequency-domain-normalization)
