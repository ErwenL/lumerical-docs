<!--
Translation from English documentation
Original command: dipolepower
Translation date: 2026-02-03 23:05:45
-->

# dipolepower

返回偶极子源注入仿真区域的功率。在3D仿真中，如果使用cwnorm，单位为瓦特；如果使用nonorm，单位为瓦特/赫兹²。

dipolepower脚本命令返回注入仿真区域的功率，相当于测量从偶极子周围小盒子透射出的功率。相比之下，[sourcepower](/hc/en-us/articles/360034925313-sourcepower)将返回偶极子在均匀材料中辐射的功率。对于均匀介质中的偶极子，dipolepower和sourcepower是等效的。

高级说明：

  * 如果偶极子位于色散介质中（折射率的虚部非零），则此函数的结果不可靠。在这种情况下，建议在偶极子周围使用监视器盒子。
  * 当使用非常小的仿真网格尺寸时，此计算中的数值误差可能会变得明显。如果网格步长小于或等于λ/1000，建议通过测量偶极子周围小盒子中的辐射功率来验证dipolepower结果。



如果您在色散介质中使用偶极子，请访问[支持中心](https://www.lumerical.com/support/)获取更多帮助。

**Syntax** |  **Description**  
---|---  
out = dipolepower(f); |  返回偶极子源在频率点f处辐射的功率。（f单位为Hz）  
out = dipolepower(f, name); |  此选项允许您获取单个偶极子辐射的功率，而不是所有偶极子的总和。此选项仅在包含多个偶极子的仿真中需要。  
  
 **示例**

 请参阅[偶极子-辐射功率](/hc/en-us/articles/360034382794-Sources-Dipoles)页面和[荧光增强](https://apps.lumerical.com/fluorescence-enhancement.html)应用示例。

 **参见**

- [sourcenorm](./sourcenorm.md)
- [sourcepower](./sourcepower.md)
- [sourcepower_avg](./sourcepower_avg.md)
- [sourcepower_pavg](./sourcepower_pavg.md)
- [transmission](./transmission.md)
- [cwnorm](./cwnorm.md)
- [nonorm](./nonorm.md)
