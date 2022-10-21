# percentile\_significance

business\_brio (pronounced “Business Brio”) is an open-source python package which contains sub-module named 'percentile\_significance'.

This submodule has one class named 'test' and this has more than one methods which are- 'result','pvalue','odds','cont\_table'.

This sub-module (percentile\_significance) of the package (business\_brio) will help you to perform a hypothesis test where you will find whether two different groups are significantly impacting another parameter value at a given percentile.

Let’s express a function as y=f(x), where the y variable is a continuous data type column and x is discrete data type column having only two levels or groups. There we can apply this submodule and its functions to check significance of those groups or levels of x variable on the value of y variable at a particular percentile value.

This is helpful to avoid the limitation of checking significance of two groups at only median or mean. Because it gives opportunity to check significant impact at any percentile value.

# How the dataset should be?

It is applicable for many use cases. Let’s say a dataset has two columns:

1. Machine type (having two levels  e.g. mc\_A, mc\_B).
1. Cycle\_time (this is a continuous data column having values). This is data of time taken for each items to be produced by any of these two machines mc\_A or mc\_B.

# How to install our package?

```
pip install business\_brio
```

# How to import and see the desired outputs?

```
from business\_brio import percentile\_significance

obj=percentile\_significance.test(arg1, arg2, arg3)

print(obj.result())

#Instead of direct result you can get only the pvalue by this way:

print(obj.pvalue())

#Instead of direct result you can get only the odds ratio value by this way:

print(obj.odds())

#Instead of direct result you can get only the contingency by this way:

print(obj.cont\_table())

```


# Arguments of the method test under the sub-module named percentile\_significance:

It takes three arguments:

arg1: A categorical column (two levels)

arg2: Output categorical column name (should have two levels 0 and 1. Where 0 refers unfulfilled and 1 refers fulfilled)

arg3: Group column name (should have two levels i.e. two group names)

Next 'result' named method is called,
```
print(obj.result())
```
It returns the result having p-value, a contingency table and odds value:


On the basis of p-value you can choose a hypothesis statement of any two of the following:

**Null Hypothesis: Two levels of arg1 has no significantly impact on arg2 at given percentile value.

**Alternate Hypothesis: Two levels of arg1 has significantly impact on arg2 at given percentile value.


# How this submodule is working (internal steps)?

Step1: Basically we are calculating the percentile value of the arg2.

Step2: We are splitting values of arg2 into two levels or groups
       \- greater equal percentile (values greater or equal to the percentile value) 
       \- smaller percentile (values less than the percentile value) 

Step3: Now we will create a contingency table to find frequency of each group of arg1 and these two newly created levels of arg2 column.

Step4: Now we will apply Fisher’s exact test on the contingency table.

This will return p-value, odds ratio

This p-value is basically applicable to 

Ho (null hypothesis): The odds ratio is equal to 1
Ha (alternate hypothesis): The odds ratio is not equal to 1

The odds ratio tells us how many times more positive cases can happen than negative cases.

This positive and negative cases is explained in the below example section.



# EXAMPLE:

from business\_brio import percentile\_significance
obj=percentile\_significance.test(df[“machine”],df[“cycle\_time”],0.4)
print(obj.result())


In this above code you will get a contingency table:

||X|
| :- | :-: |
|Y|Mac\_A|Mac\_B|
|Greater\_equal\_percentile|5|9|
|Smaller\_percentile|6|4|

The p-value: 0.408096642702929

The odds value: 0.37037037037037035

N.B: 'df' is the name of the dataframe having columns "machine", "cycle\_time".

**Inference:
From the above p-value we will accept null hypothesis (with confidence interval of 95%).
So, the two groups of machine (Mac\_A, Mac\_B) has no significant impact on cycle time.


For statistical evidence read this section:

Actually this p-value of the exact fisher’s test is valid for the following hypothesis:

Ho (null hypothesis): The odds ratio is equal to 1
Ha (alternate hypothesis): The odds ratio is not equal to 1

As said early, the odds ratio tells us how many times more positive cases can happen than negative cases. 

So, for the above given example odds ratio = Positive cases * Negative cases

This positive and negative case means,

(Frequency of smaller percentile of Mac_A * frequency of greater percentile of Mac_B) / (Frequency of greater percentile of Mac_A * frequency of smaller percentile of Mac_B)


So, basically from the example table:

=(5*4)/(9*6)

=20/54

=0.37037


So, if for your dataset if p value returned is 1.000, then it shows with the probability of (1- 1) 0%, the odds ratio will not be equal to 1 and with the probability of 100%, the odds ratio will equal 1. 

If we set our confidence level at 95% percentage because 1.00 is higher than 0.05 (1- 0.95). We accept the null hypothesis. 

It means there is a considerable probability that the odds ratio might be equal to 1 in the population (other untested cycle times). 

And we know if odds ratio is 1 or close to 1 it means that there isn’t any difference between positive and negative cases.

So, this makes a conclusion that two groups of machines Mac\_A and Mac\_B has no significant impact on the cycle time. 

Errors:

If you are getting error messages. Please check the following: Whether the arg1 passed is dataframe with no null or not Whether the arg2 is name of the salesman column which has more than one levels ( multiple unique names or entries ). Whether the arg3 is name of the saleflag column which has only two levels ( only two unique name or entries 0 refers unsold and 1 refers sold). Whether the arg4 is name of the group column which has only two levels (only two unique names or entries ).

Useful links and licenses:
