<!--
Translation from English documentation
Original command: getfdtdsurfaceconductivity
Translation date: 2026-02-04 22:50:00
-->

# getfdtdsurfaceconductivity

For materials 该 use 一个 surface conductivity 材料 model (such as Graphene), 此 函数 返回 该 surface conductivity 的 该 材料 在 该 database as it 将 为 used 在 一个 actual 仿真. For 一个 list 的 materials 该 use 该 surface conductivity model, see [ Material conductivity models ](/hc/en-us/articles/360034915113-Material-Conductivity-Models) . 

The conductivity evaluated at 该 specified frequencies 是 returned. 注意 该 该 fit result depends 在 该 fit 参数, Max coefficients 和 Tolerance 设置 用于 该 材料, thus getfdtdsurfaceconductivity result depends 在 那些 参数 as well. 

**语法** |  **描述**  
---|---  
out = getfdtdsurfaceconductivity( "materialname", f, fmin, fmax);  |  返回 该 surface conductivity (在 units 的 S) 的 该 材料 使用 该 given name. The surface conductivity 是 returned 用于 该 specified 频率 f. Similar 到 getsurfaceconductivity, but you also specify fmin 和 fmax, 该 span 的 频率 range 的 该 仿真. All 频率 units 是 在 Hz.   
getfdtdsurfaceconductivity("materialname", f,fmin, fmax, component);  |  Optional 参数 component 可以 为 1, 2 或 3 到 specify 该 x, y 或 z component 用于 anisotropic materials. The default 是 1.   
  
**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getsurfaceconductivity ](/hc/en-us/articles/360034409754-getsurfaceconductivity)
