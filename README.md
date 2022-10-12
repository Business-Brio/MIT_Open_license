# bhargabchipkg
**bhargabchipkg** (pronounced “Bhargab chi package”) is an open-source package for applying chi square (a statistical test) which is helpful for mathematics, science, and engineering. Chi square is already written package available with scipy. But, this package(bhargabchipkg) will help you to sort out the salesman ranks (good or bad)

## How the dataset should be?

It is applicable for sales data having minimum three columns:
 salesman id (or name, etc having more than one level).
 saleflag i.e. 0 and 1 where 0 refers unsold and 1 refers sold.
 type of item (only two levels i.e. two types of items).


## How to install our package?

```
pip install bhargabchipkg
```

## how to import and see the desired output?
```
from bhargabchipkg import chitest_rs
obj=chitest_rs.ChiTest2(arg1,arg2,arg3,arg4)
table,intpret=obj.chi_test()
print("Interpreted result:")
print(intpret)
print("table result:")
print(table)
```
## Arguments of the method chitest_rs.ChiTest2(arg1, arg2, arg3, arg4):

**It takes four inputs:**

**arg1. a dataframe with categorical columns for input as well as output**

**arg2. Input categorical column name (more than one level)**

**arg3. Output categorical column name(should have two levels 0 and 1. Where 0 refers unsold and 1 refers sold)**

**arg4. Groupby column name(should have two levels)**

the column names (arg2, arg3, arg4) must be passed as string (inside double inverted commas)

    
   
   

**It returns two:**

**return1: table**

**return2: interpretation**

both are dictionary type

## Errors:
 
 If you are getting error messages. Please check the following:
 Whether the arg1 passed is dataframe with no null or not
 Whether the arg2 is name of the column which has more than one levels ( multiple unique name or entries ).
 Whether the arg3 is name of the column which has only two levels ( only two unique name or entries ).
 Whether the arg4 is name of the column which has only two levels ( only two unique name or entries ).



Useful links and licenses:

You can find the example datasheet from this link:
You can see the output from this link: 


Source code:https://github.com/bhargabganguli/bhargabchipkg.git

Bug reports: https://github.com/bhargabganguli/bhargabchipkg/issues


License
Â© 2022 Bhargab Ganguli

This repository is licensed under the MIT license. 
See  https://github.com/bhargabganguli/bhargabchipkg/blob/0.0.4/LICENSE   for details.
