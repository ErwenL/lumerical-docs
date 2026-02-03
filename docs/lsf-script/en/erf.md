# erf

Calculates the error function as defined by the following equation: 

$$ \operatorname{erf}(z)=\frac{2}{\sqrt{\pi}} \int_{0}^{z} \exp \left(-t^{2}\right) d t $$ 

**Syntax** |  **Description**  
---|---  
out=erf(z);  |  Returns error function of z where z is a scalar number or matrix of scalar numbers.   
  
**Example**

Plot the error function from z=-5 to 5. 
    
    
    z=linspace(-5,5,50); # generate vector of numbers from -5 to 5 with 50 points
    erf_z = erf(z);
    plot(z,erf_z,"z","erf");

The following figure shows the plot created by the example code. 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ erfc ](/hc/en-us/articles/360034406534-erfc) , [ erfinv ](/hc/en-us/articles/360034406554-erfinv) , [ erfcinv ](/hc/en-us/articles/360034926813-erfcinv)
