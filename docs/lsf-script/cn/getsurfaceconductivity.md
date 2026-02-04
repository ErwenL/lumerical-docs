<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getsurfaceconductivity -->

# getsurfaceconductivity

**语法** | **描述**
---|---
out = getsurfaceconductivity( "materialname", f); | 返回 the surface conductivity (in units of S) of the material with the given name. The surface conductivity is returned for the specified 频率 f where f is in units of Hz.
getsurfaceconductivity( "materialname", f, component); | Optional 参数 component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default is 1.

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addmaterial ](/hc/en-us/articles/360034930013-addmaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getfdtdsurfaceconductivity ](/hc/en-us/articles/360034930133-getfdtdsurfaceconductivity)
