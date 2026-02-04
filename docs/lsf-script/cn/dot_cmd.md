<!--
Translation from English documentation
Original command: dot_cmd
Translation date: 2026-02-03 23:45:17
-->

# dot

# dot - 脚本命令

[FDTD](../lumapi/fdtd.md) [MODE](../lumapi/mode.md) [DGTD](../lumapi/dgtd.md) [CHARGE](../lumapi/charge.md) [HEAT](../lumapi/heat.md) [FEEM](../lumapi/feem.md) [INTERCONNECT](../lumapi/interconnect.md)

计算两个矩阵的点积，这两个矩阵必须具有相同数量的元素。矩阵A和B的点积将使用以下公式计算：

$$ C=\sum_iconj(A(i))B(i) $$ 

 **Syntax** |  **Description**  
--- | ---  
C = dot(A, B); | 返回A和B的点积

**示例**

    A = [1,1,0];
    B = [0,1,0];
    ?C = dot(A,B);
    result:
    1
    A = [1,1+1i,0];
    B = [0,1i,0];
    ?C = dot(A,B);
    ?C = conj(A(1))*B(1)+conj(A(2))*B(2)+conj(A(3))*B(3);
    result: 
    1+1i  
    result: 
    1+1i  
    ?dot(B,A);
    result: 
    1-1i  

 **参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [cross](./cross.md)
- [*](./mtimes.md)
- [length](./length.md)
- [size](./size.md)

### 相关文件

### 相关文章

  * [Lumerical scripting language - By category](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kG--5cfad723a60384ca0b56681043d64c73b5da3c79)
  * [Fly’s eye arrays for uniform illumination in digital projector optics](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCJNRG%2FbMJjoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJsL2hjL2VuLXVzL2FydGljbGVzLzQyNjYxNzQ0MTY5MzYzLUZseS1zLWV5ZS1hcnJheXMtZm9yLXVuaWZvcm0taWxsdW1pbmF0aW9uLWluLWRpZ2l0YWwtcHJvamVjdG9yLW9wdGljcwY7CFQ6CXJhbmtpBw%3D%3D--55485abaae8d0f000e88c0e0372984bb90a9d059)
  * [Lumerical Knowledge Base](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCJOqJZR%2BJjoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI%2FL2hjL2VuLXVzL2FydGljbGVzLzQyMzI1MDkzMjMxMjUxLUx1bWVyaWNhbC1Lbm93bGVkZ2UtQmFzZQY7CFQ6CXJhbmtpCA%3D%3D--39b3d06622e98471b87a430f1ea22ecc12d8d7b6)
  * [Multi-Mode Interference (MMI) Coupler](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCKqWMdRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJIL2hjL2VuLXVzL2FydGljbGVzLzM2MDA0MjMwNTE5NC1NdWx0aS1Nb2RlLUludGVyZmVyZW5jZS1NTUktQ291cGxlcgY7CFQ6CXJhbmtpCQ%3D%3D--4d8113d3eef643f6ec5a235ac08771cdd00c2bdc)
  * [rcwasweeppropagation - Script Command](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBPhSFKoBjoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJJL2hjL2VuLXVzL2FydGljbGVzLzczMjAwMDQ3ODAzMDctcmN3YXN3ZWVwcHJvcGFnYXRpb24tU2NyaXB0LUNvbW1hbmQGOwhUOglyYW5raQo%3D--24fa38e13aa45da7e7dc55004216608038e5d04c)

