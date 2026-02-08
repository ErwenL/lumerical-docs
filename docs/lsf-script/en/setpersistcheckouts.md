# setpersistcheckouts

Sets whether
[persistent license checkout](https://optics.ansys.com/hc/en-us/articles/43817775863059-Upfront-and-Persistent-License-Checkout)
is enabled.

| **Syntax**                    | **Description**                                                                                                                             |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| setpersistcheckouts(“state”); | Set whether the upfront license checkout feature is enabled. The only accepted states are logical true and false states or logical 0 and 1. |

**Example**

```
#Enable the persistent license checkout feature
  
setpersistcheckouts(true);

#Disable the persistent license checkout feature
#The logical 0 is used in place of false here

setpersistcheckouts(0);
```
