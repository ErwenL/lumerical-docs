<!--
Translation from English documentation
Original command: getsurfaceconductivity
Translation date: 2026-02-04 22:50:00
-->

# getsurfaceconductivity

For materials 该 use 一个 surface conductivity 材料 model (such as Graphene), 此 函数 返回 该 complex index 的 any 材料 该 是 在 该 材料 database. The surface conductivity at 该 specified 频率 是 interpolated 从 该 neighboring frequencies 其中 该 conductivity 数据 是 available. For 一个 list 的 materials 该 use 该 surface conductivity model, see [ Material conductivity models ](/hc/en-us/articles/360034915113-Material-Conductivity-Models) . 

**语法** |  **描述**  
---|---  
out = getsurfaceconductivity( "materialname", f);  |  返回 该 surface conductivity (在 units 的 S) 的 该 材料 使用 该 given name. The surface conductivity 是 returned 用于 该 specified 频率 f 其中 f 是 在 units 的 Hz.   
getsurfaceconductivity( "materialname", f, component);  |  Optional 参数 component 可以 为 1, 2 或 3 到 specify 该 x, y 或 z component 用于 anisotropic materials. The default 是 1.   
  
**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getfdtdsurfaceconductivity ](/hc/en-us/articles/360034930133-getfdtdsurfaceconductivity)
