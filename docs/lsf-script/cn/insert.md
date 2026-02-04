<!--
Translation from English documentation
Original command: insert
Translation date: 2026-02-04 22:50:01
-->

# insert

Inserts 一个 对象 into 一个 existing 单元格 在 一个 lookup table. 

**语法** |  **描述**  
---|---  
out{1}.association = insert( out{1}.association, association, 单元格 数字 );  |  Inserts 一个 对象 into 一个 existing 单元格.   
  
**示例**

Loads 该 lookup table "coupler_map.ixml" 和 prints 该 单元格 数组 该 containing all 该 contents 的 该 .ixml 文件 
    
    
    clear;
    tabCoupler = lookupread( "coupler_map.ixml" );
    ?toscript( tabCoupler );

其中 “coupler_map.ixml” 是 一个 lookup table containing 一个 map between coupler 参数 和 different s-参数: 
    
    
    tabCoupler=单元格(1);
    tabCoupler{1}=结构体;
    tabCoupler{1}.association=单元格(1);
    tabCoupler{1}.association{1}=结构体;
    tabCoupler{1}.association{1}.design=单元格(1);
    tabCoupler{1}.association{1}.design{1}=结构体;
    tabCoupler{1}.association{1}.design{1}.name='gap';
    tabCoupler{1}.association{1}.design{1}.值=3.5e-007;
    tabCoupler{1}.association{1}.extracted=单元格(1);
    tabCoupler{1}.association{1}.extracted{1}=结构体;
    tabCoupler{1}.association{1}.extracted{1}.name='coupling_length';
    tabCoupler{1}.association{1}.extracted{1}.值=7.18624e-006;
    tabCoupler{1}.name='coupler_extracted';

The following commands insert  一个  对象 into 该 existing lookup table 
    
    
    association=结构体;
    association.design=单元格(1);
    association.design{1}=结构体;
    association.design{1}.name='gap';
    association.design{1}.值=5e-007;
    association.extracted=单元格(1);
    association.extracted{1}=结构体;
    association.extracted{1}.name='coupling_length';
    association.extracted{1}.值=9e-006;
    # insert association at last position
    tabCoupler{1}.association = insert( tabCoupler{1}.association, association, 2 );
    # print updated 值
    ?toscript(tabCoupler);
    lookupwrite( "coupler_map.ixml", tabCoupler );

now 该 table prints as below: 
    
    
    tabCoupler=单元格(1);
    tabCoupler{1}=结构体;
    tabCoupler{1}.association=单元格(2);
    tabCoupler{1}.association{1}=结构体;
    tabCoupler{1}.association{1}.design=单元格(1);
    tabCoupler{1}.association{1}.design{1}=结构体;
    tabCoupler{1}.association{1}.design{1}.name='gap';
    tabCoupler{1}.association{1}.design{1}.值=3.5e-007;
    tabCoupler{1}.association{1}.extracted=单元格(1);
    tabCoupler{1}.association{1}.extracted{1}=结构体;
    tabCoupler{1}.association{1}.extracted{1}.name='coupling_length';
    tabCoupler{1}.association{1}.extracted{1}.值=7.18624e-006;
    tabCoupler{1}.association{2}=结构体;
    tabCoupler{1}.association{2}.design=单元格(1);
    tabCoupler{1}.association{2}.design{1}=结构体;
    tabCoupler{1}.association{2}.design{1}.name='gap';
    tabCoupler{1}.association{2}.design{1}.值=5e-007;
    tabCoupler{1}.association{2}.extracted=单元格(1);
    tabCoupler{1}.association{2}.extracted{1}=结构体;
    tabCoupler{1}.association{2}.extracted{1}.name='coupling_length';
    tabCoupler{1}.association{2}.extracted{1}.值=9e-006;
    tabCoupler{1}.name='coupler_extracted';

The following commands append 一个 新的 association into 该 existing table: 
    
    
    clear;
    design=单元格(1);
    design{1}=结构体;
    design{1}.name='gap';
    design{1}.值=6e-007;
    # 创建 extracted 参数
    extracted=单元格(1);
    extracted{1}=结构体;
    extracted{1}.name='coupling_length';
    extracted{1}.值=9.9e-006;
    # append 到 existing table
    lookupappend( "coupler_map.ixml", "coupler_extracted", design, extracted );
    # print contents
    ?toscript( lookupread( "coupler_map.ixml" ) );

Now 该 lookup table prints as below: 
    
    
    值=单元格(1);
    值{1}=结构体;
    值{1}.association=单元格(3);
    值{1}.association{1}=结构体;
    值{1}.association{1}.design=单元格(1);
    值{1}.association{1}.design{1}=结构体;
    值{1}.association{1}.design{1}.name='gap';
    值{1}.association{1}.design{1}.值=3.5e-007;
    值{1}.association{1}.extracted=单元格(1);
    值{1}.association{1}.extracted{1}=结构体;
    值{1}.association{1}.extracted{1}.name='coupling_length';
    值{1}.association{1}.extracted{1}.值=7.18624e-006;
    值{1}.association{2}=结构体;
    值{1}.association{2}.design=单元格(1);
    值{1}.association{2}.design{1}=结构体;
    值{1}.association{2}.design{1}.name='gap';
    值{1}.association{2}.design{1}.值=5e-007;
    值{1}.association{2}.extracted=单元格(1);
    值{1}.association{2}.extracted{1}=结构体;
    值{1}.association{2}.extracted{1}.name='coupling_length';
    值{1}.association{2}.extracted{1}.值=9e-006;
    值{1}.association{3}=结构体;
    值{1}.association{3}.design=单元格(1);
    值{1}.association{3}.design{1}=结构体;
    值{1}.association{3}.design{1}.name='gap';
    值{1}.association{3}.design{1}.值=6e-007;
    值{1}.association{3}.extracted=单元格(1);
    值{1}.association{3}.extracted{1}=结构体;
    值{1}.association{3}.extracted{1}.name='coupling_length';
    值{1}.association{3}.extracted{1}.值=9.9e-006;
    值{1}.name='coupler_extracted';

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ lookupopen ](/hc/en-us/articles/360034408254-lookupopen) , [ lookupread ](/hc/en-us/articles/360034928333-lookupread) , [ lookupwrite ](/hc/en-us/articles/360034928353-lookupwrite) , [ lookupclose ](/hc/en-us/articles/360034408234-lookupclose) , [ lookupreadtable ](/hc/en-us/articles/360034928393-lookupreadtable) , [ lookupreadvalue ](/hc/en-us/articles/360034928413-lookupreadvalue) , [ lookupreadnportsparameter ](/hc/en-us/articles/360034408274-lookupreadnportsparameter) , [ lookupappend ](/hc/en-us/articles/360034928433-lookupappend)
