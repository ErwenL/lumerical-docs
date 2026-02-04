<!--
---
**Translation metadata**
- English title: splitstring
- Chinese title: splitstring - 字符串分割
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Beginner
- Priority: Standard
---
-->

# splitstring

将长字符串分割成一系列子字符串，子字符串存储在单元格（即字符串）数组中。

| **语法** | **描述** |
|---|---|
| s2 = splitstring(s1,endl); | 使用行尾字符作为分隔符将字符串 S1 分割成一系列字符串。S2 是单元格数组。 |

**示例**

使用 splitstring 命令以单元格（即字符串）数组形式获取目录内容。然后遍历数组查找所有 FDTD 项目文件（.fsp）。

```
files = splitstring(dir,endl);        # 单元格（字符串）数组形式的目录内容
for(i=1:length(files)) {           # 遍历所有文件
 if (findstring(files{i},"fsp") != -1) {  # 查找 'fsp' 文件
  if (fileexists(files{i})) {       # 检查文件是否存在（即它是文件而非目录）
  ?files{i};               # 输出文件名
  load(files{i});            # 加载文件
  }
 }
}
```

另一个获取模拟中所有监视器名称的类似示例。遍历所有监视器，检查它们是否包含名为 'E' 的结果。如果是，将该数据保存到文件。

```
mNames = splitstring(getresult,endl);
 
for (i=1:length(mNames)) {
 if (haveresult(mNames{i},"E")) {
  E=getresult(mNames{i},"E");   # 从该监视器获取结果
 } else {
  E = mNames{i} + " did not contain the specified data.";
 }
 filename = "file"+num2str(i);
 savedata(filename,E);     # 将数据保存到 ldf 文件
}
```

**另请参见**

[ 命令列表 ](./command_list.md) , [ length ](./length.md) , [ substring ](./substring.md) , [ findstring ](./findstring.md) , [ replace ](./replace.md) , [ str2num ](./str2num.md) , [ num2str ](./num2str.md) , [ cell ](./cell.md) , [ dir ](./dir.md) , [ getresult ](./getresult.md) , [ lower ](./lower.md) , [ upper ](./upper.md) , [ toscript ](./toscript.md)
