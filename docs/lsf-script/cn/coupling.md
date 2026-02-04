<!--
Translation from English documentation
Original command: coupling
Translation date: 2026-02-04 22:49:48
-->

# coupling

返回 该 complex coupling coefficient between two modes. The power coupling 可以 为 calculated 使用 该 overlap 函数, 或 通过 该 following formula. 

Power_Coupling = | coupling |  2 

Reference: Allan W. Snyder 和 John D. Love, Optical Waveguide Theory. Chapman & Hall, London, England, 1983. 

See 该 overlap 函数 用于 more details about overlap 和 coupling calculations. 

注意:  coupling  命令 是 deprecated, consider 使用 [ expand ](/hc/en-us/articles/360034926653-expand)  
---  
**语法** |  **描述**  
---|---  
out = coupling(mode2, mode1);  | 

  * mode2, mode1: 该 mode names 
  * out: 该 coupling coefficient 

  
out = coupling(mode2, mode1, x, y);  |  Mode alignment 可以 为 adjusted before coupling 是 calculated. 

  * x offset 
  * y offset 

  
  
**示例**

This example shows 如何 到 use 该 overlap 命令 到 计算 该 overlap 和 power coupling between two modes. 
    
    
    copydcard("mode1","test_mode1");  
    copydcard("mode2","test_mode2");  
    
    out = overlap("test_mode1","test_mode2");  
    
    ?out(1);  # overlap  
    ?out(2);  # power coupling  
    ?coupling("test_mode1","test_mode2"); # 该 complex coupling coefficient  
    ?abs(coupling("test_mode1","test_mode2"))^2; # same as out(2), 该 power coupling

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ expand2 ](/hc/en-us/articles/360034406414-expand2)
