<!--
Translation from English documentation
Original command: visualize
Translation date: 2026-02-04 22:50:15
-->

# visualize

Sends 数据 到 该 [visualizer](/hc/en-us/articles/360037222234).

For FDTD, MODE, DGTD, FEEM, CHARGE, HEAT, 和 INTERCONNECT

**语法** |  **描述**  
---|---  
visualize(R); |  Plots 该 dataset R 在 该 Visualizer.  
visualize(R,T); |  Sends two data设置到 该 Visualizer。  
  
**示例**

This example 创建 一个 3D dataset 的 random numbers 和 plots it 在 该 visualizer. An additional dataset 是 created 和 added 到 该 visualizer 使用 add2visualizer.
    
    
    nPts=10;
    axis=1:nPts;
    数据=randmatrix(nPts,nPts,nPts);
    dataset = rectilineardataset("dataset",axis,axis,axis);
    dataset.addattribute("数据",数据);
    visualize(dataset);
    dataset2 = rectilineardataset("dataset2",axis,axis,axis);
    dataset2.addattribute("数据",数据+10);
    add2visualizer(dataset2, 1);

**参见**

[Datasets](/hc/en-us/articles/360034409554-Datasets), [exportfigure](/hc/en-us/articles/360034410574-exportfigure), [image](/hc/en-us/articles/360034931253-image), [plot](/hc/en-us/articles/360034410474-plot), [setplot](/hc/en-us/articles/360034931293-setplot), [closeall](/hc/en-us/articles/360034410594-closeall), [add2visualizer](/hc/en-us/articles/360034410534-add2visualizer)
