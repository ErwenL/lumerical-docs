<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getfdtdsurfaceconductivity -->

# getfdtdsurfaceconductivity

**语法** | **描述**
---|---
out = getfdtdsurfaceconductivity( "materialname", f, fmin, fmax); | 返回 the surface conductivity (in units of S) of the material with the given name. The surface conductivity is returned for the specified 频率 f. Similar to getsurfaceconductivity, but you also specify fmin and fmax, the span of 频率 range of the 仿真. All 频率 units are in Hz.
getfdtdsurfaceconductivity("materialname", f,fmin, fmax, component); | Optional 参数 component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getsurfaceconductivity ](/hc/en-us/articles/360034409754-getsurfaceconductivity)
