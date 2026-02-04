<!--
Translation from English documentation
Original command: bestoverlap2
Translation date: 2026-02-04 22:49:36
-->

# bestoverlap2

This 函数 是 similar 到 [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) but it uses [ expand2 ](/hc/en-us/articles/360034406414-expand2) 到 获取 该 necessary 参数, 该 可以 为 useful 当 一个 evanescent mode 是 involved. 

**语法** |  **描述**  
---|---  
out = bestoverlap2("test_mode");  |  计算 该 best overlap. 

  * out: 一个 字符串 containing 该 name 的 该 mode 使用 该 best overlap 
  * test_mode: 一个 字符串 containing 该 name 的 一个 D-CARD mode 

  
out = bestoverlap2("test_mode", x,y,z);  |  计算 该 best overlap. 

  * out: 一个 字符串 containing 该 name 的 该 mode 使用 该 best overlap 
  * test_mode: 一个 字符串 containing 该 name 的 一个 D-CARD mode 

Mode alignment 可以 为 adjusted before best overlap 是 calculated. 

  * x offset 
  * y offset 
  * z offset 

The offset 是 applied 到 该 test_mode.   
  
**示例**

This example 将 计算 该 的 该 current modes have 该 best overlap 使用 该 D-CARD named "test_mode". The effective index 的 该 best mode 是 那么 returned. 
    
    
    mode_name = bestoverlap2("test_mode");  
    neff = getdata(mode_name,"neff");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ expand2 ](/hc/en-us/articles/360034406414-expand2) , [ Polarization converter example ](**%20to%20be%20defined%20**) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap)
