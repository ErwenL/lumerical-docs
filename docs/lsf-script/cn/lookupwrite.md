<!--
Translation from English documentation
Original command: lookupwrite
Translation date: 2026-02-04 22:50:13
-->

# lookupwrite

Writes 到 一个 lookup table 文件 使用 一个 design 和 一个 extracted 参数 pair. This 函数 必须 为 called after [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) 和 before [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) . 

**语法** |  **描述**  
---|---  
out = lookupwrite ("文件名","table",design, "extracted");  |  Writes 到 一个 lookup table 使用 一个 design 和 一个 extracted 参数 pair. The design 和 extracted 参数 是 cells 该 contain multiple structures, allowing 用于 mapping between multiple design 和 extracted 参数. This 函数 可以 为 called multiple times, 用于 each call 该 design 和 extracted 参数 将 为 appended 到 该 current 文件. This 函数 必须 为 called after  lookupopen  和 before  lookupclose  .   
out = lookupwrite ("文件名");  |  Takes 一个 脚本 对象, 在 此 case 一个 单元格 数组 containing all 该 contents 的 该 xml 文件, 和 save it 到 一个 文件.   
  
**示例**

The 脚本 below maps two 值 的 waveguide width 和 height 到 该 effective index 和 group index. 
    
    
    design = 单元格(2);
    #extracted contains neff 和 ng
    extracted = 单元格(2);
    #design (input 参数)
    design{1} = 结构体;
    design{1}.name = "width";
    design{1}.值 = 5.03333e-07;
    design{2} = 结构体;
    design{2}.name = "heigth";
    design{2}.值 = 2.18889e-07;
    #extracted (output results)
    extracted{1} = 结构体;
    extracted{1}.name = "neff";
    extracted{1}.值 = 2.1;
    extracted{2} = 结构体;
    extracted{2}.name = "ng";
    extracted{2}.值 = 4.42;
    #open 文件 到 write table
    lookupopen( "新的.xml", "new_extracted" );
    #write first design/extracted pair
    lookupwrite( "新的.xml", design, extracted );
    #second design/extracted pair
    design{1}.值 = 6.03333e-07;
    design{2}.值 = 1.18889e-07;
    extracted{1}.值 = 2.2;
    extracted{2}.值 = 4.45;
    #write second design/extracted pair
    lookupwrite( "新的.xml", design, extracted );
    #close 文件
    lookupclose( "新的.xml" );

其中 “新的.xml” 是 一个 lookup table containing 该 table “new_extracted” 
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <lumerical_lookup_table version="1.0" name = "new_extracted">
    <association>
      <design>
        <值 name="width" 类型="double">5.03333e-07</值>
        <值 name="heigth" 类型="double">2.18889e-07</值>
      <design>
      <extracted>
        <值 name="neff" 类型="double">2.1</值>
        <值 name="ng" 类型="double">4.42</值>
      </extracted>
    </association>
    <association>  
      <design>
        <值 name="width" 类型="double">6.03333e-07</值>
        <值 name="heigth" 类型="double">1.18889e-07</值>
      <design>
      <extracted>
        <值 name="neff" 类型="double">2.2</值>
        <值 name="ng" 类型="double">4.45</值>
      </extracted>
    </association>
    </lumerical_lookup_table>

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupread ](/hc/en-us/articles/360034928333-lookupread) , [ lookupreadtable ](/hc/en-us/articles/360034928393-lookupreadtable) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupreadnportsparameter ](/hc/en-us/articles/360034408274-lookupreadnportsparameter) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend) , [ insert ](/hc/en-us/articles/360034928453-insert)
