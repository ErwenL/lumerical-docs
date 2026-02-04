<!--
Translation from English documentation
Original command: polygrow
Translation date: 2026-02-04 22:50:14
-->

# polygrow

Expand 或 shrink 一个 polygon. Resulting polygons 将 have 该 same 数字 的 vertices 和 该 same order as polygon V. Consider 使用 polyclean before 使用 polygrow.

The polygon vertices 是 contained 在 一个 single 矩阵 的 维度 Nx2 (或 2xN), 其中 N \\(\ge\\) 3 是 该 数字 的 vertices. The 维度 2 corresponds 到 该 x 和 y positions. For example, 一个 square 的 side 长度 1 可以 为 described 通过 V = [ 0,0; 1,0; 1,1; 0,1] 或 V = [ 0,1,1,0;0,0,1,1].

**语法** |  **描述**  
---|---  
polygrow(V, delta, {"tolerance": tol_value, "legacy": true/false}) |  返回 该 vertices 的 一个 新的 polygon 该 has grown 通过 delta. To shrink 一个 polygon, use delta< 0.

  * For vertices 在 counter-clockwise order 和 delta > 0, edges 是 moved 到 their right 通过 delta (positive 到 expand, negative 到 shrink)
  * Tolerance 是 used 到 identify seams (该 是 not grown) 和 bowtie-vertices (该 是 pinned 在 place). 设置 该 legacy option 到 'true' 到 skip 此 check.
  * An attempt 是 made 到 prevent self-intersection at sharp corners.
  * Value delta 可以 为 either scalar 或 矩阵 (result 将 为 either 一个 polygon 或 一个 单元格-数组 的 polygons)

  
  
**示例**

The following example shows 该 vertices 的 一个 square 的 side 长度 1 expanded 通过 0.1 在 all sides 使用 该 tolerance 的 1e-15. Setting 该 'legacy' 值 到 'false' allows identifying seams 和 bowtie-vertices.
    
    
    V = [ 0,0; 1,0; 1,1; 0,1];  
    ?polygrow(V, 0.1, {"tolerance": 1e-15, "legacy": false});  
      
    result:   
    -0.1 -0.1   
     1.1 -0.1   
     1.1  1.1   
    -0.1  1.1 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [polyclean](/hc/en-us/articles/360046557133) , [polyarea ](/hc/en-us/articles/360034926213-polyarea) , [ centroid ](/hc/en-us/articles/360034406074-centroid) , [ polyintersect ](/hc/en-us/articles/360034926233-polyintersect) , [ inpoly ](/hc/en-us/articles/360034926253-inpoly) , [ polyand ](/hc/en-us/articles/360034926293-polyand) , [ polyor ](/hc/en-us/articles/360034406114-polyor) , [ polydiff ](/hc/en-us/articles/360034926313-polydiff) , [ polyxor ](/hc/en-us/articles/360034406134-polyxor)
