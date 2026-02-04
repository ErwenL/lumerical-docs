<!--
Translation from English documentation
Original command: findresonances
Translation date: 2026-02-04 22:49:49
-->

# findresonances

返回 该 频率, decay constant, Q-factor, amplitude 和 phase 的 resonances extracted 从 该 时间 trace 的 一个 purely real 或 complex signal within 一个 频率 range \\( [f_{\text{min}}, f_{\text{max}}] \\) specified 通过 该 用户. The findresonances 脚本 命令 uses 一个 harmonic inversion method called filter diagonalization (see Ref. [1]) 到 approximate 该 时间 signal 通过 一个 superposition 的 exponentially decaying harmonic oscillations 的 该 form

$$ s(t) \approx \sum_{k=1}^{N} A_k \cos(2 \pi f_k t - \phi_k) e^{- \alpha_k t} \text{, 用于 real signals}$$

$$ s(t) \approx \sum_{k=1}^{N} A_k e^{-i (2 \pi f_k t - \phi_k)} e^{- \alpha_k t} \text{, 用于 complex signals}$$

Here \\( N \\) 是 该 数字 的 resonances 和 each resonance 是 characterized 通过 four real-valued 参数:

  * \\( f_k \\): Resonance 频率.
  * \\( \alpha_k \\): Decay constant, 其中 \\( \alpha_k \ge 0 \\). Alternatively, 该 decay 是 described 通过 该 Q-factor \\( Q_k = \omega_k / 2 \alpha \\), 其中 \\( \omega_k = 2 \pi f_k \\) 是 该 对应的 angular 频率.
  * \\( A_k \\): Amplitude.
  * \\( \phi_k \\): Phase.



Additionally, findresonances 返回 一个 error estimate 该 可以 为 used 到 identify spurious resonances reported 通过 该 脚本 命令. This estimate 是 一个 measure 的 relative confidence, i.e. it 是 only meaningful 通过 comparison between 该 estimates 用于 all resonances found. If 该 值 的 该 error estimate 用于 一个 resonance stands out as significantly larger than 该 rest, there 是 一个 higher chance 该 it 是 一个 spurious resonance.

重要 notes:

  * The signal 到 analyze 应该 start only after all sources have stopped injecting energy into 该 system. When 该 rising part 的 该 signal 是 not removed, findresonances 可能 report spurious resonances 和, 在 particular, wrong Q-factors.
  * The longer 该 provided signal, 该 more accurate 该 reported modes 将 为. However, 该 Q-factors 是 much more sensitive 到 此 than 该 resonance frequencies. It 是 often possible 到 obtain very accurate 频率 information 从 only 一个 few oscillation periods, while accurate Q-factors require significantly more 数据.
  * To reliably find modes, they 必须 为 excited 使用 sufficient energy 在 该 仿真. It 是 important 到 make sure 该 excitation bandwidth 是 comparable 到 或 larger than 该 频率 window \\( [f_{\text{min}}, f_{\text{max}}] \\).
  * Results 是 more reliable near 该 center 的 该 频率 interval \\( [f_{\text{min}}, f_{\text{max}}] \\). When scanning large 频率 intervals, it 可以 为 useful 到 run findresonances 使用 multiple overlapping 频率 windows.
  * Exciting 一个 small 频率 range helps 到 reduce 该 noise 在 该 calculation. Therefore, 用于 一个 careful 分析 的 一个 resonance 使用 known 频率, excite 该 system 使用 一个 narrow band pulse centered at 该 resonant 频率.
  * This 脚本 命令 cannot find reliably resonances 使用 very low Q-factor (\\(Q \lesssim 10\\)). Especially 当 there 是 modes 使用 both high 和 low Q-factors, 那么 该 low-Q resonance 将 not 为 very accurate.



### References:

[1] V. A. Mandelshtam 和 H. S. Taylor, "Harmonic inversion 的 时间 signals 和 its application," J. Chem. Phys., vol. 107, no. 17, p. 6756-6769 (1997).

**语法** |  **描述**  
---|---  
out = findresonances(时间, signal, frequency_interval); |  返回 该 resonance 参数 extracted 从 该 signal vs. 时间 数据. The result _out_ 是 一个 Nx6 real-valued 矩阵, 其中 N 是 该 数字 的 resonances found within 该 range specified 通过 frequency_interval. If no resonances 是 found, 该 矩阵 out 将 为 empty. The 6 columns 的 _out_ correspond 到:  **[频率, decay_constant, Q_factor, amplitude, phase, error_estimate]** The inputs 时间 和 signal 必须 为 one-dimensional arrays; 时间 必须 为 real-valued, while signal 可以 为 real- 或 complex-valued. The input frequency_interval 是 一个 real-valued 数组 使用 two entries \\( [f_{\text{min}}, f_{\text{max}}] \\) bounding 该 频率 range 用于 该 search.  
  
**示例**

The following example shows 如何 到 extract 该 resonances 从 一个 superposition 的 two decaying sinusoidal signals. We sample 该 same signal over 时间 intervals 的 different duration 和 show 该 该 results 是 该 same. For 此 simple analytical signal only 一个 few oscillation periods 是 required 到 获取 accurate 值 用于 all 该 resonant 参数. In practice, more complicated signals (用于 example, 一个 signal 从 一个 时间 监视器 在 一个 FDTD 仿真) might require more oscillation periods, especially 用于 accurate decay 或 Q-factor 值, as explained above 在 重要 notes. Finally, note 该 该 error estimates 用于 该 two resonances 是 roughly within 该 same order 的 magnitude, so their reliability 是 comparable.
    
    
    # Resonant frequencies, decay constants, amplitudes 和 phases 的 该 analytical signal:
    f1 = 1.765;
    alpha1 = 0.005;
    ampl1=1.3;
    phase1 = 0.4;
    f2 = 2.345;
    alpha2 = 0.012;
    ampl2= 0.45;
    phase2 = 1.234;
    # Time intervals 的 该 signal:
    t_long = linspace(0,20,201);
    t_short = t_long(1:20);
    # Signal:
    signal_long = ampl1*cos(2*pi*f1*t_long - phase1)*exp(-alpha1*t_long) + ampl2*cos(2*pi*f2*t_long - phase2)*exp(-alpha2*t_long);
    signal_short = ampl1*cos(2*pi*f1*t_short - phase1)*exp(-alpha1*t_short) + ampl2*cos(2*pi*f2*t_short - phase2)*exp(-alpha2*t_short);
    # Find resonances:
    res_long = findresonances(t_long, signal_long, [1.5,3]);
    res_short = findresonances(t_short, signal_short, [1.5,3]);
    # Plot signal 和 show results:
    plotxy(t_long, signal_long, t_short, signal_short, "时间", "signal");
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

**参见**

[List 的 commands](/hc/en-us/articles/360037228834), [findpeaks](/hc/en-us/articles/360034925933-findpeaks), [plotxy](/hc/en-us/articles/360034931093-plotxy), [transpose](/hc/en-us/articles/360034925973-transpose)
