# framerate

Orbits the perspective view and returns the framerate. This can be useful for estimating your graphics performance. If comparing the performance of two computers, be sure to use exactly the same simulation file.

**Syntax** |  **Description**  
---|---  
fr = framerate(num_frames, zoom); |  num_frames - Number of frames to draw zoom - Zoom factor used in perspective view fr - number of frames / wall time required to complete orbit.  
  
**Example**
    
    
    framerate(1000,2);

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [setview](/hc/en-us/articles/360034929173-setview), [getview](/hc/en-us/articles/360034408874-getview), [orbit](/hc/en-us/articles/360034929193-orbit)
