# erfc

Calculates the complementary error function as defined by the following equation: 

$$ \operatorname{erfc}(z)=1-\frac{2}{\sqrt{\pi}} \int_{0}^{z} \exp \left(-t^{2}\right) d t $$ 

**Syntax** |  **Description**  
---|---  
out=erfc(z);  |  Returns the complementary error function of z where z is a scalar number or matrix of scalar numbers.   
  
**Example**

Plot the complementary error function from z=-5 to 5. 
    
    
    z=linspace(-5,5,50); # generate vector of numbers from -5 to 5 with 50 points
    erfc_z = erfc(z);
    plot(z,erfc_z,"z","erfc");

The following figure shows the plot created by the example code. 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ erf ](/hc/en-us/articles/360034926793-erf) , [ erfinv ](/hc/en-us/articles/360034406554-erfinv) , [ erfcinv ](/hc/en-us/articles/360034926813-erfcinv)
