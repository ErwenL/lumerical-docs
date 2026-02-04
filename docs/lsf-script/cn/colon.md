<!--
Translation from English documentation
Original command: colon
Translation date: 2026-02-04 22:49:48
-->

# :

#  : (数组 operator, colon) - Script 命令 

[FDTD](/hc/en-us/articles/360033154434) [MODE](/hc/en-us/articles/360020687354) [DGTD](/hc/en-us/articles/360037744173) [CHARGE](/hc/en-us/articles/360037184494) [HEAT](/hc/en-us/articles/360037224694) [FEEM](/hc/en-us/articles/360037744633) [INTERCONNECT](/hc/en-us/articles/360037304774)

Array operator.

**语法** |  **描述**  
---|---  
x = 2 : 10; |  x 将 为 一个 数组 的 numbers 该 start at 2 和 increase 通过 1 用于 each consecutive 数字. The last entry 将 为 <= 10. x 将 equal 2,3,...,9,10.  
x = 6 : -1.5 : 2; |  x 将 为 该 数组 were 该 first 元素 是 6, 和 consecutive elements decrease 通过 1.5. All elements 将 为 >=2. In 此 example, 该 数组 将 为 [6, 4.5, 3].  
B=A(:, 2) |  B 将 为 该 数组 containing all 该 elements 从 该 second 维度 的 A.  
  
**示例**

创建 一个 向量, 那么 access 一个 portion 的 该 矩阵 在 reverse order 使用 该 : operator.

    一个=l:5;     # 一个 将 为 向量 (1, 2, 3, 4, 5)
    ?b=一个(4:-1:2);  # b 将 为 向量 (4, 3, 2) 

创建 一个 矩阵, 那么 access all 该 元素 的 一个 维度 的 该 矩阵 使用 该 : operator:

    一个=[1,2,3;4,5,6]; 
    ?b=一个(:, 1); # b 将 为 向量 (1, 4)

**参见**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ linspace ](https://optics.ansys.com/hc/en-us/articles/360034409254-linspace)

### Associated files

### Related articles

  * [Lumerical scripting language - By category](/hc/en-us/related/click?数据=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kG--cd6703bb121778897d07c20f1e5febc1b107037d)
  * [Evanescent waveguide couplers](/hc/en-us/related/click?数据=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCLaUMdRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJCL2hjL2VuLXVzL2FydGljbGVzLzM2MDA0MjMwNDY5NC1FdmFuZXNjZW50LXdhdmVndWlkZS1jb3VwbGVycwY7CFQ6CXJhbmtpBw%3D%3D--779e12c8ea10cb7de3cffca73b12de3f447febc4)
  * [NLSE Waveguide (NLSE_WGD) - INTERCONNECT Element](/hc/en-us/related/click?数据=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBODzQg6BzoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJSL2hjL2VuLXVzL2FydGljbGVzLzc5NDU4MzcxODM3NjMtTkxTRS1XYXZlZ3VpZGUtTkxTRS1XR0QtSU5URVJDT05ORUNULUVsZW1lbnQGOwhUOglyYW5raQg%3D--6f1ad30d5bcb2e07d75e8a63bb8a5bb282072e31)
  * [创建 或 modify 环境 variables 在 Windows](/hc/en-us/related/click?数据=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBMQvvAaBzoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJXL2hjL2VuLXVzL2FydGljbGVzLzc4MTIyODk1MzE5MjMtQ3JlYXRlLW9yLW1vZGlmeS1lbnZpcm9ubWVudC12YXJpYWJsZXMtaW4tV2luZG93cwY7CFQ6CXJhbmtpCQ%3D%3D--04f5cc54c68fe273a803e02ae6c4107894396e22)
  * [fitpearson4pdf - Script 命令](/hc/en-us/related/click?数据=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCKUBwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJCL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkyNzAxMy1maXRwZWFyc29uNHBkZi1TY3JpcHQtY29tbWFuZAY7CFQ6CXJhbmtpCg%3D%3D--9b4dc343a7801edf60b14fc6fac4613a7eb28523)

