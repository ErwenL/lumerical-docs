# %（百分号）

用于创建包含空格的变量名。

**命令** | **描述**
---|---
%variable with space% | 要创建包含空格的变量名（如 "variable with space"），请在变量名前后放置百分号。

**示例**

```
%variable with space%=2;
?%variable with space%*3;
result:
6
%x span% = get("x span");
?%x span% * 1e6;  # 以微米为单位的 x span
result:
4.8
```

**另请参阅**

- [命令列表](./命令列表.md)
