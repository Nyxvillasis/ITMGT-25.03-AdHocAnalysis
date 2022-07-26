import json
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import re

%matplotlib inline

filename = "transaction-data-adhoc-analysis.json"
df = pd.read_json(filename)

table1_df = df[["transaction_items", "transaction_date"]]

table1_df2 = table1_df.transaction_items.str.split(";")
table1_df2.index = table1_df.transaction_date
table1_df2 = table1_df2.reset_index("transaction_date")
table1_df3 = table1_df2.explode("transaction_items")
table1_df3["DATE"] = pd.to_datetime(df["transaction_date"])
table1_df3["Month"] = table1_df3["DATE"].dt.month

brands = ["Exotic Extras,", "HealthyKid 3+,", "Candy City,"] 
table1_df3["transaction_items"] = table1_df3["transaction_items"].str.replace("|".join(map(re.escape, brands)),"")
table1_df3["QTY"] = table1_df3["transaction_items"].str[-2]

table1_df3["QTY"]=table1_df3["QTY"].astype(int)
quantities = [",(x1)", ",(x2)", ",(x3)", ",(x4)"] 
table1_df3["transaction_items"] = table1_df3["transaction_items"].str.replace("|".join(map(re.escape, quantities)),"")

table1_df4 = table1_df3[["transaction_items", "Month", "QTY"]]

table1_df5 = table1_df4.pivot_table("QTY", ["transaction_items"], "Month", aggfunc="sum")

table1_df5

table1_df6 = table1_df5
table1_df7 = table1_df6.reset_index()
table1_df7.columns = ["Transaction_Items","January", "February", "March", "April", "May", "June"]

table1_bargraph = table1_df7.plot.bar(x="Transaction_Items", y = ["January", "February", "March", "April", "May", "June"],figsize = (25,10), title="Count of Items sold per Item per Month")
table1_bargraph.legend(loc=4,fontsize="medium")

Beef_Chicharon = [9665, 10001, 9816, 9890, 10028, 9902]
Labels = ["January", "February", "March", "April", "May", "June"]
Table1_BeefChicharonPieChart = plt.pie(Beef_Chicharon, labels=Labels, autopct='%1.0f%%')
plt.title("Beef Chicharon Orders By Month")

Gummy_Vitamins = [9681, 9980, 10145, 9842, 9948, 9980]
Labels = ["January", "February", "March", "April", "May", "June"]
Table1_GummyVitaminsPieChart = plt.pie(Gummy_Vitamins, labels=Labels, autopct='%1.0f%%')
plt.title("Gummy Vitamins Orders By Month")

Gummy_Worms = [9559, 9996, 9986, 10043, 9801, 9934]
Labels = ["January", "February", "March", "April", "May", "June"]
Table1_GummyWormsPieChart = plt.pie(Gummy_Worms, labels=Labels, autopct='%1.0f%%')
plt.title("Gummy Worms Orders By Month")

Kimchi_Seaweed = [9676, 9949, 9967, 9921, 9773, 10104]
Labels = ["January", "February", "March", "April", "May", "June"]
Table1_KimchiSeaweedPieChart = plt.pie(Kimchi_Seaweed, labels=Labels, autopct='%1.0f%%')
plt.title("Kimchi & Seaweed Orders By Month")

Nutritional_Milk = [9727, 9691, 9876, 9786, 9881, 9767]
Labels = ["January", "February", "March", "April", "May", "June"]
Table1_NutritionalMilkPieChart = plt.pie(Nutritional_Milk, labels=Labels, autopct='%1.0f%%')
plt.title("Nutritional Milk Orders By Month")

Orange_Beans = [9774, 10037, 9611, 9914, 9964, 10106]
Labels = ["January", "February", "March", "April", "May", "June"]
Table1_OrangeBeansChart = plt.pie(Orange_Beans, labels=Labels, autopct='%1.0f%%')
plt.title("Orange Beans Orders By Month")

Yummy_Vegetables = [9959, 10256, 9896, 9861, 9735, 9722]
Labels = ["January", "February", "March", "April", "May", "June"]
Table1_YummyVegetablesChart = plt.pie(Yummy_Vegetables, labels=Labels, autopct='%1.0f%%')
plt.title("Yummy Vegetables Orders By Month")