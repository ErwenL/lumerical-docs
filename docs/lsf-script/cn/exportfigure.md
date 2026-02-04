# exportfigure

将当前图形导出为 JPG 图像。如果未指定文件扩展名，将使用 ".jpg"。图像大小将与图形窗口大小相同。

如果文件被覆盖或导出失败，将生成警告。

**语法** | **描述**
---|---
exportfigure("filename"); | 将当前图形导出为名为 "filename" 的 JPG 图像。导出的图像大小与当前图形相同。
exportfigure("filename",xres,yres); | 导出的图像将具有指定的分辨率，xres 和 yres 分别表示 x、y 方向的分辨率。

**示例**

创建两个图形，然后选择第一个并将其导出为 .jpg 文件。首先使用 closeall 关闭所有先前打开的图形窗口。

```powershell
closeall;
x=linspace(0,10,100);
y1=sin(x);
y2=y1^2;
plot(x,y1,"x","y","title");
plot(x,y2,"x","y","title");
selectfigure(1);
exportfigure("sine.jpg");
```

**另请参阅**

[命令列表](../命令列表.md)、[selectfigure](./selectfigure.md)、[image](./image.md)、[plot](./plot.md)、[setplot](./setplot.md)、[closeall](./closeall.md)、[visualize](./visualize.md)