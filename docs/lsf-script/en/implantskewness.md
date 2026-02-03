# implantskewness

Calculates the 'skewness' of the 1D doping profile from ion implant. The script command takes the semiconductor material name, dopant type, and ion energy as input arguments. 

**Syntax** |  **Description**  
---|---  
out = implantskewness("dopant", "semiconductor", E)  |  Provides the 'skewness' of the 1D doping profile from ion implant. The "dopant" argument is a string providing the dopant type. The options are (i) "boron", (ii) "phosphorous", (iii) "antimony", and (iv) "arsenic". The "semiconductor" argument is a string providing the semiconductor type. The only available option is "silicon". The last argument (E) is the ion energy for the implant in units of eV.   
  
**Example**

The following script calculates the range, straggle, skewness, kurtosis, and lateral scatter for an ion implant in 'silicon' with 'boron' for an ion implant energy of 1 keV. The script then calculates the peak concentration for the 1D doping profile for an ion dose of 2e13 /cm  2  and sets up an implant doping object in the CHARGE solver to model the corresponding doping profile. 
    
    
    E = 1000;  # eV
    dose = 2e13 * 1e4;  # /m^2
    mu = implantrange("boron","silicon",E);  # range in m
    si = implantstraggle("boron","silicon",E);  # straggle in m
    gal = implantskewness("boron","silicon",E); # skewness
    be2 = implantkurtosis("boron","silicon",E); # kurtosis
    si_lat = implantlateralscatter("boron","silicon",E);  # lateral scatter in m
    # calculate peak doping concentration
    x = linspace(0,mu+10*si,1001);
    y = pearson4pdf(x,mu,si,gal,be2); 
    ion_absorbed = integrate(y,[1],x);  
    peak = max(y)*dose/ion_absorbed;  # peak doping density in /m^3
    # set up implant doping object (assume doping object is already present in the objects tree)
    select("CHARGE::implant");
    set("dopant type","p");
    set("peak concentration",peak);
    set("distribution function","pearson4");
    set("range",mu);
    set("straggle",si);
    set("skewness",gal);
    set("kurtosis",be2);
    set("lateral scatter",si_lat);

**See Also**

[ implantrange ](/hc/en-us/articles/360034927033-implantskewness) , [ implantstraggle ](/hc/en-us/articles/360034406854-implantstraggle) , [ implantkurtosis ](/hc/en-us/articles/360034927053-implantkurtosis) , [ implantlateralscatter ](/hc/en-us/articles/360034406874-implantlateralscatter) , [ fitnormpdf ](/hc/en-us/articles/360034926993-fitnormpdf) , [ fitpearson4pdf ](/hc/en-us/articles/360034927013-fitpearson4pdf) , [ pearson4pdf ](/hc/en-us/articles/360034926693-person4pdf)
