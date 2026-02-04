<!--
Translation from English documentation
Original command: updatesourcemode
Translation date: 2026-02-04 22:50:15
-->

# updatesourcemode

Updates 该 mode profile 的 选中的 mode 源. If there 是 no mode profile stored 在 该 源, 那么 该 mode 使用 该 highest effective index 将 为 选中的. If 一个 mode 是 already stored 在 该 源, 那么 该 mode 使用 该 best overlap 使用 该 old mode 将 为 选中的. 注意 该 该 mode 源 必须 为 选中的 before running 此 命令.

**语法** |  **描述**  
---|---  
?updatesourcemode; |  Updates mode profile 的 该 选中的 Mode 源. 返回 该 fraction 的 electromagnetic fields 该 overlap between 该 old 和 该 新的 mode  
?updatesourcemode(mode_number); |  Updates 该 mode 源 和 selects 该 desired mode 数字. For example, updatesourcemode(1); 将 计算 该 fundamental mode. Please note 该 making 此 call 将 force 一个 recalculation 的 一个 mode, even 如果 该 same mode has previously been calculated. In addition, making 此 call 将 force 该 mode selection method 到 become "用户 select". This optional 参数 was introduced 在 FDTD 8.6.3 和 MODE 6.5.3.  
NOTE: Saving 仿真 files before 使用 updatesourcemode If you have 一个 脚本 文件 该 updates 该 仿真 mesh, 那么 you 应该 use 该 [save 脚本 命令](/hc/en-us/articles/360034410814-save) before updating 该 源 mode. This 将 ensure 该 该 mesh has been updated before 该 新的 mode 是 calculated.  
---  
NOTE: overlap The fraction 的 electromagnetic fields 该 overlap between 该 two modes 是 given 通过 该 expression below. It 是 also 该 fraction 的 power 从 mode2 该 可以 propagate 在 mode1. For more information, please see [overlap 脚本 命令](/hc/en-us/articles/360034405254-overlap). $$ \text { overlap }=\operatorname{Re}\left[\frac{\left(\int \vec{E}_{1} \times \vec{H}_{2}^{*} \cdot d \vec{S}\right)\left(\int \vec{E}_{2} \times \vec{H}_{1}^{*} \cdot d \vec{S}\right)}{\int \vec{E}_{1} \times \vec{H}_{1}^{*} \cdot d \vec{S}}\right] \frac{1}{\operatorname{Re}\left(\int \vec{E}_{2} \times \vec{H}_{2}^{*} \cdot d \vec{S}\right)} $$  
---  
  
**示例**

Select 该 源, 那么 update 该 mode profile. Once 该 mode profile has been updated, output 该 mode effective index 和 visualize 该 mode field profile.
    
    
    # update 该 源 mode profile  
    select("源");  
    updatesourcemode;  
    
    # 获取 该 mode profile 和 effective index  
    n=getresult("源","neff");  
    ?"Effective index = " + num2str(n.neff);  
    field=getresult("源","mode profiles");  
      
    visualize(field);

**参见**

[Manipulating 对象](/hc/en-us/articles/360037228834), [addmode](/hc/en-us/articles/360034924353-addmode), [clearsourcedata](/hc/en-us/articles/360034929093-clearsourcedata), [clearmodedata](/hc/en-us/articles/360034408774-clearmodedata), [getresult](/hc/en-us/articles/360034409854-getresult), [overlap](/hc/en-us/articles/360034405254-overlap), [expand](/hc/en-us/articles/360034926653-expand), [seteigensolver](/hc/en-us/articles/360034929113-seteigensolver), [geteigensolver](/hc/en-us/articles/360034408794-geteigensolver), [updatemode](/hc/en-us/articles/360034929073-updatemodes), [updateportmodes](/hc/en-us/articles/360034409174-updateportmodes)
