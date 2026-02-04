# putremotedata

一种互操作性命令，通过活动会话将变量从客户端工作区发送到服务器工作区。这适用于矩阵和字符串（不适用于结构和单元数组）。

**语法** | **描述**
---|---
putremotedata(s,'y',x); | 通过活动会话 s，在服务器工作区中创建变量 y，其值为客户端工作区中的 x。

### 示例

以下代码示例打开 Device 作为服务器，将本地变量 'x' 发送到 Device 工作区，然后发送操作变量的命令并在关闭会话前检索结果：

```powershell
#打开 Device 会话
s2=opensession('device');
#声明本地变量 x
x=2;
#通过 API 将本地变量发送到 Device 工作区
putremotedata(s2,'x_device',x);
#通过 API 向 Device 发送脚本命令并对变量求平方
evalremote(s2,"y_device=x_device^2;");
#通过 API 从 Device 工作区获取变量
?y=getremotedata(s2,'y_device');
#关闭会话
closesession(s2);
```

**另请参阅**

[opensession](./opensession.md)、[closesession](./closesession.md)、[getremotedata](./getremotedata.md)、[evalremote](./evalremote.md)
