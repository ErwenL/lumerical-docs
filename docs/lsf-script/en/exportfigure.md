# exportfigure

Exports the current figure to a JPG image. If the file extension is not specified, ".jpg" will be used. The image size will be the same as the figure window size. 

If a file is overwritten or if the export fails, a warning will be generated. 

**Syntax** |  **Description**  
---|---  
exportfigure("filename");  |  Exports the current figure to a JPG image with the name "filename".  The exported image will have the same size as the current figure.   
exportfigure("filename",xres,yres);  |  The exported image will have the specified resolution, xres,yres, in the x,y directions respectively.   
  
**Example**

Create two figures, then select the first and export it to a .jpg file. All the previously opened figure windows are closed beforehand using closeall. 
    
    
    closeall;
    x=linspace(0,10,100);
    y1=sin(x);
    y2=y1^2;
    plot(x,y1,"x","y","title");
    plot(x,y2,"x","y","title");
    selectfigure(1);
    exportfigure("sine.jpg");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ selectfigure ](/hc/en-us/articles/360034410554-selectfigure) , [ image ](/hc/en-us/articles/360034931253-image) , [ plot ](/hc/en-us/articles/360034410474-plot) , [ setplot ](/hc/en-us/articles/360034931293-setplot) , [ closeall ](/hc/en-us/articles/360034410594-closeall) , [ visualize ](/hc/en-us/articles/360034410514-visualize)
