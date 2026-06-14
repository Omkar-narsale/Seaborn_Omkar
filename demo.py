import demo as sns
import matplotlib.pyplot as plt
#Basic Ploting
tips=sns.load_dataset('tips')
# print(tips)

#Scatter plot
# sns.scatterplot(x='total_bill',y='tip',data=tips)
# plt.title("Total_Bill vs Tips")
# plt.show()

#Line Plot
# sns.lineplot(x='size',y='total_bill',data=tips)
# plt.title("Total_bill by size")
# plt.show()

#Categorical Plot
# sns.barplot(x='day',y='total_bill',data=tips)
# plt.title("Day vs Total_bill")
# plt.show()

#Box Plot
# sns.boxplot(x='day',y='total_bill',data=tips)
# plt.show()

#Vilion Plot
# sns.violinplot(x='day',y='total_bill',data=tips)
# plt.show()

#Histogram
# sns.histplot(tips['total_bill'],bins=10,kde=True)
# plt.show()

#KDE Plot
# sns.kdeplot(tips['total_bill'],shade=True,fill=True)
# plt.show()

#Pair PLot
# sns.pairplot(tips)
# plt.show()

#HeatMap
corr=tips[['total_bill','tip','size']].corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()