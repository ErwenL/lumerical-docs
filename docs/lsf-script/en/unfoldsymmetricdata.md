# unfoldsymmetricdata

Unfolds data from a symmetric dataset based on a given plane of symmetry. This function is useful for obtaining the complete form of data from a symmetric simulation which only contains data from one half of the simulation. Only unstructured datasets are supported by this command. 

**Syntax** |  **Description**  
---|---  
unfoldsymmetricdata(dataset,'symmetry_plane');  |  Unfolds data from a symmetric dataset based on a given plane of symmetry.  The first argument is a 2D or 3D unstructured dataset. The second argument is the plane of symmetry for the symmetric data in the format [+-][xyz], e.g. “-y” and refers to the axis of the plane of symmetry (i.e. the side of the simulation region that will act as the plane of symmetry)   
  
**Examples**

Below is a simple example of unfolding an unstructured dataset generated from data available in the [ unstructured_charge_example.mat ](https://lumerical.zendesk.com/hc/article_attachments/360046127893/unstructured_charge_example.mat) file by assuming that the data is symmetric with respect to the "+y" plane. 
    
    
    matlabload("unstructured_charge_example.mat");
    x = charge.x;
    y = charge.y;
    z = charge.z;
    C = charge.elements;
    data = unstructureddataset("test",x,y,z,C);
    data_unfolded=unfoldsymmetricdata(data,'+y');

**See Also**

[ arrayperiodicdata ](/hc/en-us/articles/360034409594-arrayperiodicdata) , [ unstructureddataset ](/hc/en-us/articles/360034929933-unstructureddataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ addattribute ](/hc/en-us/articles/360034929873-addattribute) , [ addparameter ](/hc/en-us/articles/360034409494-addparameter) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ struct ](/hc/en-us/articles/360034409574-struct)
