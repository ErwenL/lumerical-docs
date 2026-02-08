# isfield

The script command checks whether input is a field.

| **Syntax**                    | **Description**                                                                                                                                |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| value= isfield(input, field); | Determine whether ‘input contains filed name ‘field’. It returns logical 1 (true) if ‘input contains ‘field’, and logical 0 (false) otherwise. |

### Example

```
>x=struct;
>x.t=10;
>?isfield(x,'t');
result: 
1
```

### See Also

[ issweep ](./issweep.md) , [ isstruct ](./isstruct.md) , [ iscell ](./iscell.md) ,
[ getfield ](./getfield.md) , [ setfield ](./setfield.md)
