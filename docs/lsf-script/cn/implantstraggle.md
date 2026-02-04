<!--
Translation from English documentation
Original command: implantstraggle
Translation date: 2026-02-03
-->

# implantstraggle

计算离子注入的 1D 掺杂分布的"离散"。脚本命令接受半导体材料名称、掺杂类型和离子能量作为输入参数。

**语法** | **描述**
---|---
out = implantstraggle("dopant", "semiconductor", E) | 提供离子注入的 1D 掺杂分布的"离散"，单位为 m。"dopant" 参数是提供掺杂类型的字符串。选项为：(i) "boron"，(ii) "phosphorous"，(iii) "antimony"，和 (iv) "arsenic"。"semiconductor" 参数是提供半导体类型的字符串。唯一可用的选项是 "silicon"。最后一个参数 (E) 是注入的离子能量，单位为 eV。

**示例**

以下脚本计算在 1 keV 离子注入能量下，'silicon' 中 'boron' 离子注入的范围、离散、偏度、峰度和横向离散。然后脚本计算离子剂量为 2e13 /cm² 的 1D 掺杂分布的峰值浓度，并在 CHARGE 求解器中设置注入掺杂对象以模拟相应的掺杂分布。

    E = 1000;  # eV
    dose = 2e13 * 1e4;  # /m^2
    mu = implantrange("boron","silicon",E);  # range in m
    si = implantstraggle("boron","silicon",E);  # straggle in m
    gal = implantskewness("boron","silicon",E); # skewness
    be2 = implantkurtosis("boron","silicon",E); # kurtosis
    si_lat = implantlateralscatter("boron","silicon",E);  # lateral scatter in m
    # calculate peak doping concentration
    x = linspace(0,mu+10*si,1001);
    y = pearson4pdf(x,mu,si,gal,be2);
    ion_absorbed = integrate(y,[1],x);
    peak = max(y)*dose/ion_absorbed;  # peak doping density in /m^3
    # set up implant doping object (assume doping object is already present in the objects tree)
    select("CHARGE::implant");
    set("dopant type","p");
    set("peak concentration",peak);
    set("distribution function","pearson4");
    set("range",mu);
    set("straggle",si);
    set("skewness",gal);
    set("kurtosis",be2);
    set("lateral scatter",si_lat);

**相关命令**

- [implantrange](./implantrange.md)
- [implantkurtosis](./implantkurtosis.md)
- [implantskewness](./implantskewness.md)
- [implantlateralscatter](./implantlateralscatter.md)
- [fitnormpdf](./fitnormpdf.md)
- [fitpearson4pdf](./fitpearson4pdf.md)
- [pearson4pdf](./pearson4pdf.md)
