<!-- Translation completed: 2026-02-04 -->
<!-- Original command: constructgeneratormatrix -->

# constructgeneratormatrix

**语法** | **描述**
---|---
constructgeneratormatrix(parityin, generatorout, parityout); | Constructs a symmetric coding generator 矩阵 ‘generatorout’ and the correspondent parity check 矩阵 ‘parityout’ from a 输入 parity check 矩阵 ‘parityin’. The 输入 and the generated files are AList formatted files.

**示例**

    constructgeneratormatrix("hamming_7_4_1_h.alist", "hamming_7_4_1_g.alist", "hamming_7_4_1_h.alist");

    constructgeneratormatrix("hamming_7_4_1_h.alist", "hamming_7_4_1_g.alist", "hamming_7_4_1_h.alist");

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834)
