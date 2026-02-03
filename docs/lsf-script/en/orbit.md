# orbit

This command performs an elliptical viewing orbit of the structure in the perspective view. Note that the commands [setview](/hc/en-us/articles/360034929173-setview), [getview](/hc/en-us/articles/360034408874-getview) and [redraw](/hc/en-us/articles/360034929133-redraw) make it possible to create any type of orbit you would like in your own script file.

**Syntax** |  **Description**  
---|---  
orbit; |  Performs an orbit of the current perspective view.  
orbit(zoom_factor); |  Performs an orbit with the specified minimum zoom factor. By default the zoom factor is 1.5.  
orbit(zoom_factor, frame_rate); |  Performs an orbit with the specified frame rate specified in frames per second. The default frame rate is 15.  
  
**Example**

Type in orbit in the prompt and you will see that the perspective view is in rotation.

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [setview](/hc/en-us/articles/360034929173-setview), [getview](/hc/en-us/articles/360034408874-getview), [framerate](/hc/en-us/articles/360034929233-framerate)
