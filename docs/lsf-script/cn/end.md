<!--
Translation from English documentation
Original command: end
Translation date: 2026-02-03 23:54:53
-->

# end

指定数组的最后一个索引。 

**Syntax** |  **Description**  
---|---  
y=x(3:end);  |  y将是x的子矩阵，从第3个元素到最后一个元素。   
  
 **示例**

创建一个向量，然后访问该矩阵的一部分。
    
    
     a=l:5; #a将是向量(1, 2, 3, 4, 5)
     ?b=a(4:end); #b将是向量(4, 5)

使用'end'从矩阵中检索元素，表示最后一个索引。您可以在任何产生索引的数学表达式中使用'end'。'end'的嵌套使用应该能正常工作。 
    
    
    A = randmatrix(5,4);
     ?A(3:end,2); #等同于A(3:5,2)
     ?A(1:end-2,2); #等同于A(3:5-2,2)
     ?A(end-1:-1:1,2); #等同于A(5-1:-1:1,2)
     ?A(1:end); #等同于A(1:20)和A(:)
    B = [1,0,1,1];
     ?A( sum(B(2:end)):end, 1); #等同于A( sum(B(2:4)):5, 1)
     ?end+4; #错误："上下文错误 - 'end'仅在索引矩阵时可用"

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [linspace](./linspace.md)
- [:](./colon.md)
