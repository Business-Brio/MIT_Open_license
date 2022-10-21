import pandas as pd #install pandas to read the dataset

# make sure you have installed our package business_brio
#create dataframe object named 'data' to store after reading data using pandas

data=pd.read_csv(r"test_data.csv")

#install package and sub-module
from business_brio import percentile_significance

obj=percentile_significance.test(df["MACHINE"],df["cycle_time_DAYS"]) #object creation

obj.result() # result method is called

# Instead of getting p-value, odds-ratio, contingency table togetherly,
# you can get these individually by calling following methods
obj.pvalue() # to get only p-value.
obj.odds() # to get only odds ratio
obj.cont_table() #to get only the contingency table