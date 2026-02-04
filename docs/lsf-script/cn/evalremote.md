# evalremote

一种互操作性命令，将脚本命令发送到服务器产品并在那里执行。

**语法** | **描述**
---|---
evalremote(s,"y=x^2;"); | 通过开放会话 s 将命令 y=x^2; 发送到服务器并执行。

### 示例

以下代码示例打开 Device 作为服务器，将本地变量 'x' 发送到 Device 工作区，然后发送操作变量的命令，并在关闭会话前检索结果：

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

[opensession](./opensession.md)、[closesession](./closesession.md)、[putremotedata](./putremotedata.md)、[getremotedata](./getremotedata.md)
