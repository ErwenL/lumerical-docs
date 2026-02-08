# newwizard

Used to create a new user defined wizard. Opens a new wizard window.

| **Syntax**                 | **Description** |
| -------------------------- | --------------- |
| newwizard( w, h, "title"); |                 |

- w and h (width and height) are specified in pixels. The minimum values for w and h are
  200\.
- title is the wizard window title.

**Examples**

In this example we will make a widget that will make 4 power monitors in the shape of a
square to encase a 2D simulation. Create a new script file and add the following code to
it:

```
#open the new wizard
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
# get the user set dimensions
out = runwizard;
xmin=wizardgetdata(1)*1e-6;
xmax=wizardgetdata(2)*1e-6;
ymin=wizardgetdata(3)*1e-6;
ymax=wizardgetdata(4)*1e-6;
killwizard;
### break if the user cancelled
if(out==0) {
?"User cancelled";
break;
}
#if the user pressed "Go", add the monitor box
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

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ message ](./message.md)
