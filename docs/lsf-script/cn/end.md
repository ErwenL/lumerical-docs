<!--
Translation from English documentation
Original command: end
Translation date: 2026-02-04 22:49:48
-->

# end

Specifies 该 last index 的 一个 数组. 

**语法** |  **描述**  
---|---  
y=x(3:end);  |  y 将 为 该 submatrix 的 x, 从 该 3rd 元素 到 该 last 元素.   
  
**示例**

创建 一个 向量, 那么 access 一个 portion 的 该 矩阵. 
    
    
    一个=l:5;     # 一个 将 为 向量 (1, 2, 3, 4, 5)
    ?b=一个(4:end);  # b 将 为 向量 (4, 5) 

Retrieve elements 从 matrices 使用 'end' 到 mean last index. You 可能 use 'end' 在 any mathematical expression 该 results 在 indexing. Nested use 的 'end' 应该 work properly. 
    
    
    A = randmatrix(5,4);
    ?A(3:end,2);      # equivalent 到 A(3:5,2)
    ?A(1:end-2,2);    # equivalent 到 A(3:5-2,2)
    ?A(end-1:-1:1,2); # equivalent 到 A(5-1:-1:1,2)
    ?A(1:end);        # equivalent 到 A(1:20) 和 A(:)
    B = [1,0,1,1];
    ?A( sum(B(2:end)):end, 1);  # equivalent 到 A( sum(B(2:4)):5, 1)
    ?end+4;           # error: "context error - 'end' 可能 only 为 used 当 indexing 一个 矩阵"

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ linspace ](/hc/en-us/articles/360034409254-linspace) , [ : ](/hc/en-us/articles/360034929533--) . 
