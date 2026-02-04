<!--
Translation from English documentation
Original command: farfieldpolar3d
Translation date: 2026-02-04 22:49:48
-->

# farfieldpolar3d

The 函数 farfieldpolar3d 是 similar 到 farfield3d, but it 返回 该 complex electric fields, rather than field intensity. The 数据 是 returned as 矩阵 的 NxMx3 (如果 one 频率 point 是 projected) 或 NxMx3xP (如果 more than 1 频率 point 是 projected), 其中 N 和 M 是 spatial indices, 该 third index refers 到 E  r  , E  θ  和 E  φ  , 在 spherical coordinates, 和 P 是 该 数字 的 频率 points. The components E  r  , E  θ  和 E  φ  是 该 complex components 的 该 electric field 向量. See 该 farfield3d documentation 用于 information 在 interpreting ux, uy, na, nb 用于 various 监视器 orientations.

注意: When viewing far fields 从 该 GUI 使用 该 visualizer, three Attributes 是 available: E2, Ep, Es. E2 corresponds 到 |E|^2, Ep 到 Etheta, 和 Es 到 Ephi.

**语法** |  **描述**  
---|---  
out = farfieldpolar3d( "mname",...); |  返回 该 spherical complex electric fields. Same 参数 as farfield3d.  
out = farfieldpolar3d( dataset,...); |  返回 该 spherical complex electric fields. Same 参数 as farfield3d.  
  
**示例**

See example in the [farfield3d ](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d) function description.

**参见**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ farfield3d ](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d) , [ farfieldvector3d ](https://optics.ansys.com/hc/en-us/articles/360034410114-farfieldvector3d) , [ Far field projections - Field polarization ](https://optics.ansys.com/hc/en-us/articles/360034914753-FFP-Field-polarization)
