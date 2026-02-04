# opensession

通过自动化 API 打开所选 Lumerical 产品的服务器会话的互操作性命令。打开会话后，客户端产品可以调用服务器执行任意 Lumerical 脚本命令并执行它们。打开的 Lumerical 会话还允许从工作区发送和获取变量。

**语法** | **描述**
---|---
s2=opensession('device'); | 执行此命令将通过自动化 API 打开 Device 会话。接受的参数：'fdtd' 'mode' 'device' 'interconnect'

**示例**

以下代码示例将 Device 打开为服务器，将局部变量 'x' 发送到 Device 工作区，然后发送命令来操作变量并在关闭会话之前检索结果：

```
# 打开 Device 会话
s2=opensession('device');
# 声明局部变量 x
x=2;
# 通过 API 将局部变量发送到 Device 工作区
putremotedata(s2,'x_device',x);
# 通过 API 向 Device 发送脚本命令并对变量求平方
evalremote(s2,"y_device=x_device^2;");
# 通过 API 从 Device 工作区获取变量
?y=getremotedata(s2,'y_device');
# 关闭会话
closesession(s2);
```

**另请参阅**

- [closesession](./closesession.md)
- [putremotedata](./putremotedata.md)
- [getremotedata](./getremotedata.md)
- [evalremote](./evalremote.md)
