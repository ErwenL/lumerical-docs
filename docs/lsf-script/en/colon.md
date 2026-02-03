# :

#  : (array operator, colon) - Script command 

[FDTD](/hc/en-us/articles/360033154434) [MODE](/hc/en-us/articles/360020687354) [DGTD](/hc/en-us/articles/360037744173) [CHARGE](/hc/en-us/articles/360037184494) [HEAT](/hc/en-us/articles/360037224694) [FEEM](/hc/en-us/articles/360037744633) [INTERCONNECT](/hc/en-us/articles/360037304774)

Array operator.

**Syntax** |  **Description**  
---|---  
x = 2 : 10; |  x will be an array of numbers that start at 2 and increase by 1 for each consecutive number. The last entry will be <= 10. x will equal 2,3,...,9,10.  
x = 6 : -1.5 : 2; |  x will be the array were the first element is 6, and consecutive elements decrease by 1.5. All elements will be >=2. In this example, the array will be [6, 4.5, 3].  
B=A(:, 2) |  B will be the array containing all the elements from the second dimension of A.  
  
**Examples**

Create a vector, then access a portion of that matrix in reverse order with the : operator.

    a=l:5;     # a will be vector (1, 2, 3, 4, 5)
    ?b=a(4:-1:2);  # b will be vector (4, 3, 2) 

Create a matrix, then access all the element of a dimension of that matrix with the : operator:

    a=[1,2,3;4,5,6]; 
    ?b=a(:, 1); # b will be vector (1, 4)

**See Also**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ linspace ](https://optics.ansys.com/hc/en-us/articles/360034409254-linspace)

### Associated files

### Related articles

  * [Lumerical scripting language - By category](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kG--cd6703bb121778897d07c20f1e5febc1b107037d)
  * [Evanescent waveguide couplers](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCLaUMdRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJCL2hjL2VuLXVzL2FydGljbGVzLzM2MDA0MjMwNDY5NC1FdmFuZXNjZW50LXdhdmVndWlkZS1jb3VwbGVycwY7CFQ6CXJhbmtpBw%3D%3D--779e12c8ea10cb7de3cffca73b12de3f447febc4)
  * [NLSE Waveguide (NLSE_WGD) - INTERCONNECT Element](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBODzQg6BzoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJSL2hjL2VuLXVzL2FydGljbGVzLzc5NDU4MzcxODM3NjMtTkxTRS1XYXZlZ3VpZGUtTkxTRS1XR0QtSU5URVJDT05ORUNULUVsZW1lbnQGOwhUOglyYW5raQg%3D--6f1ad30d5bcb2e07d75e8a63bb8a5bb282072e31)
  * [Create or modify environment variables in Windows](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBMQvvAaBzoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJXL2hjL2VuLXVzL2FydGljbGVzLzc4MTIyODk1MzE5MjMtQ3JlYXRlLW9yLW1vZGlmeS1lbnZpcm9ubWVudC12YXJpYWJsZXMtaW4tV2luZG93cwY7CFQ6CXJhbmtpCQ%3D%3D--04f5cc54c68fe273a803e02ae6c4107894396e22)
  * [fitpearson4pdf - Script command](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCKUBwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCH0LwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJCL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkyNzAxMy1maXRwZWFyc29uNHBkZi1TY3JpcHQtY29tbWFuZAY7CFQ6CXJhbmtpCg%3D%3D--9b4dc343a7801edf60b14fc6fac4613a7eb28523)

