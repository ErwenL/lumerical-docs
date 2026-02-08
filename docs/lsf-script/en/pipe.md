# |

# | (or) - Script operator

[FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
[MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
[DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
[CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
[HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
[FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
[INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)

Is the logical OR function. Imaginary components of x and y are ignored.

| **Syntax** | **Description** |
| ---------- | --------------- |
| out = y    | x;              |
| y or x;    | Same as         |

**Examples**

This example shows the usage of the "|" and OR function.

```
? (2) | (4);
result: 
1 
?(3 > 4) or (4 >3);
result: 
1  
? (0+1i) | (0);
result: 
0 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ == ](./minus.md) ,
[ != ](./minus.md) , [ \<= ](./minus.md) , [ >= ](./minus.md) , [ < ](./minus.md) ,
[ > ](./minus.md) , [ & ](./minus.md) , [ and ](./and.md) , [ | ](./minus.md) ,
[ or ](./or.md) , [ ! ](./minus.md) , [ ~ ](./minus.md)

### Associated files

### Related articles

- [& (and) - Script operator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCB0RwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCIYfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI5L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMDk3My0tYW5kLVNjcmlwdC1vcGVyYXRvcgY7CFQ6CXJhbmtpBg%3D%3D--d98b7ebe9579cd949f1f5f0926c8e41497a2b9e4)
- [~ (not) - Script operator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCFkRwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCIYfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI5L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMTAzMy0tbm90LVNjcmlwdC1vcGVyYXRvcgY7CFQ6CXJhbmtpBw%3D%3D--9f8e60d55d1be11eb0dfc8396130bd5229fca637)
- [or - Script operator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCDERwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCIYfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI3L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMDk5My1vci1TY3JpcHQtb3BlcmF0b3IGOwhUOglyYW5raQg%3D--27c0a174c8957a21ccbc5a822ad029923f08d752)
- [Lumerical scripting language - By category](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCIYfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kJ--f7f269168c21ffac58bbff57b1c9987d10cdbb34)
- [and - Script operator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCHIfudNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCIYfudNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI4L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDQxMDM1NC1hbmQtU2NyaXB0LW9wZXJhdG9yBjsIVDoJcmFua2kK--8e67c797b064ee84fc66688669a6addc3301c448)
