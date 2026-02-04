# newwizard

用于创建新的用户定义向导。打开新的向导窗口。

**语法** | **描述**
---|---
newwizard( w, h, "title"); | 

  * w 和 h（宽度和高度）以像素为单位指定。w 和 h 的最小值为 200。
  * title 是向导窗口标题。

**示例**

在此示例中，我们将创建一个构件，该构件将创建 4 个方形功率监视器以包围 2D 模拟。创建新的脚本文件并向其中添加以下代码：

```
# 打开新向导
newwizard(300,200,"Power Box Wizard");
wizardoption("fontsize",12);
wizardoption("fieldwidth",150);
wizardoption("fieldheight",20);
wizardoption("margin",20);
newwizardpage("Go");
wizardwidget("label",endl+"Choose the dimensions in for the Power Box"+endl);
wizardoption("margin",50);
wizardwidget("number","x min (um):");
wizardwidget("number","x max (um):");
wizardwidget("number","y min (um):");
wizardwidget("number","y max (um):");
# 获取用户设置的维度
out = runwizard;
xmin=wizardgetdata(1)*1e-6;
xmax=wizardgetdata(2)*1e-6;
ymin=wizardgetdata(3)*1e-6;
ymax=wizardgetdata(4)*1e-6;
killwizard;
### 如果用户取消则中断
if(out==0) {
?"User cancelled";
break;
}
# 如果用户按下了 "Go"，添加监视器框
monitors;
addpower;
set("monitor type","Linear X");
set("name","x1");
set("x",(xmax+xmin)/2);
set("y",ymin);
set("x span",xmax-xmin);
copy;
set("name","x2");
set("x",(xmax+xmin)/2);
set("y",ymax);
addpower;
set("name","y1");
set("monitor type","Linear Y");
set("y",(ymax+ymin)/2);
set("x",xmin);
set("y span",ymax-ymin);
copy;
set("name","y2");
set("y",(ymax+ymin)/2);
set("x",xmax);
```

**另请参阅**

- [命令列表](./命令列表.md)
- [message](./message.md)
