<!--
Translation from English documentation
Original command: readnportsparameterat
Translation date: 2026-02-04 22:50:14
-->

# readnportsparameterat

Interpolates the [S-Parameter sweep](https://optics.ansys.com/hc/en-us/articles/360036107934-The-S-parameter-sweep) file with the specified parameter values.

**语法** |  **描述**  
---|---  
M = readnportsparameterat(“文件名”, sweep_param) |  Interpolates 该 S-Parameter sweep 文件 使用 该 specified 参数 值, 使用 该 spline interpolation method. 文件名: S-Parameter sweep 文件. sweep_param: specified sweep 参数, usually 在 该 format 的 一个 矩阵.  
M = readnportsparameterat“文件名”, sweep_param, opt)  |  Interpolates 该 S-Parameter sweep 文件 使用 该 specified 参数 值, 使用 interpolation options 设置 在 该 结构 named opt. 文件名: S-Parameter sweep 文件. sweep_param: specified sweep 参数, usually 在 该 format 的 一个 矩阵. opt: Structure setting interpolation options. The 结构 fields 是 described 在 该 table below.  
  
The option 结构 has 该 following fields, 该 spelling 的 each field 是 case-sensitive.

**Field** |  **描述**  
---|---  
method |  The method used 用于 interpolation. The following options 是 supported:

  * spline: Spline interpolation method, 此 是 该 default method.
  * Geodesic: Geodesic interpolation method 该 ensures smooth transitions. When geodesic interpolation 是 选中的, 一个 similarity check 是 performed 在 original 数据 points near 该 interpolated point used 用于 该 interpolation, 如果 这些 points 是 not sufficiently similar, 该 数据 是 coarse 和 一个 warning 是 displayed. This method cannot 为 used 用于 extrapolation.

  
passivity |  Whether passivity 是 enforced 用于 该 s-参数 数据 prior 到 interpolation. This field only affects results 当 “geodesic” 是 选中的 as 该 interpolation method. When 数据 是 non-passive, 一个 warning message 是 always displayed. The following options 是 supported:

  * enforce: Ensures S-矩阵 是 passive 通过 making sure 该 该 induced 2-norm 的 该 s-参数 是 less than 1. This 是 该 default method.
  * ignore: Ignores passivity 的 该 s-参数 和 interpolates as-是.

  
  
**Note** : For more information on how passivity is enforced, see this [Knowledge Base](https://optics.ansys.com/hc/en-us/articles/360059772393-S-parameter-passive-workflow-guide#toc_4) article.

**示例**

The following 脚本 interpolates 该 S-Parameter 文件 " coupler_s_parameter_sweep.txt " 使用 该 specified 参数 该 defined 在 一个 矩阵 named "sweep_param". Then 此 interpolated s-参数 可以 为 assigned 到 一个 s-参数 元素.
    
    
    #Here, 该 variables radius, Lc, 和 gap has been 设置 previously  
    sweep_param = 矩阵( 3 );  
    sweep_param(1)=radius;  
    sweep_param(2)=Lc;  
    sweep_param(3)=gap;  
    ?M = readnportsparameterat("coupler_s_parameter_sweep.txt", sweep_param );

The following 脚本 interpolates 该 same S-Parameter 文件, but 使用 该 geodesic option 和 ignoring passivity.
    
    
    ?M = readnportsparameterat("coupler_s_parameter_sweep.txt", sweep_param, {"method":"geodesic", "passivity":"ignore"});

**参见**

[ convertnportsparametersweep ](/hc/en-us/articles/360034409234-convertnportsparametersweep)
