# arrayperiodicdata

Generates an array of periodic data from a unit cell dataset based on a given plane of periodicity. This function is useful for obtaining the complete form of data from a periodic simulation which only contains data from one unit cell. Only unstructured datasets are supported by this command. 

**Syntax** |  **Description**  
---|---  
arrayperiodicdata(dataset,'periodic_plane',count);  |  Unfolds data from a symmetric dataset based on a given plane of symmetry.  The first argument is a 2D or 3D unstructured dataset. The second argument is the plane with respect to which data is periodic in the format [+-][xyz], e.g. “-y” and refers to the axis of the plane of periodicity (i.e. the direction for the periodicity vector will be taken from the sign, and that plane, e.g. y-normal, will be used for arraying). The third argument count is number of unit cells to copy in the array (if 1, only returns the unit cell).   
  
**Examples**

Below is a simple example of creating a periodic array of unstructured dataset generated from data available in the [ unstructured_charge_example.mat ](https://lumerical.zendesk.com/hc/article_attachments/360046127913/unstructured_charge_example.mat) file by assuming that the data is periodic in the "-y" direction and contains 3 unit cells. 
    
    
    matlabload("unstructured_charge_example.mat");
    x = charge.x;
    y = charge.y;
    z = charge.z;
    C = charge.elements;
    data = unstructureddataset("test",x,y,z,C);
    periodic_data=arrayperiodicdata(data,'-y',3);

**See Also**

[ unfoldsymmetricdata ](/hc/en-us/articles/360034929953-unfoldsymmetricdata) , [ unstructureddataset ](/hc/en-us/articles/360034929933-unstructureddataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ addattribute ](/hc/en-us/articles/360034929873-addattribute) , [ addparameter ](/hc/en-us/articles/360034409494-addparameter) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ struct ](/hc/en-us/articles/360034409574-struct)
