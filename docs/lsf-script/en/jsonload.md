# jsonload

Returns the value of a JSON file.

| **Syntax**            | **Description**                                                     |
| --------------------- | ------------------------------------------------------------------- |
| jsonload("filename"); | Returns the values of the json file (struct, cell, string, number). |

### Example

The following code example shows how to load the data of the JSON file "test_json.json".

```
jsonload("test_json.json");
?a;
?b;
```

The output result looks like:

```
?a;
result: 
1  
?b;
result: 
1+2i  3+4i  
```

**See Also**

[ jsonsave ](./jsonsave.md) ,
[ jsonloads ](https://optics.ansys.com/hc/en-us/articles/360038741854) ,
[ jsonsaves ](https://optics.ansys.com/hc/en-us/articles/360039235453) ,
[ JSON files ](https://optics.ansys.com/hc/en-us/articles/360034936933-JSON-files)
