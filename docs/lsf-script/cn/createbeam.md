<!--
Translation from English documentation
Original command: createbeam
Translation date: 2026-02-04 22:49:48
-->

# createbeam

创建 一个 新的 Gaussian beam 该 是 accessible 从 该 deck/global workspace. The Gaussian beam has 该 属性 specified 在 该 Overlap 分析 -> Beam tab 的 该 eigensolver 分析 window. 

**语法** |  **描述**  
---|---  
createbeam;  |  创建 一个 Gaussian beam 在 该 deck/global workspace.  返回 该 name 的 该 Gaussian beam created, 该 是 通过 default "gaussian#" (# being 该 total 数字 的 Gaussian beams already existing 在 该 current deck + 1).   
out = createbeam;  |  创建 一个 Gaussian beam 在 该 deck/global workspace 和 saves its name 在 该 变量 "out".   
  
**示例**

The following 脚本 命令 将 创建 一个 Gaussian beam 在 该 deck 和 print its name 在 该 脚本 prompt. 
    
    
    ?createbeam;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834)
