# findresonances

Returns the frequency, decay constant, Q-factor, amplitude and phase of resonances extracted from the time trace of a purely real or complex signal within a frequency range \\( [f_{\text{min}}, f_{\text{max}}] \\) specified by the user. The findresonances script command uses a harmonic inversion method called filter diagonalization (see Ref. [1]) to approximate the time signal by a superposition of exponentially decaying harmonic oscillations of the form

$$ s(t) \approx \sum_{k=1}^{N} A_k \cos(2 \pi f_k t - \phi_k) e^{- \alpha_k t} \text{, for real signals}$$

$$ s(t) \approx \sum_{k=1}^{N} A_k e^{-i (2 \pi f_k t - \phi_k)} e^{- \alpha_k t} \text{, for complex signals}$$

Here \\( N \\) is the number of resonances and each resonance is characterized by four real-valued parameters:

  * \\( f_k \\): Resonance frequency.
  * \\( \alpha_k \\): Decay constant, where \\( \alpha_k \ge 0 \\). Alternatively, the decay is described by the Q-factor \\( Q_k = \omega_k / 2 \alpha \\), where \\( \omega_k = 2 \pi f_k \\) is the corresponding angular frequency.
  * \\( A_k \\): Amplitude.
  * \\( \phi_k \\): Phase.



Additionally, findresonances returns an error estimate that can be used to identify spurious resonances reported by the script command. This estimate is a measure of relative confidence, i.e. it is only meaningful by comparison between the estimates for all resonances found. If the value of the error estimate for a resonance stands out as significantly larger than the rest, there is a higher chance that it is a spurious resonance.

Important notes:

  * The signal to analyze should start only after all sources have stopped injecting energy into the system. When the rising part of the signal is not removed, findresonances may report spurious resonances and, in particular, wrong Q-factors.
  * The longer the provided signal, the more accurate the reported modes will be. However, the Q-factors are much more sensitive to this than the resonance frequencies. It is often possible to obtain very accurate frequency information from only a few oscillation periods, while accurate Q-factors require significantly more data.
  * To reliably find modes, they must be excited with sufficient energy in the simulation. It is important to make sure the excitation bandwidth is comparable to or larger than the frequency window \\( [f_{\text{min}}, f_{\text{max}}] \\).
  * Results are more reliable near the center of the frequency interval \\( [f_{\text{min}}, f_{\text{max}}] \\). When scanning large frequency intervals, it can be useful to run findresonances with multiple overlapping frequency windows.
  * Exciting a small frequency range helps to reduce the noise in the calculation. Therefore, for a careful analysis of a resonance with known frequency, excite the system with a narrow band pulse centered at the resonant frequency.
  * This script command cannot find reliably resonances with very low Q-factor (\\(Q \lesssim 10\\)). Especially when there are modes with both high and low Q-factors, then the low-Q resonance will not be very accurate.



### References:

[1] V. A. Mandelshtam and H. S. Taylor, "Harmonic inversion of time signals and its application," J. Chem. Phys., vol. 107, no. 17, p. 6756-6769 (1997).

**Syntax** |  **Description**  
---|---  
out = findresonances(time, signal, frequency_interval); |  Returns the resonance parameters extracted from the signal vs. time data. The result _out_ is a Nx6 real-valued matrix, where N is the number of resonances found within the range specified by frequency_interval. If no resonances are found, the matrix out will be empty. The 6 columns of _out_ correspond to:  **[frequency, decay_constant, Q_factor, amplitude, phase, error_estimate]** The inputs time and signal must be one-dimensional arrays; time must be real-valued, while signal can be real- or complex-valued. The input frequency_interval is a real-valued array with two entries \\( [f_{\text{min}}, f_{\text{max}}] \\) bounding the frequency range for the search.  
  
**Example**

The following example shows how to extract the resonances from a superposition of two decaying sinusoidal signals. We sample the same signal over time intervals of different duration and show that the results are the same. For this simple analytical signal only a few oscillation periods are required to get accurate values for all the resonant parameters. In practice, more complicated signals (for example, a signal from a time monitor in a FDTD simulation) might require more oscillation periods, especially for accurate decay or Q-factor values, as explained above in Important notes. Finally, note that the error estimates for the two resonances are roughly within the same order of magnitude, so their reliability is comparable.
    
    
    # Resonant frequencies, decay constants, amplitudes and phases of the analytical signal:
    f1 = 1.765;
    alpha1 = 0.005;
    ampl1=1.3;
    phase1 = 0.4;
    f2 = 2.345;
    alpha2 = 0.012;
    ampl2= 0.45;
    phase2 = 1.234;
    # Time intervals of the signal:
    t_long = linspace(0,20,201);
    t_short = t_long(1:20);
    # Signal:
    signal_long = ampl1*cos(2*pi*f1*t_long - phase1)*exp(-alpha1*t_long) + ampl2*cos(2*pi*f2*t_long - phase2)*exp(-alpha2*t_long);
    signal_short = ampl1*cos(2*pi*f1*t_short - phase1)*exp(-alpha1*t_short) + ampl2*cos(2*pi*f2*t_short - phase2)*exp(-alpha2*t_short);
    # Find resonances:
    res_long = findresonances(t_long, signal_long, [1.5,3]);
    res_short = findresonances(t_short, signal_short, [1.5,3]);
    # Plot signal and show results:
    plotxy(t_long, signal_long, t_short, signal_short, "time", "signal");
    legend("long signal", "short signal");
    ?"***Long signal***";
    ?"Resonant frequencies: " + num2str(transpose(res_long(:,1)));
    ?"Decay constant:       " + num2str(transpose(res_long(:,2)));
    ?"Q-factor:             " + num2str(transpose(res_long(:,3)));
    ?"Amplitude:            " + num2str(transpose(res_long(:,4)));
    ?"Phase:                " + num2str(transpose(res_long(:,5)));
    ?"Error estimate:       " + num2str(transpose(res_long(:,6)));
    ?"***Short signal***";
    ?"Resonant frequencies: " + num2str(transpose(res_short(:,1)));
    ?"Decay constant:       " + num2str(transpose(res_short(:,2)));
    ?"Q-factor:             " + num2str(transpose(res_short(:,3)));
    ?"Amplitude:            " + num2str(transpose(res_short(:,4)));
    ?"Phase:                " + num2str(transpose(res_short(:,5)));
    ?"Error estimate:       " + num2str(transpose(res_short(:,6)));
    result: 
    ***Long signal***
    Resonant frequencies: 1.765 2.345
    Decay constant:       0.005 0.012
    Q-factor:             1108.98 613.92
    Amplitude:            1.3 0.45
    Phase:                0.4 1.234
    Error estimate:       1.02591e-015 1.07493e-015
    ***Short signal***
    Resonant frequencies: 1.765 2.345
    Decay constant:       0.005 0.012
    Q-factor:             1108.98 613.92
    Amplitude:            1.3 0.45
    Phase:                0.4 1.234
    Error estimate:       3.13843e-016 1.64344e-015

**See Also**

[List of commands](/hc/en-us/articles/360037228834), [findpeaks](/hc/en-us/articles/360034925933-findpeaks), [plotxy](/hc/en-us/articles/360034931093-plotxy), [transpose](/hc/en-us/articles/360034925973-transpose)
