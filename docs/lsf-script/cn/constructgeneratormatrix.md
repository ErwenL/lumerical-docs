<!--
Translation from English documentation
Original command: constructgeneratormatrix
Translation date: 2026-02-04 22:49:48
-->

# constructgeneratormatrix

Constructs 一个 symmetric coding generator 矩阵. This 命令 是 especially useful together 使用 该 FEC block. 

**语法** |  **描述**  
---|---  
constructgeneratormatrix(parityin, generatorout, parityout);  |  Constructs 一个 symmetric coding generator 矩阵 ‘generatorout’ 和 该 correspondent parity check 矩阵 ‘parityout’ 从 一个 input parity check 矩阵 ‘parityin’. The input 和 该 generated files 是 AList formatted files.   
**示例**
    
    
    constructgeneratormatrix("hamming_7_4_1_h.alist", "hamming_7_4_1_g.alist", "hamming_7_4_1_h.alist");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834)
