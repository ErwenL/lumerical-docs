<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getsweepresult -->

# getsweepresult

    ?getsweepresult("thickness_optimization","best fom");
    > result: 
    0.00187328
Plot the Figure of merit trend
    FOMtrend = getsweepresult("thickness_optimization","fom trend");
    plot(FOMtrend.generation,FOMtrend.fom);
The following 脚本 is an excerpt from the 示例 脚本 from [ S-参数 矩阵 sweep ](/hc/en-us/articles/360034403214-S-参数-矩阵-sweep) showing how to collect the results from an S-参数 sweep.
    S_matrix = getsweepresult("s-参数 sweep","S 矩阵");
    S_parameters = getsweepresult("s-参数 sweep","S parameters");
    S_diagnostic = getsweepresult("s-参数 sweep","S diagnostic");

**语法** | **描述**
---|---
?getsweepresult; | 返回 names of all sweep, optimization, Monte Carlo, and S-参数 sweep objects with available results.
?getsweepresult("sweep_name"); | 返回 names of the available results from the specified sweep, optimization,Monte Carlo, or S-参数 sweep task.
out = getsweepresult("sweep_name", "result"); | 返回 the specified result 数据集 from the specified 参数 sweep, optimization, Monte Carlo, or S-参数 sweep task.

**示例**

This 示例 shows how to get data from a 参数 sweep. Please download the 示例 文件 from the [ 参数 sweeps ](/hc/en-us/articles/360034922873-参数-sweeps) page Associate files.
    ?getsweepresult("thickness_sweep");
    ?R = getsweepresult("thickness_sweep","R");
    image(R.lambda*1e6,R.thickness*1e6,R.T,"波长 (um)","thickness (um)","反射");
    > R
    > T
    > thickness
    > T vs lambda/f, thickness
This following commands show how to access optimization results:
First, see the available data.
    m="thickness_optimization";
    ?getsweepresult(m);
    > fom trend
    > best fom
    > 参数 trend
    > best parameters
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
Following is the 描述 of each available result:
    Available datasets
    fom trend :     Best result per generation. This is the quantity shown in the Optimization GUI window (1D 向量, Ng)  
    best fom :      Global best FOM. (Single 值, not 数据集) 
    参数 trend :  Parameters corresponding to FOM trend (3D 矩阵, 1 x Np x Ng)
    best parameters :  Parameters corresponding to global best FOM (1D 向量, Np)
    fom history :    Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
    参数 history : Every 参数 set used in optimization (3D maxtrix, Np x Nm x Ng)
    Available raw data. The following quantities are simply the simple 矩阵 versions of the above results
    genVec :       Generation 向量 (1D 向量, Ng)
    memberVec :     Generation member 向量 (1D 向量, Nm)
    paramsTrend :    Parameters corresponding to FOM trend (3D 矩阵, 1 x Np x Ng)
    fomTrend :      Best result per generation. This is the quantity shown in the Optimization GUI window
    paramHistory :    Every 参数 set used in optimization (3D maxtrix, Np x Nm x Ng)
    fomHistory :     Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
    bestParams :     Parameters corresponding to global best FOM (1D 向量, Np)
    bestFom :      Global best FOM (Single 值)
Get the global best Figure of merit

This 示例 shows how to get data from a 参数 sweep. Please download the 示例 文件 from the [ 参数 sweeps ](/hc/en-us/articles/360034922873-参数-sweeps) page Associate files.
    ?getsweepresult("thickness_sweep");
    ?R = getsweepresult("thickness_sweep","R");
    image(R.lambda*1e6,R.thickness*1e6,R.T,"波长 (um)","thickness (um)","反射");
    > R
    > T
    > thickness
    > T vs lambda/f, thickness
This following commands show how to access optimization results:
First, see the available data.
    m="thickness_optimization";
    ?getsweepresult(m);
    > fom trend
    > best fom
    > 参数 trend
    > best parameters
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
Following is the 描述 of each available result:
    Available datasets
    fom trend :     Best result per generation. This is the quantity shown in the Optimization GUI window (1D 向量, Ng)  
    best fom :      Global best FOM. (Single 值, not 数据集) 
    参数 trend :  Parameters corresponding to FOM trend (3D 矩阵, 1 x Np x Ng)
    best parameters :  Parameters corresponding to global best FOM (1D 向量, Np)
    fom history :    Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
    参数 history : Every 参数 set used in optimization (3D maxtrix, Np x Nm x Ng)
    Available raw data. The following quantities are simply the simple 矩阵 versions of the above results
    genVec :       Generation 向量 (1D 向量, Ng)
    memberVec :     Generation member 向量 (1D 向量, Nm)
    paramsTrend :    Parameters corresponding to FOM trend (3D 矩阵, 1 x Np x Ng)
    fomTrend :      Best result per generation. This is the quantity shown in the Optimization GUI window
    paramHistory :    Every 参数 set used in optimization (3D maxtrix, Np x Nm x Ng)
    fomHistory :     Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
    bestParams :     Parameters corresponding to global best FOM (1D 向量, Np)
    bestFom :      Global best FOM (Single 值)
Get the global best Figure of merit

**另请参阅**

[ Dataset introduction ](/hc/en-us/articles/360034409554-Datasets) , [ runsweep ](/hc/en-us/articles/360034931413-runsweep) , [ havesweepresult ](/hc/en-us/articles/360034409954-havesweepresult) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ savedata ](/hc/en-us/articles/360034411174-savedata) , [ getsweepdata ](/hc/en-us/articles/360034409794-getsweepdata) , [ savesweep ](/hc/en-us/articles/360034410014-savesweep) , [ loadsweep ](/hc/en-us/articles/360034409994-loadsweep)
