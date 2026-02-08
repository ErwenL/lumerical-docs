# visualize

Sends data to the [visualizer](/hc/en-us/articles/360037222234).

For FDTD, MODE, DGTD, FEEM, CHARGE, HEAT, and INTERCONNECT

**Syntax** |  **Description**  
---|---  
visualize(R); |  Plots the dataset R in the Visualizer.  
visualize(R,T); |  Sends two datasets to the Visualizer.  
  
**Example**

This example creates a 3D dataset of random numbers and plots it in the visualizer. An additional dataset is created and added to the visualizer using add2visualizer.
    
    
    nPts=10;
    axis=1:nPts;
    data=randmatrix(nPts,nPts,nPts);
    dataset = rectilineardataset("dataset",axis,axis,axis);
    dataset.addattribute("data",data);
    visualize(dataset);
    dataset2 = rectilineardataset("dataset2",axis,axis,axis);
    dataset2.addattribute("data",data+10);
    add2visualizer(dataset2, 1);

**See Also**

[Datasets](/hc/en-us/articles/360034409554-Datasets), [exportfigure](/hc/en-us/articles/360034410574-exportfigure), [image](/hc/en-us/articles/360034931253-image), [plot](/hc/en-us/articles/360034410474-plot), [setplot](/hc/en-us/articles/360034931293-setplot), [closeall](/hc/en-us/articles/360034410594-closeall), [add2visualizer](/hc/en-us/articles/360034410534-add2visualizer)
