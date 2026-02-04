<!--
Translation from English documentation
Original command: bestoverlap
Translation date: 2026-02-04 22:49:36
-->

# bestoverlap

Finds 该 mode 使用 highest (best) overlap between 该 specified D-CARD 和 该 currently calculated modes 在 该 mode list. 返回 该 name 的 该 mode 使用 该 best overlap. This 函数 是 used 用于 tracking 该 desired mode during 参数 sweeps 使用 该 FDE 求解器. 

See 该 [ overlap ](/hc/en-us/articles/360034405254-overlap) 函数 用于 more details about overlap 和 coupling calculations. 

**语法** |  **描述**  
---|---  
out = bestoverlap("test_mode");  |  计算 该 best overlap. 

  * out: 一个 字符串 containing 该 name 的 该 mode 使用 该 best overlap 
  * test_mode: 一个 字符串 containing 该 name 的 一个 D-CARD mode 

  
  
**示例**

This example 将 计算 该 的 该 current modes have 该 best overlap 使用 该 D-CARD named "test_mode". The effective index 的 该 best mode 是 那么 returned. 
    
    
    mode_name = bestoverlap("test_mode");  
    neff = getdata(mode_name,"neff");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ expand2 ](/hc/en-us/articles/360034406414-expand2) , [ bestoverlap2 ](/hc/en-us/articles/360034925193-bestoverlap2) , [ Polarization converter example ](**%20to%20be%20defined%20**)
