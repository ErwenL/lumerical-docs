<!-- Translation completed: 2026-02-04 -->
<!-- Original command: bestoverlap2 -->

# bestoverlap2

**语法** | **描述**
---|---
out = bestoverlap2("test_mode"); | 计算 the best overlap.
out = bestoverlap2("test_mode", x,y,z); | 计算 the best overlap.

**示例**

This 示例 will 计算 which of the current 模式 have the best overlap with the D-CARD named "test_mode". The effective index of the best 模式 is then returned. 
    mode_name = bestoverlap2("test_mode");  
    neff = getdata(mode_name,"neff");

This 示例 will 计算 which of the current 模式 have the best overlap with the D-CARD named "test_mode". The effective index of the best 模式 is then returned. 
    mode_name = bestoverlap2("test_mode");  
    neff = getdata(mode_name,"neff");

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ expand2 ](/hc/en-us/articles/360034406414-expand2) , [ Polarization converter example ](**%20to%20be%20defined%20**) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap)
