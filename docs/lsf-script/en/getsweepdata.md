# getsweepdata

Gets raw data from a parameter sweep/optimization/Monte Carlo analysis. In most cases,
it is more convenient to get a complete dataset with getsweepresult , rather than
getting individual data elements with getsweepdata .

| **Syntax**                                | **Description**                                                                                                               |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ?getsweepdata;                            | Returns names of all sweep, optimization, and Monte Carlo analysis objects.                                                   |
| ?getsweepdata("sweep_name");              | Returns all the names of the available data which is stored in the sweep, optimization, or Monte Carlo analysis object.       |
| out = getsweepdata("sweep_name", "data"); | Returns parameter sweep, optimization, or Monte Carlo analysis data. The following data can be obtained from an optimization: |

- fomTrend - Figure of merit as a function of generation
- fomHistory - Figure of merit history (for each generation there will be generation
  size number)
- bestFom - Best figure of merit obtained during sweep
- bestParameter - Parameter which corresponds to bestFom
- paramHistory - Parameter history

For a parameter sweep and Monte Carlo analysis, this command returns both parameters and
results.

**Examples**

This example shows how to get data from a parameter sweep. Please download the example
file from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
m="thickness_sweep";
?getsweepdata(m);
th = getsweepdata(m,"thickness"); # get parameter from sweep
R = getsweepdata(m,"R");# get result from sweep
plot(th*1e6,R,"thickness (microns)","Reflection");
> R
> T
> thickness 
```

This example shows how to access data from an optimization.

```
m="thickness_optimization";
?getsweepdata(m);
genVec = getsweepdata(m,"genVec");       # Generation vector (1D vector, Ng)
memberVec = getsweepdata(m,"memberVec");    # Generation member vector (1D vector, Nm)
fomTrend = getsweepdata(m,"fomTrend");     # Best of each generation, same as shown in Opt. GUI window (1D vector, Ng)
paramsTrend = getsweepdata(m,"paramsTrend");  # Parameters corresponding to FOM trend (3D matrix, 1 x Np x Ng)
bestFom = getsweepdata(m,"bestFom");      # Global best FOM
bestParams = getsweepdata(m,"bestParams");   # Parameters corresponding to global best FOM (1D vector, Np)
fomHistory = getsweepdata(m,"fomHistory");   # Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
paramHistory = getsweepdata(m,"paramHistory"); # Every parameter set used in optimization (3D maxtrix, Np x Nm x Ng)
plot(genVec,fomTrend,"generation number","fom Trend","best FOM of each generation"); 
?"Best FOM: "+num2str(bestFom);
?"Best Params: "+num2str(bestParams);
?"Total number of simulations run: "+num2str(length(genVec)*length(memberVec));
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
> Total number of simulations run: 50
```

**See Also**

[ getdata ](./getdata.md) , [ runsweep ](./runsweep.md) ,
[ havesweepdata ](./havesweepdata.md) , [ savedata ](./savedata.md) ,
[ getsweepresult ](./getsweepresult.md) , [ savesweep ](./savesweep.md) ,
[ loadsweep ](./loadsweep.md)
