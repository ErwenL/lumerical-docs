<!--
Translation from English documentation
Original command: addtolibrary
Translation date: 2026-02-04 22:49:36
-->

# addtolibrary

添加 该 选中的 元素 到 该 currently 选中的 folder under Custom library. 

**语法** |  **描述**  
---|---  
addtolibrary ("name", replace);  |  添加 一个 元素 到 该 currently 选中的 folder under Custom library.  The "name" specified 是 该 自定义 folder name. If no folder named as specified, 一个 新的 folder 将 为 generated under 该 Custom library.  The "replace" 是 一个 boolean 值. If "replace" 是 true, 该 元素 在 该 Custom library 使用 该 same name 将 为 replaced; 如果 "replace" 是 false, 一个 warning message 将 pop up 到 获取 further action 用于 replacing 该 元素 使用 该 same name 或 not. The default 值 用于 "replace" 是 false.   
  
**Eample**
    
    
    #添加 该 选中的 元素 到 该 folder "folder1" under Custom library
    addtolibrary("folder1", true);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ library ](/hc/en-us/articles/360034927473-library) , [ customlibrary ](/hc/en-us/articles/360034407254-customlibrary)
