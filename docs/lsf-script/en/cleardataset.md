# cleardataset

This command clears the dataset from any current 'np Density' grid attribute. This is
only useful for keeping file size small.

| **Syntax**    | **Description**                                      |
| ------------- | ---------------------------------------------------- |
| cleardataset; | Clears the dataset from the selected grid attribute. |

**Examples**

This example shows how to import an unstructured dataset 'charge' to the 'np Density'
grid attribute.

```
select("np density");
importdataset("device_data.mat");
cleardataset;
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ importdataset ](./importdataset.md) , [ addgridattribute ](./addgridattribute.md)
