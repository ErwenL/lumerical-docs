<!--
Translation from English documentation
Original command: selectmode
Translation date: 2026-02-04 22:50:14
-->

# selectmode

Selects 一个 mode 从 该 mode list. All modes found 在 一个 仿真 是 numbered based 在 their effective index 和 they 是 displayed 在 该 mode list 在 该 Eigensolver 分析 window.

**语法** |  **描述**  
---|---  
selectmode(N); |  Select 该 Nth mode 从 该 mode list.  
selectmode([N]); |  Select mode(s) 从 一个 scalar 矩阵 参数; multiple modes 可以 为 选中的 通过 listing multiple elements 在 [N], e.g., [1,2,3].  
selectmode(name); |  Selects 该 desired mode 其中 name 是 一个 字符串 containing 该 name 的 一个 mode. Modes 是 named mode1, mode2, ..modeN. This form 的 该 命令 是 compatible 使用 该 [ bestoverlap ](/hc/en-us/articles/360034405274-bestoverlap) 函数.  
  
**示例**

Both 这些 commands select 该 third mode 在 该 list:
    
    
    selectmode(3);selectmode("mode3");

Selects 该 3rd, 5th, 和 6th modes.
    
    
    selectmode([3,5,6]);
    

Selects 该 modes 2 through 5, 和 8.
    
    
    selectmode([[2:5];8]);
    

This 命令 selects 该 mode 该 has 该 best overlap 使用 该 D-card named "reference"
    
    
    selectmode(bestoverlap("reference"));

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ setanalysis ](/hc/en-us/articles/360034925113-setanalysis) , [ mesh ](/hc/en-us/articles/360034410654-mesh) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ frequencysweep](/hc/en-us/articles/360034925153-frequencysweep) , [bestoverlap](/hc/en-us/articles/360034405274)
