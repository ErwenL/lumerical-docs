<!--
Translation from English documentation
Original command: dipolepower
Translation date: 2026-02-04 22:49:48
-->

# dipolepower

返回 该 power injected into 该 仿真 region 通过 一个 dipole 源. In 3D simulations, 该 units 将 为 在 Watts 如果 cwnorm 是 used, 和 Watts/Hertz2 如果 nonorm 是 used.

The dipolepower 脚本 命令 返回 该 power 该 was injected into 该 仿真 region, 和 是 equivalent 到 measuring 该 power transmitted out 的 一个 small box surrounding 该 dipole. In contrast, [sourcepower](/hc/en-us/articles/360034925313-sourcepower) 将 返回 该 power 该 该 dipole would radiate 在 一个 homogeneous 材料. dipolepower 和 sourcepower 是 equivalent 用于 dipoles 在 一个 homogeneous medium.

Advanced notes:

  * If 该 dipole 是 located within 一个 dispersive medium (使用 一个 non-zero imaginary part 的 该 refractive index), 那么 该 results 的 此 函数 是 not reliable. In such situations, 使用 一个 box 的 monitors around 该 dipole 是 recommended.
  * Numerical errors 在 此 calculation 可能 become noticeable 当 very small 仿真 mesh sizes 是 used. If 该 mesh step 是 该 order 的, 或 smaller than, λ/1000, verifying 该 dipolepower results 通过 measuring 该 radiated power 使用 一个 small box 的 monitors surrounding 该 dipole 是 recommended.



Please visit the [Support Center](https://www.lumerical.com/support/) for more assistance if you are using a dipole in a dispersive medium.

**语法** |  **描述**  
---|---  
out = dipolepower(f); |  返回 该 amount 的 power radiated 通过 该 dipole 源, at 频率 points f. (f 在 Hz)  
out = dipolepower(f, name); |  This option allows you 到 obtain 该 power radiated 通过 一个 single dipole, rather than 该 sum 的 all dipoles. This option 是 only needed 用于 simulations 使用 multiple dipoles.  
  
**示例**

See the [Dipoles - Radiated Power](/hc/en-us/articles/360034382794-Sources-Dipoles) page and the [Fluorescence enhancement](https://apps.lumerical.com/fluorescence-enhancement.html) application example.

**参见**

[sourcenorm](/hc/en-us/articles/360034925273-sourcenorm), [sourcepower](/hc/en-us/articles/360034925313-sourcepower), [sourcepower_avg](/hc/en-us/articles/360034925333-sourcepower-avg), [sourcepower_pavg](/hc/en-us/articles/360034925353-sourcepower-pavg), [transmission](/hc/en-us/articles/360034405354-transmission), [cwnorm](/hc/en-us/articles/360034405454-cwnorm), [nonorm](/hc/en-us/articles/360034405434-nonorm)
