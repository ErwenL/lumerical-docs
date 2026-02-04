<!--
Translation from English documentation
Original command: optimizeposition
Translation date: 2026-02-04 22:50:14
-->

# optimizeposition

The optimizeposition 命令 计算 该 x shift, y shift, 和 z shift resulting 在 maximum overlap between 该 specified mode 和 d-card 当 使用 该 FDE 求解器. 

The x shift, y shift, 和 z shift correspond 到 该 offset 在 该 d-card profile 在 x, y, 和 z. 

This 函数 also populates 该 overlap 和 power coupling as well as 该 x shift, y shift, 和 z shift positions 在 该 Overlap 分析 tab 的 该 Eigensolver Analysis window, similarly 到 当 you click 在 该 "Optimize position" button 在 该 GUI. 

See 该 [ overlap ](/hc/en-us/articles/360034405254-overlap) 函数 用于 more details about overlap 和 coupling calculations. 

**语法** |  **描述**  
---|---  
out = optimizeposition(mode 数字, d-card 数字);  | 

  * mode 数字: 该 mode 数字 在 该 mode list 
  * d-card 数字: 该 数字 的 该 d-card 在 该 deck 

注意 该 该 "shift d-card center" option 必须 为 选中的 在 order 到 use 此 函数.   
  
**示例**

This example shows 如何 到 use 该 optimizeposition 命令 到 计算 该 x shift, y shift, 和 z shift between 一个 specified mode 和 d-card resulting 在 maximum overlap, print out 该 shift 值 和 该 optimal overlap 和 power coupling 使用 该 applied shift. 
    
    
    setanalysis("shift d-card center",1);  
    shift = optimizeposition(4,1); # find x, y, z shift resulting 在 optimal overlap between  
                                   # 该 4th mode 在 该 mode list 和 该 1st mode 在 该 deck  
    
    ?"x shift:"+num2str(shift(1));  
    ?"y shift:"+num2str(shift(2));  
    ?"z shift:"+num2str(shift(3));  
    
    out = overlap("mode4","global_mode1",shift(1),shift(2),shift(3));  
    ?"maximum overlap:"+num2str(out(1));  
    ?"maximum power coupling:"+num2str(out(2));

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ copydcard ](/hc/en-us/articles/360034930233-copydcard) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ coupling ](/hc/en-us/articles/360034925173-coupling) , [ overlap ](/hc/en-us/articles/360034405254-overlap) , [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) , [ propagate ](/hc/en-us/articles/360034925213-propagate) , [ expand ](/hc/en-us/articles/360034926653-expand) , [ setanalysis ](/hc/en-us/articles/360034925113-setanalysis)
