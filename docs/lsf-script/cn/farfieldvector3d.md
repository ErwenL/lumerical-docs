<!--
Translation from English documentation
Original command: farfieldvector3d
Translation date: 2026-02-04 22:49:49
-->

# farfieldvector3d

The 函数 farfieldvector3d 是 similar 到 farfield3d, but it 返回 该 complex electric fields, rather than field intensity. The 数据 是 returned as 矩阵 的 NxMx3 (如果 one 频率 point 是 projected) 或 NxMx3xP (如果 more than 1 频率 point 是 projected), 其中 N 和 M 是 spatial indices, 该 third index refers 到 Ex, Ey 和 Ez 在 spherical coordinates, 和 P 是 该 数字 的 频率 points. The components Ex, Ey 和 Ez 是 该 complex components 的 该 electric field 向量. See 该 farfield3d documentation 用于 information 在 interpreting ux, uy, na, nb 用于 various 监视器 orientations.

**语法** |  **描述**  
---|---  
out = farfieldvector3d( "mname",...); |  返回 该 cartesian complex electric fields. Same 参数 as farfield3d.  
out = farfieldvector3d( dataset,...); |  返回 该 cartesian complex electric fields. Same 参数 as farfield3d.  
  
**示例**

See example in the [farfield3d](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d) function description.

[Understanding field polarization in far field projections](https://optics.ansys.com/hc/en-us/search/click?data=BAh7DjoHaWRsKwjB0cDTUwA6D2FjY291bnRfaWRpA02AjDoJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ2aHR0cHM6Ly9vcHRpY3MuYW5zeXMuY29tL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkxNDc1My1VbmRlcnN0YW5kaW5nLWZpZWxkLXBvbGFyaXphdGlvbi1pbi1mYXItZmllbGQtcHJvamVjdGlvbnMGOwhUOg5zZWFyY2hfaWRJIilkYjc4YzM5Yy1iOWU1LTRjNWUtYjE0NC02MGQzNjA4MGRkYWIGOwhGOglyYW5raQg6C2xvY2FsZUkiCmVuLXVzBjsIVDoKcXVlcnlJIhNmYXJmaWVsZHZlY3RvcgY7CFQ6EnJlc3VsdHNfY291bnRpEg%3D%3D--90007a278d7628d12a8c14265df095c4975dd311)

**参见**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ farfield3d ](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d) , [ farfieldpolar3d ](https://optics.ansys.com/hc/en-us/articles/360034930713-farfieldpolar3d) , [ Far field projections - Field polarization ](https://optics.ansys.com/hc/en-us/articles/360034914753-FFP-Field-polarization)
