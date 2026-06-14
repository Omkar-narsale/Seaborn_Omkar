import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
sales_df=pd.read_csv('data_udemy.csv')
print(sales_df.head())

# plt.figure(figsize=(10,6))
# sns.barplot(x='Category',y='Sales',data=sales_df,estimator=sum)
# plt.title("Total Sales By Product")
# plt.xlabel('Category')
# plt.ylabel('Sales')
# plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x='Region',y='Sales',data=sales_df,estimator=sum)
plt.title("Total Sales By Region")
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()