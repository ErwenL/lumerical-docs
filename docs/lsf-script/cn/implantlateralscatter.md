<!--
Translation from English documentation
Original command: implantlateralscatter
Translation date: 2026-02-04 22:50:00
-->

# implantlateralscatter

计算 该 'lateral scatter' 的 该 doping profile 从 一个 ion implant. The 脚本 命令 takes 该 semiconductor 材料 name, dopant 类型, 和 ion energy as input 参数. 

**语法** |  **描述**  
---|---  
out = implanlateralscatter("dopant", "semiconductor", E)  |  Provides 该 'lateral scatter' 的 该 doping profile 从 一个 ion implant 在 units 的 m. The "dopant" 参数 是 一个 字符串 providing 该 dopant 类型. The options 是 (i) "boron", (ii) "phosphorous", (iii) "antimony", 和 (iv) "arsenic". The "semiconductor" 参数 是 一个 字符串 providing 该 semiconductor 类型. The only available option 是 "silicon". The last 参数 (E) 是 该 ion energy 用于 该 implant 在 units 的 eV.   
  
**示例**

The following 脚本 计算 该 range, straggle, skewness, kurtosis, 和 lateral scatter 用于 一个 ion implant 在 'silicon' 使用 'boron' 用于 一个 ion implant energy 的 1 keV. The 脚本 那么 计算 该 peak concentration 用于 该 1D doping profile (without lateral scatter) 用于 一个 ion dose 的 2e13 /cm  2  和 设置 up 一个 implant doping 对象 在 该 CHARGE 求解器 到 model 该 对应的 doping profile. 
    
    
    E = 1000;  # eV
    dose = 2e13 * 1e4;  # /m^2
    mu = implantrange("boron","silicon",E);  # range 在 m
    si = implantstraggle("boron","silicon",E);  # straggle 在 m
    gal = implantskewness("boron","silicon",E); # skewness
    be2 = implantkurtosis("boron","silicon",E); # kurtosis
    si_lat = implantlateralscatter("boron","silicon",E);  # lateral scatter 在 m
    # 计算 peak doping concentration
    x = linspace(0,mu+10*si,1001);
    y = pearson4pdf(x,mu,si,gal,be2); 
    ion_absorbed = integrate(y,[1],x);  
    peak = max(y)*dose/ion_absorbed;  # peak doping density 在 /m^3
    # 设置 up implant doping 对象 (assume doping 对象 是 already present 在 该 对象 tree)
    select("CHARGE::implant");
    设置("dopant 类型","p");
    设置("peak concentration",peak);
    设置("distribution 函数","pearson4");
    设置("range",mu);
    设置("straggle",si);
    设置("skewness",gal);
    设置("kurtosis",be2);
    设置("lateral scatter",si_lat);

**参见**

[ implantrange ](/hc/en-us/articles/360034406874-implantlateralscatter) , [ implantstraggle ](/hc/en-us/articles/360034406854-implantstraggle) , [ implantkurtosis ](/hc/en-us/articles/360034927053-implantkurtosis) , [ implantskewness ](/hc/en-us/articles/360034927033-implantskewness) , [ fitnormpdf ](/hc/en-us/articles/360034926993-fitnormpdf) , [ fitpearson4pdf ](/hc/en-us/articles/360034927013-fitpearson4pdf) , [ pearson4pdf ](/hc/en-us/articles/360034926693-person4pdf)
