<!-- Translation completed: 2026-02-04 -->
<!-- Original command: createsphericalsurface -->

# createsphericalsurface

**语法** | **描述**
---|---
out = createsphericalsurface([theta1,theta2],[phi1,phi2], [X,Y,Z],radius,lmax); | Creates an unstructured data set with a triangulated surface or a segmented arc. Their 维度 are specified by the 输入 angles, orientation axis and radius. The coarseness of the triangulation (or line segmentation) is specified as the 最大值 separation between adjacent points. The 输出 data set contains the IDs of each 元素 (triangles or lines) and the corresponding areas (only for triangles).
theta1 | optional
theta2 | optional
phi1 | optional
phi2 | optional
[X,Y,Z] | optional
radius | optional
lmax | optional

**示例**

This 示例 creates a spherical surface and performs a far 场 projection using the near 场 data from a surface 监视器 named "监视器". 
    surf = createsphericalsurface([0,pi/4],[0,2*pi],[0,0,1],1,0.1);
    E_near = getresult("DGTD::监视器","fields");
    E_far = near2far(E_near,surf);
    visualize(E_far); 

This 示例 creates an arc (in the XZ plane) and performs a far 场 projection using the near 场 data from a line 监视器 called "监视器" (also in the XZ plane). 
    surf = createsphericalsurface([pi/2,pi/2],[pi,2*pi],[0,1,0],1,0.1);
    E_near = getresult("DGTD::监视器","fields");
    E_far = near2far(E_near,surf);
    visualize(E_far); 

This 示例 creates an arc (in the XZ plane) and performs a far 场 projection using the near 场 data from a line 监视器 called "监视器" (also in the XZ plane). 
    surf = createsphericalsurface([pi/2,pi/2],[pi,2*pi],[0,1,0],1,0.1);
    E_near = getresult("DGTD::监视器","fields");
    E_far = near2far(E_near,surf);
    visualize(E_far); 

**另请参阅**

[ near2far ](/hc/en-us/articles/360034930753-near2far) , [ List of commands ](/hc/en-us/articles/360037228834) , 
