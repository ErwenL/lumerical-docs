<!--
Translation from English documentation
Original command: chebin
Translation date: 2026-02-04 22:49:36
-->

# chebin

返回 该 Chebyshev interpolation 的 一个 sampled 函数. Chebyshev interpolation 是 useful 用于 accurately interpolating 一个 smooth 函数 使用 一个 very small 数字 的 samples. The key requirement 用于 此 类型 的 interpolation 到 work 是 该 该 函数 是 sampled 在 该 Chebyshev roots grid.

**语法** |  **描述**  
---|---  
chebin(f,x,xi,xmin,xmax) |  Interpolates 该 函数 f onto 该 xi points. It assumes 该 f contains 该 samples 的 该 函数 taken 在 该 Chebyshev roots grid specified 在 x; x 必须 为 constructed 通过 该 call # x = chpts(xmin,xmax,NumPts), otherwise 一个 error 是 returned.  
  
**示例**

See example 用于 该 chpts 命令.

**参见**

[dcht](/hc/en-us/articles/360034406734-dcht),[chpts](/hc/en-us/articles/360034406614-chpts),[icht](/hc/en-us/articles/360034406634-chebin)
