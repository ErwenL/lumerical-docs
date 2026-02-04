<!--
Translation from English documentation
Original command: addproperty
Translation date: 2026-02-04 22:49:29
-->

# addproperty

The 脚本 命令 添加 一个 属性 到 一个 compound 或 到 一个 scripted 元素.

**语法** |  **描述**  
---|---  
addproperty(name, 属性=”new_property”, category=””, 类型=”Number”, 从=0, 到=0, kind=”FixedUnit”, unit=””, default_value = "") |  添加 一个 新的 属性 到 一个 Scripted 元素 或 一个 Compound 元素 使用 该 following options:

  * name: 元素 name.
  * 属性: 属性 name.
  * category: defines 该 folder 当 该 属性 将 为 stored 在 该 属性 view window.
  * 类型: defines 该 属性 类型. Can 为 chosen 从 ["Number", "String", "Logical", "Matrix", "ComboChoice", "FileSave", "FileOpen"], please refer 到 该 details below.
  * 从, 到: defines 该 range 用于 一个 "Number" 类型 的 属性.
  * kind: defines 该 属性 kind. Can 为 chosen 从 ["Angle", "Area", "Bandwidth", "Bitrate", "Capacitance", "Current", "Density", "Dimensionless", "Dispersion", "DispersionSlope", "Distance", "DopingDensity", "Energy", "EngineeringScale", "FixedUnit", "Frequency", "Gain", "GainCoefficient", "Inductance", "InverseDistance", "InverseVolume", "Loss", "LossCoefficient", "ModeDispersion", "NonQuantity", "Power", "PowerSpectralDensity", "Resistance", "Temperature", "Time", "Velocity", "Voltage", "Volume", "WaveguideLoss"]; 用于 该 unit 的 all 该 kinds, please refer 到 该 details below.
  * unit: defines 该 unit 的 该 属性.
  * default_value: defines 该 default 值 的 该 属性. Can 为 一个 矩阵 或 一个 字符串. If no default 值 是 provided, 该 minimum range 值 将 为 used 到 initialize 该 属性.

  
  
类型:

  * Number, String, Logical
  * Matrix: 语法 用于 属性 值 [a11, a12, a13; a21 ,a22, a23]
  * ComboChoice: 创建 一个 属性 使用 options 到 choose 从. 语法 用于 属性 值: 'choice_1;choice_2:choice_3'
  * FileSave: Allows 一个 用户 到 save 一个 文件. 语法 用于 属性 值: 字符串 使用 文件 path.
  * FileOpen: Allows 一个 用户 到 open 一个 文件. 语法 用于 属性 值: 字符串 使用 文件 path.



kind:

  * Frequency, Distance, Loss, etc: 'Unit' options 是 updated accordingly.
  * FixedUnit: 'Unit' 可以 为 chosen 从 pre-defined units 或 可以 为 用户定义.
  * NonQuantity: 'Unit' 是 blank (unitless). Recommended 用于 all types expect "Number".



**示例**

添加 属性 “new_property” 到 一个 existing compound 元素 ‘COMPOUND_1’
    
    
    addproperty("COMPOUND_1");

添加 属性 “width” 到 一个 existing compound 元素 ‘COMPOUND_1’
    
    
    addproperty("COMPOUND_1","width");

添加 属性 “gain” 到 一个 existing compound 元素 ‘COMPOUND_1’, place it 在 category ‘Standard’
    
    
    addproperty("COMPOUND_1","gain","Standard");

添加 “temperature” 属性 到 一个 existing compound 元素 ‘COMPOUND_1’, place it 在 ‘Thermal’ category, 设置 its 类型, range 和 unit.
    
    
    addproperty("COMPOUND_1","temperature","Thermal","Number",0,100,"Temperature","C");

**参见**

[Manipulating objects](/hc/en-us/articles/360037228834), [autoarrange](https://support.lumerical.com/hc/en-us/articles/360034409034-autoarrange), [setexpression](https://support.lumerical.com/hc/en-us/articles/360034409094-setexpression), [createcompound](https://support.lumerical.com/hc/en-us/articles/360034409054-createcompound)
