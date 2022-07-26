import json
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import re

%matplotlib inline

filename = "transaction-data-adhoc-analysis.json"
df = pd.read_json(filename)

table2_df = df[["transaction_items", "transaction_value", "transaction_date"]]
table2_df2 = table2_df.transaction_items.str.split(";")
table2_df2.index = table2_df.transaction_date
table2_df2 = table2_df2.reset_index("transaction_date")
table2_df3 = table2_df2.explode("transaction_items")
table2_df3["transaction_value"] = table2_df["transaction_value"]
table2_df3["DATE"] = pd.to_datetime(df["transaction_date"])
table2_df3["Month"] = table2_df3["DATE"].dt.month

brands = ["Exotic Extras,", "HealthyKid 3+,", "Candy City,"] 
table2_df3["transaction_items"] = table2_df3["transaction_items"].str.replace("|".join(map(re.escape, brands)),"")

table2_df3["QTY"] = table2_df3["transaction_items"].str[-2]
table2_df3["QTY"] = table2_df3["QTY"].astype(int)
quantities = [",(x1)", ",(x2)", ",(x3)", ",(x4)"] 
table2_df3["transaction_items"] = table2_df3["transaction_items"].str.replace("|".join(map(re.escape, quantities)),"")

table2_df4 = table2_df3[["Month","transaction_items","QTY","transaction_value"]]

conditions = [
    (table2_df4["transaction_items"] == "Beef Chicharon"), 
    (table2_df4["transaction_items"] == "Gummy Vitamins"),
    (table2_df4["transaction_items"] == "Gummy Worms"),
    (table2_df4["transaction_items"] == "Kimchi and Seaweed"),
    (table2_df4["transaction_items"] == "Nutrional Milk"),
    (table2_df4["transaction_items"] == "Orange Beans"),
    (table2_df4["transaction_items"] == "Yummy Vegetables"),
]

values = [1299, 1500, 150, 799, 1990, 199, 500]

table2_df4["Price of Item"] =  np.select(conditions, values)

table2_df5 = table2_df4[["Month", "transaction_items", "Price of Item", "QTY", "transaction_value"]]
table2_df5["QTY"] = table2_df5["QTY"].astype(int)

table2_df5["Total Sale Value"] = table2_df5["Price of Item"] * table2_df5["QTY"]
table2_df5 = table2_df5[["Month", "transaction_items", "Price of Item", "QTY", "Total Sale Value"]]

table2_df6 = table2_df5.pivot_table("Total Sale Value", ["transaction_items"], "Month", aggfunc="sum")

table2_df7 = table2_df6
table2_df8 = table2_df7.reset_index()
table2_df8.columns = ["Transaction_Items","January", "February", "March", "April", "May", "June"]
table2_df8["Total Sale Value"] = [77033298,89094000,8897850,47452610,116868720,11821794,29714500]
table2_df8

Total_Sale_Value = [77033298,89094000,8897850,47452610,116868720,11821794,29714500]
Labels = ["Beef Chicharon", "Gummy Vitamins", "Gummy Worms", "Kimchi and Seaweed", "Nutritional Milk", "Orange Beans", "Yummy Vegetables"]
Table2_TotalSaleValuePieChart = plt.pie(Total_Sale_Value, labels=Labels, autopct='%1.0f%%')
plt.title("Total Sale Value per Transactional Item from January to June")
