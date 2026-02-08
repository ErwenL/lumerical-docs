# setsourcesignal

Loads a custom source time signal into a source. This advanced source property allows
users to create a custom source source time signal and spectrum. Custom source time
signals are required for some types of nonlinear simulations. This feature is not
recommended for most types of linear simulations.

The custom time signal must be defined in terms of the signal Amplitude and Phase. This
is a convenient definition because the Amplitude and Phase are generally slowly varying
as a function of time (compared with the actual time signal), meaning a lower sampling
rate can be used to define the custom signal. The actual time domain signal injected by
the source is given by:

| **Syntax**                                                        | **Description**                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| setsourcesignal("name", t, amplitude, phase);                     | Sets the time domain signal of source named "name". t, amplitude, and phase are 1D vectors with the same length.                                                                                                                                                                                  |
| setsourcesignal("name", t, amplitude, phase, fcentre, bandwidth); | Allows you to specify the precise center frequency and bandwidth that will be used for all simulations. These values are used for materials fits, calculating the mesh, and source limits. If fcentre and bandwidth are not specified, they will be automatically estimated from the time signal. |

**Example**

See the
[Custom source time signal](https://optics.ansys.com/hc/en-us/articles/360034383114-Custom-time-signal)
example.

**See Also**

[sourcepower](./sourcepower.md)
