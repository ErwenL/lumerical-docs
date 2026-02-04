# pause

暂停程序一段时间。

**语法** | **描述**
---|---
pause(time); | 暂停脚本 time 秒。按空格键强制脚本继续。按 ESC 键在此处中断脚本。此函数不返回任何数据。

**示例**

暂停 5 秒。

```
pause(5);
```

暂停直到用户点击空格键。

```
?"Part 1 complete. Hit space bar to proceed with part 2.";
pause(10000);
```

**另请参阅**

- [命令列表](./命令列表.md)
- [break](./break.md)
- [ESCAPE 键](./ESCAPE%20键.md)
