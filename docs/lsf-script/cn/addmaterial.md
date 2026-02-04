<!--
Translation from English documentation
Original command: addmaterial
Translation date: 2026-02-04 22:49:29
-->

# addmaterial

添加 一个 新的 材料 到 该 材料 database given 该 材料 model 或 类型 和 返回 该 name 的 该 新的 材料. For details 在 available 材料 models see: [ Material permittivity models ](/hc/en-us/articles/360034394634-Material-Permittivity-Models) 和 [ Material conductivity models ](/hc/en-us/articles/360034915113-Material-Conductivity-Models) . 

**语法** |  **描述**  
---|---  
?addmaterial;  |  Lists all available 材料 models 该 可以 为 added into 该 材料 database.   
out = addmaterial("materialtype");  |  添加 一个 新的 材料 和 返回 该 name 的 该 新的 材料. The 参数 "materialtype" has 到 match correct 字符串 exactly.   
  
**示例**

These commands 添加 一个 新的 Conductive 材料, 设置 该 name 到 "aluminum", anisotropy 到 "Diagonal", 和 设置 该 permittivity as well as conductivity 属性 用于 该 材料. 
    
    
    A=[4;5;6];
    B=[1;2;3];
    mymaterial = addmaterial("Conductive");
    setmaterial(mymaterial,"name","Aluminum");
    setmaterial("Aluminum", "Anisotropy", 1); # 启用 diagonal anisotropy
    setmaterial("Aluminum","Permittivity", A);
    setmaterial("Aluminum","Conductivity", B);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ deletematerial ](/hc/en-us/articles/360034409734-deletematerial) , [ copymaterial ](/hc/en-us/articles/360034930033-copymaterial) , [ setmaterial ](/hc/en-us/articles/360034409654-setmaterial) , [ getmaterial ](/hc/en-us/articles/360034930053-getmaterial)
