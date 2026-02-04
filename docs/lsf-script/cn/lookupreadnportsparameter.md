<!--
Translation from English documentation
Original command: lookupreadnportsparameter
Translation date: 2026-02-04 22:50:01
-->

# lookupreadnportsparameter

Returns an interpolated s-parameter cell for specific design parameters from an [xml file containing a lookup table of design](https://optics.ansys.com/hc/en-us/articles/360034416634-INTERCONNECT-XML-lookup-tables-for-element-data).

The xml file should have a lookup table associating s-parameter data files with design parameters. Each s-parameter file associated by the table should be compatible with the [Optical N Port S-Parameter element](https://optics.ansys.com/hc/en-us/articles/360036107914-Optical-N-Port-S-Parameter-SPAR-INTERCONNECT-Element), in the exact same format, and should not contain any header.

**语法** |  **描述**  
---|---  
out = lookupreadnportsparameter ("文件名","table",design,"extracted"); |  返回 一个 interpolated s-参数 单元格 从 一个 xml 文件 containing 一个 lookup table 的 design:

  * 文件名: Name 的 该 xml 文件.
  * table: Name 的 该 lookup table located inside 该 xml 文件.
  * design: Cell containing multiple structures defining 该 target design 到 extract.
  * extracted: Name 的 该 参数 inside 该 lookup table 该 holds names 的 该 s-参数 数据 文件 用于 each design.

  
out = lookupreadnportsparameter ("文件名","table",design,"extracted", opt); |  返回 一个 interpolated s-参数 单元格 从 一个 xml 文件 containing 一个 lookup table 的 design 使用 interpolation options 在 该 结构 opt:

  * 文件名: Name 的 该 xml 文件.
  * table: Name 的 该 lookup table located inside 该 xml 文件.
  * design: Cell containing multiple structures defining 该 target design 到 extract.
  * extracted: Name 的 该 参数 inside 该 lookup table 该 holds names 的 该 s-参数 数据 文件 用于 each design.
  * opt: Structure setting interpolation options. The 结构 fields 是 described 在 该 table below.

  
  
The option 结构 has 该 following fields, 该 spelling 的 each field 是 case-sensitive.

**Field** |  **描述**  
---|---  
method |  The method used 用于 interpolation. The following options 是 supported:

  * spline: Spline interpolation method, 此 是 该 default method.
  * Geodesic: Geodesic interpolation method 该 ensures smooth transitions. When geodesic interpolation 是 选中的, 一个 similarity check 是 performed 在 original 数据 points near 该 interpolated point used 用于 该 interpolation, 如果 这些 points 是 not sufficiently similar, 该 数据 是 coarse, 和 一个 warning 是 displayed. This method cannot 为 used 用于 extrapolation.

  
passivity |  Whether passivity 是 enforced 用于 该 s-参数 数据 prior 到 interpolation. This field only affects results 当 “geodesic” 是 选中的 as 该 interpolation method. When 数据 是 non-passive, 一个 warning message 是 always displayed 用于 geodesic interpolation. The following options 是 supported:

  * enforce: Ensures S-矩阵 是 passive 通过 making sure 该 该 induced 2-norm 的 该 s-参数 是 less than 1. This 是 该 default method.
  * ignore: Ignores passivity 的 该 s-参数 和 interpolates as-是.

  
  
**Note** : For more information on how passivity is enforced, see this [Knowledge Base](https://optics.ansys.com/hc/en-us/articles/360059772393-S-parameter-passive-workflow-guide#toc_4) article.

**示例**

Loads 该 s-参数 的 一个 coupler depending 在 用户定义 design 参数 设置 up target 用于 interpolation:
    
    
    文件名 = "coupler.ixml";
    table = "coupler";
    radius = 3e-06;
    gap = 3e-07;
    design = 单元格(2);
    #design (input 参数)
    design{1} = 结构体;
    design{1}.name = "radius";
    design{1}.值 = radius;
    design{2} = 结构体;
    design{2}.name = "gap";
    design{2}.值 = gap; 

Interpolate 参数 和 load into S-参数 单元格 数组 使用 spline interpolation
    
    
    ?M = lookupreadnportsparameter( 文件名, table, design, "out_filename" ); 

Interpolate 参数 和 load into S-参数 单元格 数组 使用 geodesic interpolation, ignoring passivity 的 该 元素
    
    
    ?M = lookupreadnportsparameter( 文件名, table, design, "out_filename", {"method":"geodesic","passivity":"ignore" ); 

设置 参数 到 元素
    
    
    addelement("Optical N Port S-Parameter");  
    setvalue('SPAR_1','s 参数',M);

“coupler.ixml” 是 一个 lookup table containing 一个 map between coupler 参数 和 different s-参数:
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <lumerical_lookup_table version="1.0" name = "coupler">
      <association>
        <design>
          <值 name="radius" 类型="double">3e-06</值>
          <值 name="gap" 类型="double">3e-07</值>
        </design>
        <extracted>
          <值 name="out_filename" 类型="字符串">radius_3_gap_3.txt</值>
        </extracted>
      </association>
    </lumerical_lookup_table>
    

For example “radius_3_gap_3.txt” 文件 contains s-参数 用于 该 ‘Optical N Port S-Parameter’ 元素
    
    
    ("端口 1","TE",1,"端口 1",1,"transmission")
    (3,3)
     2.262580000000e+014 1.034036580296e-002 -2.629253819969e+000
     2.275690000000e+014 9.716591457652e-003 -2.734774978072e+000
     2.288790000000e+014 6.884340821788e-003 -2.838683842048e+000
    ("端口 1","TE",1,"端口 2",1,"transmission")
    (3,3)
     2.262580000000e+014 9.847090174703e-001 1.376105202083e-001
     2.275690000000e+014 9.959778891317e-001 1.450376288706e-001
     2.288790000000e+014 1.002869828593e+000 1.483183421805e-001

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupread ](/hc/en-us/articles/360034928333-lookupread) , [ lookupwrite ](/hc/en-us/articles/360034928353-lookupwrite) , [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) , [ lookupreadtable ](/hc/en-us/articles/360034928393-lookupreadtable) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend) , [ insert ](/hc/en-us/articles/360034928453-insert)
