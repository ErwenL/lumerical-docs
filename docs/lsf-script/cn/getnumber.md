<!--
Translation from English documentation
Original command: getnumber
Translation date: 2026-02-04 22:50:00
-->

# getnumber

获取 该 数字 的 对象 该 是 选中的. 

**语法** |  **描述**  
---|---  
out = getnumber;  |  返回 该 数字 的 对象 该 是 选中的;   
  
**示例**

添加 2 微米 到 该 radius 的 all 对象 named "circle". 
    
    
    select("circle");
    用于 (i=1:getnumber) {
     rad=获取("radius",i);
     设置("radius",rad+2e-6,i);
    }

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ 获取 ](/hc/en-us/articles/360034928873-获取) , [ getnamed ](/hc/en-us/articles/360034408574-getnamed) , [ getnamednumber ](/hc/en-us/articles/360034408594-getnamednumber) , [ 设置 ](/hc/en-us/articles/360034928773-设置)
