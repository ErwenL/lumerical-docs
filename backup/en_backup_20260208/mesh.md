# mesh

Produces a mesh of the current structure that is required to perform a subsequent calculation. In MODE, it produces a d-card called "material" which contains the material properties of the meshed object. 

This is equivalent to pressing the "mesh structure" button in the graphical user interface of MODE, or "Mesh" button in Finite Element IDE. 

**Syntax** |  **Description**  
---|---  
mesh;  |  Mesh the current simulation in FDE, DGTD, or FEEM. In MODE, it can be used only with FDE solver. In Finite Element IDE, it meshes the simulation that is present (DGTD or FEEM)   
mesh("solver_name");  |  Mesh the current simulation in the desired solver defined by the argument "solver_name". Argument name is supported only in Finite Element IDE, and the options are "DGTD" and "FEEM".   
  
**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ setanalysis ](/hc/en-us/articles/360034925113-setanalysis) , [ mesh ](/hc/en-us/articles/360034410654-mesh) , [ findmodes ](/hc/en-us/articles/360034405214-findmodes) , [ frequencysweep ](/hc/en-us/articles/360034925153-frequencysweep) , [ analysis ](/hc/en-us/articles/360034405194-analysis) , [ getanalysis ](/hc/en-us/articles/360034925133-getanalysis)
