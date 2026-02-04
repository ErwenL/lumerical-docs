# parsebackannotation

解析波导后向注释。

**语法** | **描述**
---|---
parsebackannotation(backannotation) | 解析波导后向注释。注释包含模式标签列表，对于每个模式，提供温度和波长相关的传播参数列表。该函数返回一个包含多个结构的单元向量，其中包含解析的数据。

**示例**

```
sIn = "( ( 'TE' ( '26.85' '1.5475u' 0.0501323 2.4485 4.19145 0.000138683 ) ( '26.85' '1.5u' 0.0501323 2.4485 4.19145 0.000138683 ) ) ( 'TM' ( '26.85' '1.5475u' 17.3718 1.785382 3.76608 -0.019477 ) ( '26.85' '1.5u' 17.3718 1.785382 3.76608 -0.019477 ) ) ( 'TX' ( '26.85' '1.5650u' 0.0485085 2.42879 4.19216 0.000133047 ) ( '26.85' '1.5u' 0.0485085 2.42879 4.19216 0.000133047 ) ) ( 'TY' ( '49.85' '1.5475u' 0.0501048 2.45306 4.19667 0.000154927 ) ( '49.85' '1.5u' 0.b0501048 2.45306 4.19667 0.000154927 ) ) ) ";
x=parsebackannotation(sIn);
?toscript(x);
x=cell(4);
x{1}=struct;
x{1}.dispersion=matrix(2);
x{1}.dispersion(1)=0.000138683;
x{1}.dispersion(2)=0.000138683;
x{1}.dispersion_temperature_sensitivity=matrix(2);
x{1}.dispersion_temperature_sensitivity(1)=0;
x{1}.dispersion_temperature_sensitivity(2)=0;
x{1}.effective_index=matrix(2);
x{1}.effective_index(1)=2.4485;
x{1}.effective_index(2)=2.4485;
x{1}.effective_index_temperature_sensitivity=matrix(2);
x{1}.effective_index_temperature_sensitivity(1)=0;
x{1}.effective_index_temperature_sensitivity(2)=0; …
```

**另请参阅**

- [parsewaveguidebackannotation](./parsewaveguidebackannotation.md)
