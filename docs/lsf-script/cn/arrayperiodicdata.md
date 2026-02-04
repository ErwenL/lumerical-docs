<!-- Translation completed: 2026-02-04 -->
<!-- Original command: arrayperiodicdata -->

# arrayperiodicdata

**语法** | **描述**
---|---
arrayperiodicdata(dataset,'periodic_plane',count); | Unfolds data from a symmetric 数据集 based on a given plane of symmetry.  The first 参数 is a 2D or 3D unstructured 数据集. The second 参数 is the plane with respect to which data is periodic in the 格式 [+-][xyz], e.g. “-y” and refers to the axis of the plane of periodicity (i.e. the direction for the periodicity 向量 will be taken from the sign, and that plane, e.g. y-normal, will be used for arraying). The third 参数 count is 数字 of unit cells to copy in the 数组 (if 1, only 返回 the unit cell).

**示例**

Below is a simple 示例 of creating a periodic 数组 of unstructured 数据集 generated from data available in the [ unstructured_charge_example.mat ](https://lumerical.zendesk.com/hc/article_attachments/360046127913/unstructured_charge_example.mat) 文件 by assuming that the data is periodic in the "-y" direction and contains 3 unit cells. 
    matlabload("unstructured_charge_example.mat");
    x = charge.x;
    y = charge.y;
    z = charge.z;
    C = charge.元素;
    data = unstructureddataset("test",x,y,z,C);
    periodic_data=arrayperiodicdata(data,'-y',3);

Below is a simple 示例 of creating a periodic 数组 of unstructured 数据集 generated from data available in the [ unstructured_charge_example.mat ](https://lumerical.zendesk.com/hc/article_attachments/360046127913/unstructured_charge_example.mat) 文件 by assuming that the data is periodic in the "-y" direction and contains 3 unit cells. 
    matlabload("unstructured_charge_example.mat");
    x = charge.x;
    y = charge.y;
    z = charge.z;
    C = charge.元素;
    data = unstructureddataset("test",x,y,z,C);
    periodic_data=arrayperiodicdata(data,'-y',3);

**另请参阅**

[ unfoldsymmetricdata ](/hc/en-us/articles/360034929953-unfoldsymmetricdata) , [ unstructureddataset ](/hc/en-us/articles/360034929933-unstructureddataset) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ addattribute ](/hc/en-us/articles/360034929873-addattribute) , [ addparameter ](/hc/en-us/articles/360034409494-addparameter) , [ visualize ](/hc/en-us/articles/360034410514-visualize) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ getparameter ](/hc/en-us/articles/360034409514-getparameter) , [ getattribute ](/hc/en-us/articles/360034409534-getattribute) , [ matrixdataset ](/hc/en-us/articles/360034409454-matrixdataset) , [ struct ](/hc/en-us/articles/360034409574-struct)
