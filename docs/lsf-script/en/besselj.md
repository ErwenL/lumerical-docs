# besselj

Computes the Bessel function of the first kind. 

**Syntax** |  **Description**  
---|---  
out=besselj(nu, z);  |  "nu" is the order and "z" could be an array. Both nu and z need to be real.   
  
**Example**

This example shows how to obtain the first order Bessel function of the first kind of the array z. 
    
    
    >z = 0.2:0.2:1;
    >?besselj(1,z);
    result: 
    0.0995008 
    0.196027 
    0.286701 
    0.368842 
    0.440051     

**See Also**

[ bessely ](/hc/en-us/articles/360034926953-bessely) ,  [ besseli ](/hc/en-us/articles/360034926973-besseli) ,  [ besselk ](/hc/en-us/articles/360034406774-besselk)
