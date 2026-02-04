<!--
Translation from English documentation
Original command: legend
Translation date: 2026-02-03
-->

# legend

向线图添加图例。

**语法** |  **描述**
---|---
legend("legend1","legend2",..., "legendn"); |  向所选图形添加图例。参数可以是字符串或字符串数组（单元格）。此函数不返回任何数据。

**示例**

使用字符串数组添加图例。

    x=linspace(0,10,100);
    y1=sin(x);
    y2=y1^2;
    plot(x,y1,y2,"x","y","title");

    # create an array of strings
    leg=cell(2);
    leg{1}="y1";
    leg{2}="y2";

    # add legend
    legend(leg);

使用 for 循环向图例添加数字。

    n=5; # number of legend
    leg=cell(n); # define the array of strings
    y=linspace(10,50,n);
    for (i=1:n){
    leg{i}=num2str(y(i));
    }

    # add legend
    legend(leg);

**相关命令**

- [List of commands](./List-of-commands.md)
- [plot](./plot.md)
- [closeall](./closeall.md)
- [visualize](./visualize.md)
