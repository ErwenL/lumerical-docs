# >=

# >= (greater than or equal) - Script operator

[FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
[MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
[DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
[CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
[HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
[FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
[INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)

Performs a logical greater-than-or-equal-to comparison. Imaginary components of x and y
are ignored.

| **Syntax**    | **Description**           |
| ------------- | ------------------------- |
| out = y >= x; | Greater than or equal to. |

**Examples**

This example shows the usage of the ">=" operator.

```
x=[1+3i, 2+5i];
y=[0.5+4i, 3+10i];
?x>=y;
Warning: prompt line 3: in expression A >= B, imaginary parts of A and B are ignored
result: 
1  0  
```

**See Also**

[ List of commands](../lsf-script-commands-alphabetical.md), [ ==](./minus.md),
[ !=](./minus.md), [\<=](./minus.md), [almostequal](./almostequal.md), [\<](./minus.md),
[>](./minus.md), [&](./minus.md), [and](./and.md), [|](./minus.md), [or](./or.md),
[!](./minus.md), [~](./minus.md)

### Associated files

### Related articles

- [Lumerical scripting language - By category](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kG--e6f7b1b6f9e5e6b360145e1c4e9cbb22f84330ae)
- [if - Script command](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCGYXudNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI2L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDQwODI5NC1pZi1TY3JpcHQtY29tbWFuZAY7CFQ6CXJhbmtpBw%3D%3D--3116bc4c2e2dd76184f43e4e8528e3c262353487)
- [== (equal) - Script operator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCM0QwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI7L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMDg5My0tZXF1YWwtU2NyaXB0LW9wZXJhdG9yBjsIVDoJcmFua2kI--e425291d199fd4438fbd02dc68b80f006c53a4d3)
- [> (greater than) - Script operator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCAkRwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJCL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMDk1My0tZ3JlYXRlci10aGFuLVNjcmlwdC1vcGVyYXRvcgY7CFQ6CXJhbmtpCQ%3D%3D--a6b460ee3fb8776caa860ff6d46654a69660b48c)
- [Waveguide crossing](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCDElOdRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI3L2hjL2VuLXVzL2FydGljbGVzLzM2MDA0MjgwMDQzMy1XYXZlZ3VpZGUtY3Jvc3NpbmcGOwhUOglyYW5raQo%3D--2e4b2524f120a7d55d142538ab68f03e9bfd76d4)
