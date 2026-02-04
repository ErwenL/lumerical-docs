<!-- Translation: unselectall -->
<!-- Date: 2026-02-03 -->
<!-- Original: unselectall -->

# unselectall

取消选择所有对象和组。这是[selectall](./selectall.md)的反向操作。

**语法** | **说明**
---|---
unselectall; | 取消选择所有对象和组。此函数不返回任何数据。

**示例**

以下脚本添加两个对象，选择它们并设置它们的x位置。然后取消选择它们以进行其他修改。


    addrect;
    set("name","A1");
    addring;
    set("name","ring");
    selectall;
    set("x",-1e-6);
    unselectall;

**参见**

[操作对象](./360037228834.md), [selectall](./selectall.md)
