<!--
Translation from English documentation
Original command: getnamednumber
Translation date: 2026-02-04 22:50:00
-->

# getnamednumber

获取 该 数字 的 对象 使用 一个 given name. 

**语法** |  **描述**  
---|---  
out = getnamednumber( "name");  |  The same as getnumber, but acts 在 对象 使用 一个 specific name, instead 的 选中的 对象.   
out = getnamednumber( "groupname::name");  |  The same as getnumber, but acts 在 all 对象 named "name" 在 该 group "groupname", instead 的 选中的 对象.   
  
**示例**

添加 2 微米 到 该 radius 的 all 选中的 对象 named circle. 
    
    
    用于 (i=1:getnamednumber("circle")) {
     rad=getnamed("circle","radius",i);
     setnamed("circle","radius",rad+2e-6,i);
    }

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ 获取 ](/hc/en-us/articles/360034928873-获取) , [ getnamed ](/hc/en-us/articles/360034408574-getnamed) , [ getnumber ](/hc/en-us/articles/360034928913-getnumber) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ setnamed ](/hc/en-us/articles/360034928793-setnamed)
