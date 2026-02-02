# dot

#  dot - Script command 

[FDTD](/hc/en-us/articles/360033154434) [MODE](/hc/en-us/articles/360020687354) [DGTD](/hc/en-us/articles/360037744173) [CHARGE](/hc/en-us/articles/360037184494) [HEAT](/hc/en-us/articles/360037224694) [FEEM](/hc/en-us/articles/360037744633) [INTERCONNECT](/hc/en-us/articles/360037304774)

Calculates the dot product of two matrices, which must have the same number of elements. The dot product of matrices A and B will be computed with the following formula: 

$$ C=\sum_iconj(A(i))B(i) $$ 

**Syntax** |  **Description**  
---|---  
C = dot(A, B);  |  Returns the dot product of A and B   
  
**Example**

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

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ cross ](/hc/en-us/articles/360034405734-cross) , [ * ](/hc/en-us/articles/360034930833--) , [ length ](/hc/en-us/articles/360034925653-length) , [ size ](/hc/en-us/articles/360034405654-size)

### Associated files

### Related articles

  * [Lumerical scripting language - By category](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kG--5cfad723a60384ca0b56681043d64c73b5da3c79)
  * [Fly’s eye arrays for uniform illumination in digital projector optics](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCJNRG%2FbMJjoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJsL2hjL2VuLXVzL2FydGljbGVzLzQyNjYxNzQ0MTY5MzYzLUZseS1zLWV5ZS1hcnJheXMtZm9yLXVuaWZvcm0taWxsdW1pbmF0aW9uLWluLWRpZ2l0YWwtcHJvamVjdG9yLW9wdGljcwY7CFQ6CXJhbmtpBw%3D%3D--55485abaae8d0f000e88c0e0372984bb90a9d059)
  * [Lumerical Knowledge Base](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCJOqJZR%2BJjoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI%2FL2hjL2VuLXVzL2FydGljbGVzLzQyMzI1MDkzMjMxMjUxLUx1bWVyaWNhbC1Lbm93bGVkZ2UtQmFzZQY7CFQ6CXJhbmtpCA%3D%3D--39b3d06622e98471b87a430f1ea22ecc12d8d7b6)
  * [Multi-Mode Interference (MMI) Coupler](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCKqWMdRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJIL2hjL2VuLXVzL2FydGljbGVzLzM2MDA0MjMwNTE5NC1NdWx0aS1Nb2RlLUludGVyZmVyZW5jZS1NTUktQ291cGxlcgY7CFQ6CXJhbmtpCQ%3D%3D--4d8113d3eef643f6ec5a235ac08771cdd00c2bdc)
  * [rcwasweeppropagation - Script Command](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBPhSFKoBjoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCM38wNNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJJL2hjL2VuLXVzL2FydGljbGVzLzczMjAwMDQ3ODAzMDctcmN3YXN3ZWVwcHJvcGFnYXRpb24tU2NyaXB0LUNvbW1hbmQGOwhUOglyYW5raQo%3D--24fa38e13aa45da7e7dc55004216608038e5d04c)

