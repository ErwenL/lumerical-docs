<!--
Translation from English documentation
Original command: farfieldexact2d
Translation date: 2026-02-04 22:49:48
-->

# farfieldexact2d

This 函数 projects complete complex 向量 fields 到 specific locations. It 是 expected 到 为 correct down 到 distances 在 该 order 的 one 波长. The projections 从 multiple monitors 可以 为 added 到 创建 一个 total far field projection - see [ Projections 从 一个 监视器 box ](/hc/en-us/articles/360034915613-Projections-从-一个-监视器-box) .

farfieldexact2d projects any surface 到 该 grid points defined 通过 该 vectors x, y. If only E field 是 returned as 该 result, 该 数据 是 returned 在 该 form 的 一个 矩阵 该 是 的 维度 NxMxPx3 其中 N 是 该 长度 的 该 x 向量, M 是 该 长度 的 该 y 向量, P 是 该 数字 的 频率 points, 和 该 final index represents Ex, Ey, 和 Ez. 注意 该 N 和 M 可以 为 1; 当 they 是 both 1, 该 函数 是 该 same as farfieldexact. If both E 和 H fileds 是 returned, 该 数据 是 returned as 一个 dataset 使用 该 E 和 H fields packaged 使用 该 对应的 x,y, 和 频率/波长.

**语法** |  **描述**  
---|---  
out = farfieldexact2d( "mname", x, y, f, index); |  Projects 一个 given power 或 field profile 监视器 到 该 far field at grid points specified 通过 该 vectors x,y. 返回 E field only.  
out = farfieldexact2d( dataset, x, y, f, index); |  Projects 一个 given rectilinear dataset 到 该 far field at grid points specified 通过 该 vectors x,y. 返回 E field only.  
out = farfieldexact2d( "mname", x, y, opt); |  Projects 一个 given power 或 field profile 监视器 到 该 far field at grid points specified 通过 该 vectors x,y. 返回 E filed 或 E 和 H fields. Refer 到 该 following table 用于 该 options.  
out = farfieldexact2d( dataset, x, y, opt); |  Projects 一个 given rectilinear dataset 到 该 far field at grid points specified 通过 该 vectors x,y. 返回 E filed 或 E 和 H fields. Refer 到 该 following table 用于 该 options.  
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
mname |  required |  |  字符串 |  name 的 该 监视器 从 该 far field 是 calculated.  
dataset |  required |  |  dataset |  Rectilinear dataset containing both E 和 H  
x |  required |  |  向量 |  x coordinates 的 该 grid points 其中 far field 是 calculated.  
y |  required |  |  向量 |  y coordinates 的 该 grid points 其中 far field 是 calculated.  
f |  optional | 1 |  向量 |  Index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. Multithreaded projection was introduced since R2016b.  
index |  optional | index at 监视器 center |  数字 |  The index 的 该 材料 到 use 用于 该 projection.  
opt |  optional |  |  结构体 |  该 'opt' 参数 includes 该 following options: "field": This 参数 是 optional. It defines 该 返回 field, 可以 either 为 "E" 或 "E 和 H". "f": This 参数 是 optional. It defines 该 index 的 该 desired 频率 point. This 可以 为 一个 single 数字 或 一个 向量. Multi-threaded projection was introduced since R2016b. "index": This 参数 是 optional. It defines 该 index 的 该 材料 到 use 用于 该 projection.  
  
[[注意:]] When 使用 一个 dataset, 该 default 值 的 该 refractive index 是 1.

**示例**

See example 在 farfieldexact3d 函数 description.

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldexact3d ](/hc/en-us/articles/360034930733-farfieldexact3d) , [ farfieldexact ](/hc/en-us/articles/360034410214-farfieldexact)
