# for

启动 for 循环以允许某些操作重复执行多次。使用 for 循环的三参数版本可以实现 while 循环。

**语法** | **描述**
---|---
for(x=1:100) { ?x; } | 单参数 for 循环。循环将按顺序为 x 的每个值执行。
for(x=1; x<= 100; x=x+1) { ?x; } | 三参数 for 循环。循环开始时 x=1。只要 x <=100，循环就继续，并在每次遍历时设置 x=x+1。
x=1; for(0; x<10; 0) { ?x; x=x+1; } | 这等同于执行 x<10 的 while 循环。

**示例**

此示例显示一个简单的 for 循环，其中 x 取值 1、3、5、7、9。

```powershell
a=1:2:10;
for(x=a) {
    ?x;
}
```

嵌套循环：此示例显示一个嵌套的 for 循环。

```powershell
for(i=1:100) {
    for(j=1:100) {
        x = i^2+j;
        ?x;
    }
}
```

以下代码将从该仿真文件中的每个监视器获取电场数据，然后将该数据保存为一系列 Lumerical 数据文件。要测试此示例，请下载相关仿真文件，运行仿真，然后运行以下脚本。

```powershell
run;
mNames = splitstring(getresult,endl);

for (i=1:length(mNames)) {
    if (haveresult(mNames{i},"E")) {
        E=getresult(mNames{i},"E");   # 从该监视器获取结果
    } else {
        E = mNames{i} + " did not contain the specified data.";
    }
    savedata(mNames{i},E);     # 将数据保存到文件
}
```

While 循环：脚本语言中没有"while"命令，但可以使用"for"命令实现"while"命令。命令 for(0; conditional_expression; 0) {} 等同于 while(conditional_expression) {}。"for"循环中的"0"语句什么都不做，只是占位符，因为脚本语言期望那里有一个参数。

```powershell
# 支持 while 循环的语言中 while 循环的实现
x=1;
while(x<10) {
    ?x;
    x=x+1;
}
# Lumerical 脚本语言中等效的 while 循环实现
x=1;
for(0; x<10; 0) {
    ?x;
    x=x+1;
}
```

**另请参阅**

[命令列表](../命令列表.md)、[if](./if.md)