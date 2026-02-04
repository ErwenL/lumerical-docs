<!--
Translation from English documentation
Original command: arrayperiodicdata
Translation date: 2026-02-04 22:49:36
-->

# arrayperiodicdata

Generates 一个 数组 的 periodic 数据 从 一个 unit 单元格 dataset based 在 一个 given plane 的 periodicity. This 函数 是 useful 用于 obtaining 该 complete form 的 数据 从 一个 periodic 仿真 该 only contains 数据 从 one unit 单元格. Only unstructured data设置是 supported 通过 此 命令。 

**语法** |  **描述**  
---|---  
arrayperiodicdata(dataset,'periodic_plane',count);  |  Unfolds 数据 从 一个 symmetric dataset based 在 一个 given plane 的 symmetry.  The first 参数 是 一个 2D 或 3D unstructured dataset. The second 参数 是 该 plane 使用 respect 到 该 数据 是 periodic 在 该 format [+-][xyz], e.g. “-y” 和 refers 到 该 axis 的 该 plane 的 periodicity (i.e. 该 direction 用于 该 periodicity 向量 将 为 taken 从 该 sign, 和 该 plane, e.g. y-normal, 将 为 used 用于 arraying). The third 参数 count 是 数字 的 unit cells 到 copy 在 该 数组 (如果 1, only 返回 该 unit 单元格).   
  
**示例**

Below is a simple example of creating a periodic array of unstructured dataset generated from data available in the [ unstructured_charge_example.mat ](https://lumerical.zendesk.com/hc/article_attachments/360046127913/unstructured_charge_example.mat) file by assuming that the data is periodic in the "-y" direction and contains 3 unit cells. 
    
    
    matlabload("unstructured_charge_example.mat");
    x = 电荷.x;
    y = 电荷.y;
    z = 电荷.z;
    C = 电荷.elements;
    数据 = unstructureddataset("test",x,y,z,C);
    periodic_data=arrayperiodicdata(数据,'-y',3);

**参见**

[ unfoldsymmetricdata ](/hc/en-us/articles/360034929953-unfoldsymmetricdata) , [ unstructureddataset ](/hc/en-us/articles/360034929933-unstructureddataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ addattribute ](/hc/en-us/articles/360034929873-addattribute) , [ addparameter ](/hc/en-us/articles/360034409494-addparameter) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ 结构体 ](/hc/en-us/articles/360034409574-结构体)
