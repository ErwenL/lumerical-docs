<!--
Translation from English documentation
Original command: setsourcesignal
Translation date: 2026-02-04 22:50:14
-->

# setsourcesignal

Loads 一个 自定义 源 时间 signal into 一个 源. This advanced 源 属性 allows users 到 创建 一个 自定义 源 源 时间 signal 和 spectrum. Custom 源 时间 signals 是 required 用于 some types 的 nonlinear simulations. This feature 是 not recommended 用于 most types 的 linear simulations. 

The 自定义 时间 signal 必须 为 defined 在 terms 的 该 signal Amplitude 和 Phase. This 是 一个 convenient definition because 该 Amplitude 和 Phase 是 generally slowly varying as 一个 函数 的 时间 (compared 使用 该 actual 时间 signal), meaning 一个 lower sampling rate 可以 为 used 到 define 该 自定义 signal. The actual 时间 domain signal injected 通过 该 源 是 given 通过:

**语法** |  **描述**  
---|---  
setsourcesignal("name", t, amplitude, phase); |  设置 该 时间 domain signal 的 源 named "name". t, amplitude, 和 phase 是 1D vectors 使用 该 same 长度.  
setsourcesignal("name", t, amplitude, phase, fcentre, bandwidth); |  Allows you 到 specify 该 precise center 频率 和 bandwidth 该 将 为 used 用于 all simulations. These 值 是 used 用于 materials fits, calculating 该 mesh, 和 源 limits. If fcentre 和 bandwidth 是 not specified, they 将 为 automatically estimated 从 该 时间 signal.   
  
**示例**

See 该 [Custom 源 时间 signal](/hc/en-us/articles/360034383114-Custom-时间-signal) example.

**参见**

[sourcepower](/hc/en-us/articles/360034925313-sourcepower)
