<!--
Translation from English documentation
Original command: gte
Translation date: 2026-02-03 10:52:36
-->

# >=

# >=（大于等于）- 脚本运算符

[FDTD](/hc/en-us/articles/360033154434) [MODE](/hc/en-us/articles/360020687354) [DGTD](/hc/en-us/articles/360037744173) [CHARGE](/hc/en-us/articles/360037184494) [HEAT](/hc/en-us/articles/360037224694) [FEEM](/hc/en-us/articles/360037744633) [INTERCONNECT](/hc/en-us/articles/360037304774)

执行逻辑大于等于比较。忽略 x 和 y 的虚部。

**语法** |  **描述**  
 ---|---  
 out = y >= x; |  大于等于。
  
**示例**

此示例展示 ">=" 运算符的用法。

    x=[1+3i, 2+5i];
    y=[0.5+4i, 3+10i];
    ?x>=y;
    Warning: prompt line 3: in expression A >= B, imaginary parts of A and B are ignored
    result: 
    1  0

**另请参阅**

[ 命令列表 ](/hc/en-us/articles/360037228834) 、[ == ](/hc/en-us/articles/360034930893--) 、[ != ](/hc/en-us/articles/360034930913--) 、[ <= ](/hc/en-us/articles/360034410314--) 、[ almostequal ](/hc/en-us/articles/360034410294-almostequal) 、[ < ](/hc/en-us/articles/360034410334--) 、[ > ](/hc/en-us/articles/360034930953--) 、[ & ](/hc/en-us/articles/360034930973--) 、[ and ](/hc/en-us/articles/360034410354-and) 、[ | ](/hc/en-us/articles/360034410374--) 、[ or ](/hc/en-us/articles/360034930993-or) 、[ ! ](/hc/en-us/articles/360034931013--) 、[ ~ ](/hc/en-us/articles/360034931033--)

### 关联文件

### 相关文章

  * [Lumerical scripting language - By category](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCCIh5NNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJNL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzIyODgzNC1MdW1lcmljYWwtc2NyaXB0aW5nLWxhbmd1YWdlLUJ5LWNhdGVnb3J5BjsIVDoJcmFua2kG--e6f7b1b6f9e5e6b360145e1c4e9cbb22f84330ae)
  * [if - Script command](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCGYXudNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI2L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDQwODI5NC1pZi1TY3JpcHQtY29tbWFuZAY7CFQ6CXJhbmtpBw%3D%3D--3116bc4c2e2dd76184f43e4e8528e3c262353487)
  * [== (equal) - Script operator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCM0QwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI7L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMDg5My0tZXF1YWwtU2NyaXB0LW9wZXJhdG9yBjsIVDoJcmFua2kI--e425291d199fd4438fbd02dc68b80f006c53a4d3)
  * [> (greater than) - Script operator](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCAkRwdNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJCL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkzMDk1My0tZ3JlYXRlci10aGFuLVNjcmlwdC1vcGVyYXRvcgY7CFQ6CXJhbmtpCQ%3D%3D--a6b460ee3fb8776caa860ff6d46654a69660b48c)
  * [Waveguide crossing](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCDElOdRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCPUQwdNTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSI3L2hjL2VuLXVzL2FydGljbGVzLzM2MDA0MjgwMDQzMy1XYXZlZ3VpZGUtY3Jvc3NpbmcGOwhUOglyYW5raQo%3D--2e4b2524f120a7d55d142538ab68f03e9bfd76d4)

