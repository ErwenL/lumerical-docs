<!-- Translation completed: 2026-02-04 -->
<!-- Original command: visualize -->

# visualize

**语法** | **描述**
---|---
visualize(R); | Plots the 数据集 R in the Visualizer.
visualize(R,T); | Sends two datasets to the Visualizer.

**示例**

This 示例 creates a 3D 数据集 of random numbers and plots it in the visualizer. An additional 数据集 is created and added to the visualizer using add2visualizer.
    nPts=10;
    axis=1:nPts;
    data=randmatrix(nPts,nPts,nPts);
    数据集 = rectilineardataset("数据集",axis,axis,axis);
    数据集.addattribute("data",data);
    visualize(数据集);
    dataset2 = rectilineardataset("dataset2",axis,axis,axis);
    dataset2.addattribute("data",data+10);
    add2visualizer(dataset2, 1);

This 示例 creates a 3D 数据集 of random numbers and plots it in the visualizer. An additional 数据集 is created and added to the visualizer using add2visualizer.
    nPts=10;
    axis=1:nPts;
    data=randmatrix(nPts,nPts,nPts);
    数据集 = rectilineardataset("数据集",axis,axis,axis);
    数据集.addattribute("data",data);
    visualize(数据集);
    dataset2 = rectilineardataset("dataset2",axis,axis,axis);
    dataset2.addattribute("data",data+10);
    add2visualizer(dataset2, 1);

**另请参阅**

[Datasets](/hc/en-us/articles/360034409554-Datasets), [exportfigure](/hc/en-us/articles/360034410574-exportfigure), [image](/hc/en-us/articles/360034931253-image), [plot](/hc/en-us/articles/360034410474-plot), [setplot](/hc/en-us/articles/360034931293-setplot), [closeall](/hc/en-us/articles/360034410594-closeall), [add2visualizer](/hc/en-us/articles/360034410534-add2visualizer)
