<!--
Translation from English documentation
Original command: getsweepresult
Translation date: 2026-02-04 22:50:00
-->

# getsweepresult

获取 该 参数 sweep/optimization/Monte Carlo/S-参数 sweep results 在 该 form 的 一个 dataset.

**语法** |  **描述**  
---|---  
?getsweepresult; |  返回 names 的 all sweep, optimization, Monte Carlo, 和 S-参数 sweep 对象 使用 available results.  
?getsweepresult("sweep_name"); |  返回 names 的 该 available results 从 该 specified sweep, optimization,Monte Carlo, 或 S-参数 sweep task.  
out = getsweepresult("sweep_name", "result"); |  返回 该 specified result dataset 从 该 specified 参数 sweep, optimization, Monte Carlo, 或 S-参数 sweep task.  
  
**示例**

This example shows 如何 到 获取 数据 从 一个 参数 sweep. Please download 该 example 文件 从 该 [ Parameter sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps) page Associate files.
    
    
    ?getsweepresult("thickness_sweep");
    ?R = getsweepresult("thickness_sweep","R");
    image(R.lambda*1e6,R.thickness*1e6,R.T,"波长 (um)","thickness (um)","reflection");
    > R
    > T
    > thickness
    > T vs lambda/f, thickness

This following commands show 如何 到 access optimization results:

First, see 该 available 数据.
    
    
    m="thickness_optimization";
    ?getsweepresult(m);
    > fom trend
    > best fom
    > 参数 trend
    > best 参数
    > fom history
    > 参数 history
    > genVec
    > memberVec
    > paramsTrend
    > fomTrend
    > paramHistory
    > fomHistory
    > bestParams
    > bestFom

Following 是 该 description 的 each available result:
    
    
    Available datasets
    fom trend :     Best result per generation. This 是 该 quantity shown 在 该 Optimization GUI window (1D 向量, Ng)  
    best fom :      Global best FOM. (Single 值, not dataset) 
    参数 trend :  Parameters 对应的 到 FOM trend (3D 矩阵, 1 x Np x Ng)
    best 参数 :  Parameters 对应的 到 global best FOM (1D 向量, Np)
    fom history :    Every FOM calculated 在 optimization (2D maxtrix, Nm x Ng)
    参数 history : Every 参数 设置 used 在 optimization (3D maxtrix, Np x Nm x Ng)
    Available raw 数据. The following quantities 是 simply 该 simple 矩阵 versions 的 该 above results
    genVec :       Generation 向量 (1D 向量, Ng)
    memberVec :     Generation member 向量 (1D 向量, Nm)
    paramsTrend :    Parameters 对应的 到 FOM trend (3D 矩阵, 1 x Np x Ng)
    fomTrend :      Best result per generation. This 是 该 quantity shown 在 该 Optimization GUI window
    paramHistory :    Every 参数 设置 used 在 optimization (3D maxtrix, Np x Nm x Ng)
    fomHistory :     Every FOM calculated 在 optimization (2D maxtrix, Nm x Ng)
    bestParams :     Parameters 对应的 到 global best FOM (1D 向量, Np)
    bestFom :      Global best FOM (Single 值)

获取 该 global best Figure 的 merit
    
    
    # 获取 该 best FOM
    ?getsweepresult("thickness_optimization","best fom");
    > result: 
    0.00187328

Plot 该 Figure 的 merit trend
    
    
    FOMtrend = getsweepresult("thickness_optimization","fom trend");
    plot(FOMtrend.generation,FOMtrend.fom);

The following 脚本 是 一个 excerpt 从 该 example 脚本 从 [ S-参数 矩阵 sweep ](/hc/en-us/articles/360034403214-S-参数-矩阵-sweep) showing 如何 到 collect 该 results 从 一个 S-参数 sweep.
    
    
    # collect results
    S_matrix = getsweepresult("s-参数 sweep","S 矩阵");
    S_parameters = getsweepresult("s-参数 sweep","S 参数");
    S_diagnostic = getsweepresult("s-参数 sweep","S diagnostic");

**参见**

[ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) , [ runsweep ](/hc/en-us/articles/360034931413-runsweep) , [ havesweepresult ](/hc/en-us/articles/360034409954-havesweepresult) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ savedata ](/hc/en-us/articles/360034411174-savedata) , [ getsweepdata ](/hc/en-us/articles/360034409794-getsweepdata) , [ savesweep ](/hc/en-us/articles/360034410014-savesweep) , [ loadsweep ](/hc/en-us/articles/360034409994-loadsweep)
