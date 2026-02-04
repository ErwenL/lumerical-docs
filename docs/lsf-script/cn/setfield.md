<!--
Translation from English documentation
Original command: setfield
Translation date: 2026-02-03
-->

# setfield

脚本命令为结构输入字段赋值。

**语法** | **描述**
---|----
output= setfield(input, field,value); | 将'value'赋值给结构'input'的'field'字段。

**示例**

```lsf
>x=struct;
>x=setfield(x,'t',10);
>?x.t;
result:
10
```

**另请参见**

- [isfield](./isfield.md)
- [getfield](./getfield.md)
