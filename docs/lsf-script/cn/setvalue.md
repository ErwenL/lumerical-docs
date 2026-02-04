# setvalue

> **原文**: setvalue  
> **翻译日期**: 2026-02-03  
> **翻译状态**: ✅ 已完成

设置元素内部参数的内部值。

| **语法** | **说明** |
| --- | --- |
| setvalue(element, parameter ,value); | 为'element'的内部'parameter'设置内部值。与'set'或'setnamed'不同，'setvalue'可以直接访问内部元素参数。目前只有'Optical N Port S-Parameter'支持此功能用于内部's parameters'值。's parameters'参数是一个包含元素s参数完整描述的单元。 |

**示例**

```
M=cell(3);
M{1}=struct;
M{1}.numberOfNPorts=-1;
M{2}=struct;
M{2}.numberOfMPorts=-1;
M{3}=cell(1);
M{3}{1}=struct;
M{3}{1}.data=matrix(5,3);
M{3}{1}.data(1,1)=2.26258e+014;
M{3}{1}.data(2,1)=2.27569e+014;
M{3}{1}.data(3,1)=2.28879e+014;
M{3}{1}.data(4,1)=2.3019e+014;
M{3}{1}.data(5,1)=2.315e+014;
M{3}{1}.data(1,2)=0.0104993;
M{3}{1}.data(2,2)=0.00926858;
M{3}{1}.data(3,2)=0.00596999;
M{3}{1}.data(4,2)=0.00182042;
M{3}{1}.data(5,2)=0.00429422;
M{3}{1}.data(1,3)=-2.64534;
M{3}{1}.data(2,3)=-2.75636;
M{3}{1}.data(3,3)=-2.89119;
M{3}{1}.data(4,3)=-3.62524;
M{3}{1}.data(5,3)=-5.23423;
M{3}{1}.modeInputLabel='TE';
M{3}{1}.modeInputOID=1;
M{3}{1}.modeInputUID='#1';
M{3}{1}.modeOutputLabel='TE';
M{3}{1}.modeOutputOID=1;
M{3}{1}.modeOutputUID='#1';
M{3}{1}.portInput='port 1';
M{3}{1}.portOutput='port 2';
# 为元素SPAR_1设置s参数
setvalue('SPAR_1','s parameters',M);
```

**相关命令**

[getvalue](./getvalue.md)
