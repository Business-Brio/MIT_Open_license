import pandas as pd #install pandas to read the dataset
#create dataframe object named 'data' to store after reading data using pandas
#Use the path of the downloaded or created data.
# I have kept it in C drive under a folder named 'bhargab drive' of my local machine.

data=pd.read_csv(r"test_data.csv")

#install package and sub-module
from business_brio import performance_rank_discrete


obj=performance_rank_discrete.test(data,'salesman_id', 'saleflag', 'matched_table') #object creation

table,intrprt=obj.result(n=30) #method calling by taking two objects (table and intrprt)

#See the outputs:
print("Interpreted result")
print(intrprt)
print("table result")
print(table)