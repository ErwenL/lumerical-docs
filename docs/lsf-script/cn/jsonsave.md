<!--
Translation from English documentation
Original command: jsonsave
Translation date: 2026-02-04 22:50:01
-->

# jsonsave

Saves 数据 到 一个 JSON 文件.

**语法** |  **描述**  
---|---  
jsonsave("文件名"); |  Saves all 数据 在 workspace 到 一个 JSON 文件 使用 该 explicit Lumerical Cell 和 Matrix Option 1 notation. For detailed information 在 该 notations, please see 该 page [ JSON files ](/hc/en-us/articles/360034936933-JSON-files) .  
jsonsave("文件名", var1, var2, ...); |  Saves 该 specified 数据 variables 到 一个 JSON 文件 使用 该 explicit Lumerical Cell 和 Matrix Option 1 notation. For detailed information 在 该 notations, please see 该 page [ JSON files ](/hc/en-us/articles/360034936933-JSON-files) .  
  
### 示例

The following code example shows 如何 到 save 该 数据 在 Lumerical workspace 到 一个 JSON 文件.
    
    
    # 创建 variables 一个 和 b
    一个 = 1;
    b = [1+2i, 3+4i];
    jsonsave("test_json.json");

Data 在 该 "test_json.json" 文件:

{ "一个" : 1, "b" : { "_complex" : true, "_data" : [ 1, 2, 3, 4 ], "_size" : [ 1, 2 ], "_type" : "矩阵" } }  
  
Specify 该 variables you would like 到 save 在 your workspace.
    
    
    一个 = 1;  
    b = [1+2i, 3+4i];  
    字符串 = "字符串";  
    jsonsave("test_json.json",一个,字符串);

创建 该 following json 文件.
    
    
    {  
     "一个" : 1,  
     "字符串" : "字符串"  
    }

**参见**

[ jsonload ](/hc/en-us/articles/360034408194-jsonload) , [ jsonloads ](/hc/en-us/articles/360038741854) , [ jsonsaves ](/hc/en-us/articles/360039235453) , [ JSON files ](/hc/en-us/articles/360034936933-JSON-files)
