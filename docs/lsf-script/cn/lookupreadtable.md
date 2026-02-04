<!--
Translation from English documentation
Original command: lookupreadtable
Translation date: 2026-02-04 22:50:01
-->

# lookupreadtable

返回 一个 interpolated 矩阵 从 一个 文件 containing 一个 lookup table 的 design 和 extracted 参数. 

**语法** |  **描述**  
---|---  
out = lookupreadtable ("文件名","table",design,"extracted");  |  返回 一个 interpolated 矩阵 从 一个 文件 containing 一个 lookup table 的 design 和 extracted 参数. Parameter table 是 该 name 的 该 lookup table located inside 该 文件, design 是 一个 单元格 containing multiple structures 该 define 该 design 参数 到 search, 和 extracted 是 该 name 的 该 参数 到 为 extracted. It 将 返回 一个 矩阵 该 contains multiple columns. The first column 是 该 independent 变量. e.g. 频率 dependent transmission 值.   
  
**示例**

The 脚本 below loads 该 频率 dependent propagation 属性 的 一个 bent waveguide: 
    
    
    文件名 = "waveguide.ixml";
    table = "waveguide";
    design = 单元格(1);
    #design (input 参数)
    design{1} = 结构体;
    design{1}.name = "radius";
    design{1}.值 = 3e-6;
    w_length = 1e-6;
    M=lookupreadtable("waveguide.ixml", "waveguide", design, "Filename" );
    # 设置 该 s-参数 在 scripted 元素
    setsparameter("端口 2", "端口 1", "propagation", M, w_length);
    setsparameter("端口 1", "端口 2", "propagation", M, w_length);

其中 “waveguide.ixml” 是 一个 lookup table containing 一个 map between waveguide ‘radius’ 和 ‘Filename’ containing 频率 dependent propagation 属性: 
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <lumerical_lookup_table version="1.0" name = "waveguide">
      <association> 
        <design>
          <值 name="radius" 类型="double">3e-06</值>
        </design> 
        <extracted>
          <值 name="Filename" 类型="字符串">radius_3.txt</值> 
        </extracted>
      </association>
    </lumerical_lookup_table>

For example, “radius_3.txt” 文件 contains 一个 矩阵 使用 频率 dependent propagation 属性 
    
    
    2.315e+14552.62.787.071e+07
    2.30918e+14552.72.717.076e+07
    2.30335e+14543.32.737.075e+07
    2.29753e+14543.32.767.076e+07
    2.2917e+14544.72.787.062e+07
    2.28588e+14545.52.727.061e+07
    2.28006e+14546.62.717.064e+07
    2.27423e+14544.22.737.061e+07
    2.26841e+14533.12.747.063e+07
    2.26258e+14532.22.757.069e+07 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupread ](/hc/en-us/articles/360034928333-lookupread) , [ lookupwrite ](/hc/en-us/articles/360034928353-lookupwrite) , [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupreadnportsparameter ](/hc/en-us/articles/360034408274-lookupreadnportsparameter) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend) , [ insert ](/hc/en-us/articles/360034928453-insert)
