<!--
Translation from English documentation
Original command: saveelement
Translation date: 2026-02-04 22:50:14
-->

# saveelement

Saves 一个 元素 到 一个 .ice 文件 在 该 current working directory. 

**语法** |  **描述**  
---|---  
saveelement ("name");  |  Save 一个 元素 到 一个 文件. The 元素 将 为 saved 使用 该 current 元素 name 在 该 current working directory 使用 extension ICE.   
  
**示例**
    
    
    #添加 一个 元素 star coupler 和 saves it 到 一个 .ice 文件 在 该 current working directory
    addelement("Star Coupler");
    saveelement("STAR_1");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ library ](/hc/en-us/articles/360034927473-library) , [ addtolibrary ](/hc/en-us/articles/360034407234-addtolibrary) , [ probe ](/hc/en-us/articles/360034407294-probe) , [ loadelement ](/hc/en-us/articles/360034407274-loadelement)
