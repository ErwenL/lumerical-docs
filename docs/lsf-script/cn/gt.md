<!--
Translation from English documentation
Original command: gt
Translation date: 2026-02-03 10:50:31
-->

# >

# >（大于）- 脚本运算符

[FDTD](/hc/en-us/articles/360033154434) [MODE](/hc/en-us/articles/360020687354) [DGTD](/hc/en-us/articles/360037744173) [CHARGE](/hc/en-us/articles/360037184494) [HEAT](/hc/en-us/articles/360037224694) [FEEM](/hc/en-us/articles/360037744633) [INTERCONNECT](/hc/en-us/articles/360037304774)

执行逻辑大于比较。忽略 x 和 y 的虚部。

**语法** |  **描述**  
 ---|---  
 out = y > x;  |  大于。   
 
**示例**

此示例展示 ">" 运算符的用法。

    x=[1+3i, 2+5i];
    y=[0.5+4i, 3+10i];
    ?x>y;
    Warning: prompt line 3: in expression A > B, imaginary parts of A and B are ignored
    result: 
    1  0

**另请参阅**

[ 命令列表 ](/hc/en-us/articles/360037228834) 、[ == ](/hc/en-us/articles/360034930893--) 、[ != ](/hc/en-us/articles/360034930913--) 、[ <= ](/hc/en-us/articles/360034410314--) 、[ >= ](/hc/en-us/articles/360034930933--) 、[ < ](/hc/en-us/articles/360034410334--) 、[ almostequal ](/hc/en-us/articles/360034410294-almostequal) 、[ & ](/hc/en-us/articles/360034930973--) 、[ and ](/hc/en-us/articles/360034410354-and) 、[ | ](/hc/en-us/articles/360034410374--) 、[ or ](/hc/en-us/articles/360034930993-or) 、[ ! ](/hc/en-us/articles/360034931013--) 、[ ~ ](/hc/en-us/articles/360034931033--)

### 关联文件

### 相关文章

  * [>=（大于等于）- 脚本运算符](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCPUQwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCAkRwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJLL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMDkzMy0tZ3JlYXRlci10aGFuLW9yLWVxdWFsLVNjcmlwdC1vcGVyYXRvcgY7CFQ6CXJhbmtpBg%3D%3D--37fbae0815d9e23c1c8d81cbce86f34ed76aaf21)
  * [Lumerical 脚本语言 - 按类别](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCAkRwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kH--5c244f41ab2f3bfa22f7c8b43842f73cc805cf52)
  * [==（等于）- 脚本运算符](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCM0QwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCAkRwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI7L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMDg5My0tZXF1YWwtU2NyaXB0LW9wZXJhdG9yBjsIVDoJcmFua2kI--374515e2b855db9572ee6501fbc70eebf3e09999)
  * [使用 MATLAB 在场图像上叠加矢量图](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCJOSiecBBDoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCAkRwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJaL2hjL2VuLXVzL2FydGljbGVzLzQ0MDYyMjYwMzEyNTEtT3ZlcmxheWluZy12ZWN0b3ItcGxvdC1vdmVyLWZpZWxkLWltYWdlLXVzaW5nLU1BVExBQgY7CFQ6CXJhbmtpCQ%3D%3D--319bb2e1013fba2487728e9537b795e8e5979259)
  * [光子晶体平板（RCWA）](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCBMXnEIEBDoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCAkRwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJAL2hjL2VuLXVzL2FydGljbGVzLzQ0MTYzNDM5MDYwNjctUGhvdG9uaWMtQ3J5c3RhbC1TbGFiLVJDV0EGOwhUOglyYW5raQo%3D--8026c1e6f1c6a5d3abfcbe89e1ba2ee3df13e1a3)

