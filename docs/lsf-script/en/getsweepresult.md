# getsweepresult

Gets the parameter sweep/optimization/Monte Carlo/S-parameter sweep results in the form
of a dataset.

| **Syntax**                                    | **Description**                                                                                                                |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| ?getsweepresult;                              | Returns names of all sweep, optimization, Monte Carlo, and S-parameter sweep objects with available results.                   |
| ?getsweepresult("sweep_name");                | Returns names of the available results from the specified sweep, optimization,Monte Carlo, or S-parameter sweep task.          |
| out = getsweepresult("sweep_name", "result"); | Returns the specified result dataset from the specified parameter sweep, optimization, Monte Carlo, or S-parameter sweep task. |

**Examples**

This example shows how to get data from a parameter sweep. Please download the example
file from the
[ Parameter sweeps ](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
page Associate files.

```
?getsweepresult("thickness_sweep");
?R = getsweepresult("thickness_sweep","R");
image(R.lambda*1e6,R.thickness*1e6,R.T,"wavelength (um)","thickness (um)","reflection");
> R
> T
> thickness
> T vs lambda/f, thickness
```

This following commands show how to access optimization results:

First, see the available data.

```
m="thickness_optimization";
?getsweepresult(m);
> fom trend
> best fom
> parameter trend
> best parameters
> fom history
> parameter history
> genVec
> memberVec
> paramsTrend
> fomTrend
> paramHistory
> fomHistory
> bestParams
> bestFom
```

Following is the description of each available result:

```
Available datasets
fom trend :     Best result per generation. This is the quantity shown in the Optimization GUI window (1D vector, Ng)  
best fom :      Global best FOM. (Single value, not dataset) 
parameter trend :  Parameters corresponding to FOM trend (3D matrix, 1 x Np x Ng)
best parameters :  Parameters corresponding to global best FOM (1D vector, Np)
fom history :    Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
parameter history : Every parameter set used in optimization (3D maxtrix, Np x Nm x Ng)
Available raw data. The following quantities are simply the simple matrix versions of the above results
genVec :       Generation vector (1D vector, Ng)
memberVec :     Generation member vector (1D vector, Nm)
paramsTrend :    Parameters corresponding to FOM trend (3D matrix, 1 x Np x Ng)
fomTrend :      Best result per generation. This is the quantity shown in the Optimization GUI window
paramHistory :    Every parameter set used in optimization (3D maxtrix, Np x Nm x Ng)
fomHistory :     Every FOM calculated in optimization (2D maxtrix, Nm x Ng)
bestParams :     Parameters corresponding to global best FOM (1D vector, Np)
bestFom :      Global best FOM (Single value)
```

Get the global best Figure of merit

```
# get the best FOM
?getsweepresult("thickness_optimization","best fom");
> result: 
0.00187328
```

Plot the Figure of merit trend

```
FOMtrend = getsweepresult("thickness_optimization","fom trend");
plot(FOMtrend.generation,FOMtrend.fom);
```

The following script is an excerpt from the example script from
[ S-parameter matrix sweep ](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep)
showing how to collect the results from an S-parameter sweep.

```
# collect results
S_matrix = getsweepresult("s-parameter sweep","S matrix");
S_parameters = getsweepresult("s-parameter sweep","S parameters");
S_diagnostic = getsweepresult("s-parameter sweep","S diagnostic");
```

**See Also**

[ Dataset introduction ](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
, [ runsweep ](./runsweep.md) , [ havesweepresult ](./havesweepresult.md) ,
[ getresult ](./getresult.md) , [ savedata ](./savedata.md) ,
[ getsweepdata ](./getsweepdata.md) , [ savesweep ](./savesweep.md) ,
[ loadsweep ](./loadsweep.md)
