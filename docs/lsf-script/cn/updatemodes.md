<!--
Translation from English documentation
Original command: updatemodes
Translation date: 2026-02-04 22:50:15
-->

# updatemodes

Updates 该 mode profile(s) 的 选中的 mode expansion 监视器 If there 是 no mode profiles stored 在 该 mode expansion 监视器, 那么 该 mode 使用 该 highest effective index 将 为 选中的. If mode profiles 是 already stored 在 该 mode expansion 监视器, 那么 该 modes 使用 该 best overlap 使用 该 old modes 将 为 选中的. 注意 该 该 mode expansion 监视器 必须 为 选中的 before running 此 命令.

**语法** |  **描述**  
---|---  
updatemodes; |  Updates mode profile 的 该 选中的 mode expansion 监视器.  返回 1 如果 该 update was successful 和 -1 如果 not.  
updatemodes(mode_number); |  Updates 该 mode expansion 监视器 和 selects 该 desired mode numbers. For example, updatemodes(1:10); 将 计算 该 10 modes 使用 该 highest refractive index. Please note 该 making 此 call 将 force 一个 recalculation 的 一个 modes, even 如果 该 same modes have previously been calculated. In addition, making 此 call 将 force 该 mode selection method 到 become "用户 select". This optional 参数 was introduced 在 FDTD 8.6.3 和 MODE 6.5.3.  
  
NOTE: Saving 仿真 files before 使用 updatesourcemode If you have 一个 脚本 文件 该 updates 该 仿真 mesh, 那么 you 应该 use 该 [save 脚本 命令](/hc/en-us/articles/360034410814-save) before updating 该 源 mode. This 将 ensure 该 该 mesh has been updated before 该 新的 mode 是 calculated.  
---  
  
NOTE: overlap The fraction 的 electromagnetic fields 该 overlap between 该 two modes 是 given 通过 该 expression below. It 是 also 该 fraction 的 power 从 mode2 该 可以 propagate 在 mode1. For more information, please see [overlap 脚本 命令](/hc/en-us/articles/360034405254-overlap).  $$ \text { overlap }=\operatorname{Re}\left[\frac{\left(\int \vec{E}_{1} \times \vec{H}_{2}^{*} \cdot d \vec{S}\right)\left(\int \vec{E}_{2} \times \vec{H}_{1}^{*} \cdot d \vec{S}\right)}{\int \vec{E}_{1} \times \vec{H}_{1}^{*} \cdot d \vec{S}}\right] \frac{1}{\operatorname{Re}\left(\int \vec{E}_{2} \times \vec{H}_{2}^{*} \cdot d \vec{S}\right)} $$  
---  
  
**示例**

See 该 example 在 该 [addmodeexpansion](/hc/en-us/articles/360034924573-addmodeexpansion) 脚本 函数

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [addmode](/hc/en-us/articles/360034924353-addmode), [addmodeexpansion](/hc/en-us/articles/360034924573-addmodeexpansion), [clearsourcedata](/hc/en-us/articles/360034929093-clearsourcedata), [clearmodedata](/hc/en-us/articles/360034408774-clearmodedata), [getresult](/hc/en-us/articles/360034409854-getresult), [overlap](/hc/en-us/articles/360034405254-overlap), [expand](/hc/en-us/articles/360034926653-expand), [seteigensolver](/hc/en-us/articles/360034929113-seteigensolver), [geteigensolver](/hc/en-us/articles/360034408794-geteigensolver), [updatesourcemode](/hc/en-us/articles/360034408754-updatesourcemode)
