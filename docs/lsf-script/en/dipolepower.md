# dipolepower

Returns the power injected into the simulation region by a dipole source. In 3D
simulations, the units will be in Watts if cwnorm is used, and Watts/Hertz2 if nonorm is
used.

The dipolepower script command returns the power that was injected into the simulation
region, and is equivalent to measuring the power transmitted out of a small box
surrounding the dipole. In contrast, [sourcepower](./sourcepower.md) will return the
power that the dipole would radiate in a homogeneous material. dipolepower and
sourcepower are equivalent for dipoles in a homogeneous medium.

Advanced notes:

- If the dipole is located within a dispersive medium (with a non-zero imaginary part of
  the refractive index), then the results of this function are not reliable. In such
  situations, using a box of monitors around the dipole is recommended.
- Numerical errors in this calculation may become noticeable when very small simulation
  mesh sizes are used. If the mesh step is the order of, or smaller than, λ/1000,
  verifying the dipolepower results by measuring the radiated power with a small box of
  monitors surrounding the dipole is recommended.

Please visit the [Support Center](https://www.lumerical.com/support/) for more
assistance if you are using a dipole in a dispersive medium.

| **Syntax**                  | **Description**                                                                                                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = dipolepower(f);       | Returns the amount of power radiated by the dipole source, at frequency points f. (f in Hz)                                                                                   |
| out = dipolepower(f, name); | This option allows you to obtain the power radiated by a single dipole, rather than the sum of all dipoles. This option is only needed for simulations with multiple dipoles. |

**Examples**

See the
[Dipoles - Radiated Power](https://optics.ansys.com/hc/en-us/articles/360034382794-Sources-Dipoles)
page and the
[Fluorescence enhancement](https://apps.lumerical.com/fluorescence-enhancement.html)
application example.

**See Also**

[sourcenorm](./sourcenorm.md), [sourcepower](./sourcepower.md),
[sourcepower_avg](https://optics.ansys.com/hc/en-us/articles/360034925333-sourcepower-avg),
[sourcepower_pavg](https://optics.ansys.com/hc/en-us/articles/360034925353-sourcepower-pavg),
[transmission](./transmission.md), [cwnorm](./cwnorm.md), [nonorm](./nonorm.md)
