<!--
Translation from English documentation
Original command: mczfit
Translation date: 2026-02-04 22:50:13
-->

# mczfit

Fits 一个 变量 gain filter 到 一个 family 的 gain curve 数据, 其中 each curve 在 该 family corresponds 到 一个 值 的 carrier density, producing 一个 文件 的 gain filter coefficients 到 为 used 通过 该 TWLM 元素.

**语法** |  **描述**  
---|---  
out=mczfit(inputfilename, outputfilebase, centrefrequency, samplerate, maxnumcoef, tol, maxiter, rectangular, rolloff); |  Fits 一个 变量 gain filter 到 一个 family 的 gain curve 数据, 其中 each curve 在 该 family corresponds 到 一个 值 的 carrier density, producing 一个 文件 的 gain filter coefficients 到 为 used 通过 该 TWLM 元素. " **inputfilename** " 是 一个 字符串 containing 该 name 的 该 input 数据 文件 (including 该 suffix). The format 的 该 input 数据 是 specified below. " **outputfilename** " 是 一个 字符串 containing 该 name (excluding 该 suffix) 的 该 文件 containing 该 gain filter coefficients. " **centrefrequency** " 是 该 center 频率 的 该 频率 band 用于 该 该 gain fitting 是 到 为 performed. " **samplerate** " 是 该 bandwidth 的 该 频率 band 用于 该 该 gain fitting 是 到 为 performed. " **maxnumcoef** " 是 该 maximum 数字 的 filter coefficients 到 为 used 到 fit 到 该 数据. " **tol** " 是 该 tolerance " **rectangular** " 是 一个 bool 值, it defines 该 数据 format. "true" represents 'real' 和 'imaginary' format; "false" represents polar coordinate format 使用 'amplitude' 和 'phase' " **maxiter** " 是 该 maximum 数字 的 iterations used 在 fitting 到 该 数据. " **rolloff** " 是 该 fraction 的 该 bandwidth over 该 该 input 频率 数据 是 rolled off 到 该 average 的 该 two 值 at 该 band edges.  
  
**Implementation detail**

The format 的 该 数据 文件 是 as follows:
    
    
    (1, Nc)
    carrierdensity_1, carrierdenisty_2, …, carrierdensity_Nc
    (Ns, Nc+1)
    freq_1gain_1_1gain_1_2…gain_1_Nc
    freq_2gain_2_1gain_2_2…gain_2_Nc
    ……………
    freq_Nsgain_Ns_1gain_Ns_2…gain_Ns_Nc

其中 该 参数 是 defined 在 该 table below:

Nc |  The 数字 的 gain curvers  
---|---  
Ns |  The 数字 的 频率 samples  
carrierdensity_j |  The carrier density 对应的 到 该 j-th gain curve  
freq_i |  The i-th 频率 sample  
gain_i_j |  The gain 值 用于 该 i-th 频率 sample 在 该 j-th curve  
  
注意:

  1. The frequencies 必须 为 ordered 在 ascending order, such 该 frequency_1 是 该 lowest 和 frequency_Ns 是 该 highest 
  2. The gain curves 和 carrier densities 必须 为 ordered 在 descending order 的 carrier density. That 是, carrierdensity_1 是 该 largest carrier density 和 carrierdensity_Nc 是 该 lowest carrier density, 和 gain_i_1 是 该 gain 用于 该 largest carrier density 和 i-th 频率 sample 和 gain_i_Nc 是 该 gain 用于 该 lowest carriest density 和 i-th 频率 sample. 



The 返回 值 是 listed 在 该 table below:

fit_out |  A 结构体 使用 fields  
---|---  
频率 |  A column 向量 的 该 频率 sample points  
input |  A 矩阵 使用 该 column vectors containing 该 input 频率 response 到 为 fit 用于 each operating point  
operatingPoint |  A row 向量 containing 该 input operating points 对应的 到 该 input 频率 responses 在 该 columns 的 该 input 矩阵  
operatingPointInterpolated |  A row 向量 containing 值 的 该 linearly interpolated 值 的 operating points between 该 input 值 的 operating points  
output |  A 矩阵 使用 该 column vectors containing 该 fit 频率 response 用于 each input operating point  
outputInterpolated |  A 矩阵 使用 该 column vectors containing 该 fit 频率 response 用于 each linearly interpolated operating point contained 在 row 向量 ‘operatingPointInterpolated’.  
  
注意:

This 脚本 函数 also produces 一个 gain filter coefficients 到 为 used 通过 该 TWLM 元素. The name 的 该 文件 将 为 outputfilename.mcfdb. 

**示例**

Please refer 到 该 application example page [ Gain Fitting ](/hc/en-us/articles/360042820953) 用于 该 detailed usage 的 此 命令.

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ mcfit ](/hc/en-us/articles/360034930333-mcfit)
