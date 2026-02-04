<!--
Translation from English documentation
Original command: jsonload
Translation date: 2026-02-03
-->

# jsonload

返回 JSON 文件的值。

**语法** |  **描述**
---|---
jsonload("filename");  |  返回 json 文件的值（结构体、单元格、字符串、数字）。

**示例**

以下代码示例显示如何加载 JSON 文件 "test_json.json" 的数据。

    jsonload("test_json.json");
    ?a;
    ?b;

输出结果如下：

    ?a;
    result:
    1
    ?b;
    result:
    1+2i  3+4i

**相关命令**

- [jsonsave](./jsonsave.md)
- [jsonloads](./jsonloads.md)
- [jsonsaves](./jsonsaves.md)
- [JSON files](./JSON-files.md)
