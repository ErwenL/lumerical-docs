<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getsweepdata -->

# getsweepdata

**语法** | **描述**
---|---
?getsweepdata; | 返回 names of all sweep, optimization, and Monte Carlo analysis objects.
?getsweepdata("sweep_name"); | 返回 all the names of the available data which is stored in the sweep, optimization, or Monte Carlo analysis object.
out = getsweepdata("sweep_name", "data"); | 返回 参数 sweep, optimization, or Monte Carlo analysis data.  The following data can be obtained from an optimization:

**示例**

This 示例 shows how to get data from a 参数 sweep. Please download the 示例 文件 from the [ 参数 sweeps ](/hc/en-us/articles/360034922873-参数-sweeps) page Associate files. 
    m="thickness_sweep";
    ?getsweepdata(m);
    th = getsweepdata(m,"thickness"); # get 参数 from sweep
    R = getsweepdata(m,"R");# get result from sweep
    plot(th*1e6,R,"thickness (microns)","反射");
    > R
    > T
    > thickness 
This 示例 shows how to access data from an optimization. 
    m="thickness_optimization";
    ?getsweepdata(m);
    genVec = getsweepdata(m,"genVec");       # Generation 向量 (1D 向量, Ng)
    memberVec = getsweepdata(m,"memberVec");    # Generation member 向量 (1D 向量, Nm)
    fomTrend = getsweepdata(m,"fomTrend");     # Best of each generation, same as shown in Opt. GUI window (1D 向量, Ng)
    paramsTrend = getsweepdata(m,"paramsTrend");  # Parameters corresponding to FOM trend (3D 矩阵, 1 x Np x Ng)
    bestFom = getsweepdata(m,"bestFom");      # Global best FOM
    bestParams = getsweepdata(m,"bestParams");   # Parameters corresponding to global best FOM (1D 向量, Np)
    fomHistory = getsweepdata(m,"fomHistory");   # Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
    paramHistory = getsweepdata(m,"paramHistory"); # Every 参数 set used in optimization (3D maxtrix, Np x Nm x Ng)
    plot(genVec,fomTrend,"generation 数字","fom Trend","best FOM of each generation"); 
    ?"Best FOM: "+num2str(bestFom);
    ?"Best Params: "+num2str(bestParams);
    ?"Total 数字 of simulations run: "+num2str(长度(genVec)*长度(memberVec));
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
    > Total 数字 of simulations run: 50

This 示例 shows how to get data from a 参数 sweep. Please download the 示例 文件 from the [ 参数 sweeps ](/hc/en-us/articles/360034922873-参数-sweeps) page Associate files. 
    m="thickness_sweep";
    ?getsweepdata(m);
    th = getsweepdata(m,"thickness"); # get 参数 from sweep
    R = getsweepdata(m,"R");# get result from sweep
    plot(th*1e6,R,"thickness (microns)","反射");
    > R
    > T
    > thickness 
This 示例 shows how to access data from an optimization. 
    m="thickness_optimization";
    ?getsweepdata(m);
    genVec = getsweepdata(m,"genVec");       # Generation 向量 (1D 向量, Ng)
    memberVec = getsweepdata(m,"memberVec");    # Generation member 向量 (1D 向量, Nm)
    fomTrend = getsweepdata(m,"fomTrend");     # Best of each generation, same as shown in Opt. GUI window (1D 向量, Ng)
    paramsTrend = getsweepdata(m,"paramsTrend");  # Parameters corresponding to FOM trend (3D 矩阵, 1 x Np x Ng)
    bestFom = getsweepdata(m,"bestFom");      # Global best FOM
    bestParams = getsweepdata(m,"bestParams");   # Parameters corresponding to global best FOM (1D 向量, Np)
    fomHistory = getsweepdata(m,"fomHistory");   # Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
    paramHistory = getsweepdata(m,"paramHistory"); # Every 参数 set used in optimization (3D maxtrix, Np x Nm x Ng)
    plot(genVec,fomTrend,"generation 数字","fom Trend","best FOM of each generation"); 
    ?"Best FOM: "+num2str(bestFom);
    ?"Best Params: "+num2str(bestParams);
    ?"Total 数字 of simulations run: "+num2str(长度(genVec)*长度(memberVec));
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
    > Total 数字 of simulations run: 50

**另请参阅**

[ getdata ](/hc/en-us/articles/360034409834-getdata) , [ runsweep ](/hc/en-us/articles/360034931413-runsweep) , [ havesweepdata ](/hc/en-us/articles/360034409934-havesweepdata) , [ savedata ](/hc/en-us/articles/360034411174-savedata) , [ getsweepresult ](/hc/en-us/articles/360034409814-getsweepresult) , [ savesweep ](/hc/en-us/articles/360034410014-savesweep) , [ loadsweep ](/hc/en-us/articles/360034409994-loadsweep)
