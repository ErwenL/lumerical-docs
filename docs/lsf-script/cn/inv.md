<!--
Translation from English documentation
Original command: inv
Translation date: 2026-02-03
-->

# inv

计算矩阵的逆矩阵。该矩阵必须是可逆的。

**语法** |  **描述**
---|---
out = inv(A) |  返回矩阵 A 的逆。
out = inv(A, tol); |  返回矩阵 A 的 Moore-Penrose 伪逆，容差为 "tol"。

**示例**

反转矩阵并乘以原始矩阵以获得单位矩阵。

    A= [ 1, 2; 3, 4];
    B= inv(A);
    ?mult(B,A);  # This should return the identity matrix
    result:
    1 0
    0 1

推导同一矩阵的 Moore-Penrose 伪逆，容差为 0.1。

    ?C = inv(A, 0.1);
    result:
    0.0426428 0.0963963
    0.0605104 0.136787

**相关命令**

- [List of commands](./List-of-commands.md)
- [=](./Equal.md)
- [==](./EqualEqual.md)
- [!=](./NotEqual.md)
- [<=](./LessEqual.md)
- [>=](./GreaterEqual.md)
- [<](./LessThan.md)
- [>](./GreaterThan.md)
- [&](./Ampersand.md)
- [and](./and.md)
- [|](./Pipe.md)
- [or](./or.md)
- [!](./Exclamation.md)
- [~](./Tilde.md)
- [eig](./eig.md)
- [mult](./mult.md)
- [solve](./solve.md)
