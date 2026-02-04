<!--
Translation from English documentation
Original command: getsweepdata
Translation date: 2026-02-04 22:50:00
-->

# getsweepdata

获取 raw 数据 从 一个 参数 sweep/optimization/Monte Carlo 分析. In most cases, it 是 more convenient 到 获取 一个 complete dataset 使用  getsweepresult  , rather than getting individual 数据 elements 使用  getsweepdata  . 

**语法** |  **描述**  
---|---  
?getsweepdata;  |  返回 names 的 all sweep, optimization, 和 Monte Carlo 分析 对象.   
?getsweepdata("sweep_name");  |  返回 all 该 names 的 该 available 数据 该 是 stored 在 该 sweep, optimization, 或 Monte Carlo 分析 对象.   
out = getsweepdata("sweep_name", "数据");  |  返回 参数 sweep, optimization, 或 Monte Carlo 分析 数据.  The following 数据 可以 为 obtained 从 一个 optimization: 

  * fomTrend - Figure 的 merit as 一个 函数 的 generation 
  * fomHistory - Figure 的 merit history (用于 each generation there 将 为 generation size 数字) 
  * bestFom - Best figure 的 merit obtained during sweep 
  * bestParameter - Parameter 该 corresponds 到 bestFom 
  * paramHistory - Parameter history 

For 一个 参数 sweep 和 Monte Carlo 分析, 此 命令 返回 both 参数 和 results.   
  
**示例**

This example shows 如何 到 获取 数据 从 一个 参数 sweep. Please download 该 example 文件 从 该 [ Parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps) page Associate files. 
    
    
    m="thickness_sweep";
    ?getsweepdata(m);
    th = getsweepdata(m,"thickness"); # 获取 参数 从 sweep
    R = getsweepdata(m,"R");# 获取 result 从 sweep
    plot(th*1e6,R,"thickness (微米)","Reflection");
    > R
    > T
    > thickness 

This example shows 如何 到 access 数据 从 一个 optimization. 
    
    
    m="thickness_optimization";
    ?getsweepdata(m);
    genVec = getsweepdata(m,"genVec");       # Generation 向量 (1D 向量, Ng)
    memberVec = getsweepdata(m,"memberVec");    # Generation member 向量 (1D 向量, Nm)
    fomTrend = getsweepdata(m,"fomTrend");     # Best 的 each generation, same as shown 在 Opt. GUI window (1D 向量, Ng)
    paramsTrend = getsweepdata(m,"paramsTrend");  # Parameters 对应的 到 FOM trend (3D 矩阵, 1 x Np x Ng)
    bestFom = getsweepdata(m,"bestFom");      # Global best FOM
    bestParams = getsweepdata(m,"bestParams");   # Parameters 对应的 到 global best FOM (1D 向量, Np)
    fomHistory = getsweepdata(m,"fomHistory");   # Every FOM calculated 在 optimization (2D maxtrix, Nm x Ng)
    paramHistory = getsweepdata(m,"paramHistory"); # Every 参数 设置 used 在 optimization (3D maxtrix, Np x Nm x Ng)
    plot(genVec,fomTrend,"generation 数字","fom Trend","best FOM 的 each generation"); 
    ?"Best FOM: "+num2str(bestFom);
    ?"Best Params: "+num2str(bestParams);
    ?"Total 数字 的 simulations run: "+num2str(长度(genVec)*长度(memberVec));
    image(memberVec,genVec,fomHistory,"member","generation","All FOM's obtained");
    > genVec
    > memberVec
    > paramsTrend
    > fomTrend
    > paramHistory
    > fomHistory
    > bestParams
    > bestFom
    > Best FOM: 0.00187328
    > Best Params: 5.96041e-008
    > Total 数字 的 simulations run: 50

**参见**

[ getdata ](/hc/en-us/articles/360034409834-getdata) , [ runsweep ](/hc/en-us/articles/360034931413-runsweep) , [ havesweepdata ](/hc/en-us/articles/360034409934-havesweepdata) , [ savedata ](/hc/en-us/articles/360034411174-savedata) , [ getsweepresult ](/hc/en-us/articles/360034409814-getsweepresult) , [ savesweep ](/hc/en-us/articles/360034410014-savesweep) , [ loadsweep ](/hc/en-us/articles/360034409994-loadsweep)
