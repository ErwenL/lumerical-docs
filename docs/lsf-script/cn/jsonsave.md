<!--
Translation from English documentation
Original command: jsonsave
Translation date: 2026-02-03
-->

# jsonsave

将数据保存到 JSON 文件。

**语法** |  **描述**
---|---
jsonsave("filename"); |  使用明确的 Lumerical 单元格和矩阵选项 1 符号将工作区中的所有数据保存到 JSON 文件，有关符号的详细信息，请参阅 JSON 文件页面。
jsonsave("filename", var1, var2, ...); |  使用明确的 Lumerical 单元格和矩阵选项 1 符号将指定的数据变量保存到 JSON 文件，有关符号的详细信息，请参阅 JSON 文件页面。

**示例**

以下代码示例显示如何将 Lumerical 工作区中的数据保存到 JSON 文件。

    # Create variables a and b
    a = 1;
    b = [1+2i, 3+4i];
    jsonsave("test_json.json");

"test_json.json" 文件中的数据：

    { "a" : 1, "b" : { "_complex" : true, "_data" : [ 1, 2, 3, 4 ], "_size" : [ 1, 2 ], "_type" : "matrix" } }

指定您要保存在工作区中的变量。

    a = 1;
    b = [1+2i, 3+4i];
    string = "string";
    jsonsave("test_json.json",a,string);

创建以下 json 文件。

    {
     "a" : 1,
     "string" : "string"
    }

**相关命令**

- [jsonload](./jsonload.md)
- [jsonloads](./jsonloads.md)
- [jsonsaves](./jsonsaves.md)
- [JSON files](./JSON-files.md)
