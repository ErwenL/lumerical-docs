# mie3d

The function mie3d can be used to calculate the scattering, absorption, and extinction efficiencies of a spherical particle made of any (non-magnetic) material embedded in any ambient dielectric material. The efficiencies are simply the cross sections normalized to the geometric cross section of the particle (\\(\pi r^2\\)). 

###  References: 

[1] Bohren C.F. and D.R. Huffman, “Absorption and Scattering of Light by Small Particles”, John Wiley, New York, NY, 1983. 

[2] Documentation of Mätzler C. “MATLAB Functions for Mie Scattering and Absorption, Version 2”, IAP Res. Rep. No. 2002-11, August, 2002. 

**Syntax** |  **Description**  
---|---  
Q = mie3d(m,x);  |  The result Q is a struct which contains quantities Qext, Qabs and Qscat (Qext = Qabs+Qscat). These will have the same length as x.  The arguments are:  m: the ratio of the refractive index of the sphere to the refractive index of the ambient dielectric medium. This quantity may be complex-valued because the refractive index of the sphere may be complex. This quantity should either have a singleton value, or be the same length of x for dispersive media.  x: the size parameter which is defined as 2*pi*r/lambda0*n1 where lambda0 is the free space wavelength, r is the sphere radius, and n1 is the real-valued refractive index of the ambient medium.   
Q = mie3d(m,x,nmax);  |  nmax : the maximum number of orders to calculate for the mie coefficients. The default value is 0, and in this case the nmax = ceil(x+4*x^(1/3))+2. There is typically no need to modify the default value.   
  
**Example**

In this example we will calculate and compare the extinction efficiencies for 1 micron spheres of n=1.5, dispersive glass and gold over the visible spectrum. 
    
    
    # input parameters
    n1 = 1;
    n2 = 1.5;
    lambda0 = linspace(400e-9,700e-9,10000);
    radius = 1000e-9;
    # calculate m,x and call mie3d
    m = n2/n1;
    x = 2*pi*radius/lambda0*n1;
    Q1 = mie3d(m,x);
    # recalculate with dispersive glass
    n2 = getindex("SiO2 (Glass) - Palik",c/lambda0);
    m = n2/n1;
    Q2 = mie3d(m,x);
    # recalculate with Al
    n2 = getindex("Au (Gold) - Palik",c/lambda0);
    m = n2/n1;
    Q3 = mie3d(m,x);
    plot(lambda0*1e9,Q1.Qext,Q2.Qext,Q3.Qext,"wavelength (nm)","Q extinction");
    legend("n = 1.5","Glass (Palik)","Gold (Palik)");

**See Also**

[ mie3ds12 ](/hc/en-us/articles/360034406814-mie3ds12) , [ Mie3D example (FDTD) ](https://apps.lumerical.com/mie-scattering-fdtd.html) , [ Mie3D example (DGTD) ](https://apps.lumerical.com/mie-scattering-dgtd.html)
