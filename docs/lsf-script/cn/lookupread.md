<!--
Translation from English documentation
Original command: lookupread
Translation date: 2026-02-04 22:50:01
-->

# lookupread

Finds 该 nearest extracted 值 从 一个 文件 containing 一个 lookup table 的 design 和 extracted 参数. 

**语法** |  **描述**  
---|---  
out = lookupread ("文件名","table",design,"extracted");  |  Finds 该 nearest extracted 值 从 一个 文件 containing 一个 lookup table 的 design 和 extracted 参数. Parameter table 是 该 name 的 该 lookup table located inside 该 文件, design 是 一个 单元格 containing multiple structures 该 define 该 design 参数 到 search, 和 extracted 是 该 name 的 该 参数 到 为 extracted. It 将 返回 该 值 located at 该 nearest design 参数.   
out = lookupread ("文件名");  |  返回 一个 脚本 对象, 在 此 case 一个 单元格 数组 containing all 该 contents 的 该 xml 文件.   
  
**示例**

To load 该 coupling 长度 index associated 到 一个 coupler gap: 
    
    
    #design 单元格 containing design/layout 参数 (input 参数 到 search)#“gap” 是 该 name 的 该 属性 在 该 文件  
    
    w_gap=3.5e-07;
    design = 单元格(1);
    design{1} = 结构体;
    design{1}.name = "gap";
    design{1}.值 = w_gap;
    #read coupling 长度 从 文件 (使用 design as input search “coupling_length”)
    cl=lookupread( "coupler_map.xml", "coupler_extracted", design, "coupling_length" );
    ?c1
    7.18624026618721e-06

其中 “coupler_map.xml” 是 一个 lookup table containing 一个 map between coupler gap 和 coupling 长度 值: 
    
    
    ?xml version="1.0" encoding="UTF-8"?
    <lumerical_lookup_table version="1.0" name = "coupler_extracted">
      <association>
        <design>
          <值 name="gap" 类型="double">3.5e-07</值>
        </design>
        <extracted>
          <值 name="coupling_length" 类型="double">7.18624026618721e-06</值> 
        </extracted> 
      </association>
    ...
    </lumerical_lookup_table>
    

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupwrite ](/hc/en-us/articles/360034928353-lookupwrite) , [ lookupreadtable ](/hc/en-us/articles/360034928393-lookupreadtable) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupreadnportsparameter ](/hc/en-us/articles/360034408274-lookupreadnportsparameter) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend) , [ insert ](/hc/en-us/articles/360034928453-insert)
