<!--
Translation from English documentation
Original command: islicensestandard
Translation date: 2026-02-03
-->

# islicensestandard

检查许可证是否为标准许可证。

**语法** |  **描述**
---|---
islicensestandard; | 检查 Lumerical 的当前许可证是否为标准许可证。如果是标准许可证则返回 true，否则返回 false。

**示例**

    #Ran on an enterprise license environment
    ?islicensestandard;

    Result:
    False

**相关命令**

- [Ansys optics solve, accelerator, and Ansys HPC license consumption](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)
- [getlicenseestimate](./getlicenseestimate.md)
- [getlicenseestimateallactiveresources](./getlicenseestimateallactiveresources.md)
