import json
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import re

%matplotlib inline

filename = "transaction-data-adhoc-analysis.json"
df = pd.read_json(filename)

table3_df = df[["name", "transaction_items", "transaction_date"]]
table3_df2 = table3_df.transaction_items.str.split(";")
table3_df2.index = table3_df.transaction_date
table3_df2 = table3_df2.reset_index("transaction_date")
table3_df3 = table3_df2.explode("transaction_items")
table3_df3["Name"] = table3_df["name"]
table3_df3["DATE"] = pd.to_datetime(df["transaction_date"])
table3_df3["Month"] = table3_df3["DATE"].dt.month

brands = ["Exotic Extras,", "HealthyKid 3+,", "Candy City,"] 
table3_df3["transaction_items"] = table3_df3["transaction_items"].str.replace("|".join(map(re.escape, brands)),"")

table3_df3["QTY"] = table3_df3["transaction_items"].str[-2]
table3_df3["QTY"] = table3_df3["QTY"].astype(int)

quantities = [",(x1)", ",(x2)", ",(x3)", ",(x4)"] 
table3_df3["transaction_items"] = table3_df3["transaction_items"].str.replace("|".join(map(re.escape, quantities)),"")

table3_df3 = table3_df3[["Name", "transaction_items","QTY", "Month"]]

table3_df4 = table3_df3.pivot_table("transaction_items", ["Name"], "Month", aggfunc="count")
table3_df4 = table3_df4.reset_index()
table3_df4.columns = ["Name", "1", "2", "3", "4", "5", "6"]
table3_df4["1"] = table3_df4["1"].fillna(0)
table3_df4["2"] = table3_df4["2"].fillna(0)
table3_df4["3"] = table3_df4["3"].fillna(0)
table3_df4["4"] = table3_df4["4"].fillna(0)
table3_df4["5"] = table3_df4["5"].fillna(0)
table3_df4["6"] = table3_df4["6"].fillna(0)
table3_df4["1"] = table3_df4["1"].astype(int)
table3_df4["2"] = table3_df4["2"].astype(int)
table3_df4["3"] = table3_df4["3"].astype(int)
table3_df4["4"] = table3_df4["4"].astype(int)
table3_df4["5"] = table3_df4["5"].astype(int)
table3_df4["6"] = table3_df4["6"].astype(int)
table3_df4["January"] = table3_df4["1"].astype(int)
table3_df4["February"] = table3_df4["2"].astype(int)
table3_df4["March"] = table3_df4["3"].astype(int)
table3_df4["April"] = table3_df4["4"].astype(int)
table3_df4["May"] = table3_df4["5"].astype(int)
table3_df4["June"] = table3_df4["6"].astype(int)

def myfunc1(January):
    if January > 0:
        answer1 = "Just Purchased"
    else:
        answer1 = "No Purchases"
    return answer1
def myfunc2(January, February):
    if January > 0 and February == 0:
        answer2 = "Inactive"
    elif January > 0 and February > 0: 
        answer2 = "Repeater"
    elif January == 0 and February > 0: 
        answer2 = "Just Purchased"
    else:
        answer2 = "No Purchases"
    return answer2

def myfunc3(January, February, March):
    if January > 0 and February > 0: 
        if March ==0:
            answer3 = "Inactive"
        else: 
            answer3 = "Engaged"
    elif January == 0 and February == 0 and March > 0: 
        answer3 = "Just Purchased"
    elif March > 0:
        if February > 0:
            answer3 = "Repeater" 
        else:
            answer3 = "Returnee"
    elif January > 0:
        if March == 0:
            answer3 = "Inactive" 
        else: 
            answer3 = "Repeater"
    elif February > 0:
        if March == 0:
            answer3 = "Inactive" 
        else: 
            answer3 = "Repeater"
    else: 
        answer3 = "No Purchases"
    return answer3

def myfunc4(January, February, March, April):
    if January > 0 and February > 0 and March > 0: 
        if April ==0:
            answer4 = "Inactive"
        else: 
            answer4 = "Engaged"
    elif January == 0 and February == 0 and March == 0 and April > 0: 
        answer4 = "Just Purchased"
    elif April > 0: 
        if March > 0:
            answer4 = "Repeater"
        else:
            answer4 = "Returnee"
    elif January > 0:
        if April == 0:
            answer4 = "Inactive" 
        else: 
            answer4 = "Repeater"
    elif February > 0:
        if April == 0:
            answer4 = "Inactive" 
        else: 
            answer4 = "Repeater"
    elif March > 0:
        if April == 0:
            answer4 = "Inactive" 
        else: 
            answer4 = "Repeater"
    else: 
        answer4 = "No Purchases"
    return answer4

def myfunc5(January, February, March, April, May):
    if January > 0 and February > 0 and March > 0 and April >0: 
        if May ==0:
            answer5 = "Inactive"
        else: 
            answer5 = "Engaged"
    elif January == 0 and February == 0 and March == 0 and April == 0 and May > 0: 
        answer5 = "Just Purchased"
    elif May > 0: 
        if April >0:
            answer5 = "Repeater" 
        else:
            answer5 = "Returnee"
    elif January > 0:
        if May == 0:
            answer5 = "Inactive" 
        else: 
            answer5 = "Repeater"
    elif February > 0:
        if May == 0:
            answer5 = "Inactive" 
        else: 
            answer5 = "Repeater"
    elif March > 0:
        if May == 0:
            answer5 = "Inactive" 
        else: 
            answer5 = "Repeater"
    elif April > 0:
        if May == 0:
            answer5 = "Inactive" 
        else: 
            answer5 = "Repeater"
    else: 
        answer5 = "No Purchases"
    return answer5
def myfunc6(January, February, March, April, May, June):
    if January > 0 and February > 0 and March > 0 and April >0 and May > 0: 
        if June ==0:
            answer6 = "Inactive"
        else: 
            answer6 = "Engaged"
    elif January == 0 and February == 0 and March == 0 and April == 0 and May == 0 and June >0: 
        answer6 = "Just Purchased"
    elif June > 0: 
        if May > 0:
            answer6 = "Repeater"
        else:
            answer6 = "Returnee"
    elif January > 0:
        if June == 0:
            answer6 = "Inactive" 
        else: 
            answer6 = "Repeater"
    elif February > 0:
        if June == 0:
            answer6 = "Inactive" 
        else: 
            answer6 = "Repeater"
    elif March > 0:
        if June == 0:
            answer6 = "Inactive" 
        else: 
            answer6 = "Repeater"
    elif April > 0:
        if June == 0:
            answer6 = "Inactive" 
        else: 
            answer6 = "Repeater"
    elif May > 0:
        if June == 0:
            answer6 = "Inactive" 
        else: 
            answer6 = "Repeater"
    else: 
        answer6 = "No Purchases"
    return answer6

table3_df4["M1_Status"] =table3_df4.apply(lambda x: myfunc1(x["January"]), axis=1)
table3_df4["M2_Status"] =table3_df4.apply(lambda x: myfunc2(x["January"], x["February"]), axis=1)
table3_df4["M3_Status"] =table3_df4.apply(lambda x: myfunc3(x["January"], x["February"], x["March"]), axis=1)
table3_df4["M4_Status"] =table3_df4.apply(lambda x: myfunc4(x["January"], x["February"], x["March"], x["April"]), axis=1)
table3_df4["M5_Status"] =table3_df4.apply(lambda x: myfunc5(x["January"], x["February"], x["March"], x["April"], x["May"]), axis=1)
table3_df4["M6_Status"] =table3_df4.apply(lambda x: myfunc6(x["January"], x["February"], x["March"], x["April"], x["May"], x["June"]), axis=1)

table3_df5 = table3_df4[["Name","January", "February", "March", "April", "May", "June", "M1_Status", "M2_Status", "M3_Status", "M4_Status", "M5_Status", "M6_Status"]]

M1_Engaged = table3_df4.M1_Status.str.count("Just Purchased").sum()
M1_NoHistory = table3_df4.M1_Status.str.count("No Purchases").sum()

M2_Repeater = table3_df4.M2_Status.str.count("Repeater").sum()
M2_Inactive = table3_df4.M2_Status.str.count("Inactive").sum()
M2_New = table3_df4.M2_Status.str.count("Just Purchased").sum()
M2_NoHistory = table3_df4.M2_Status.str.count("No Purchases").sum()

M3_Repeater = table3_df4.M3_Status.str.count("Repeater").sum()
M3_Inactive = table3_df4.M3_Status.str.count("Inactive").sum()
M3_Engaged = table3_df4.M3_Status.str.count("Engaged").sum()
M3_New = table3_df4.M3_Status.str.count("Just Purchased").sum()
M3_Returnee = table3_df4.M3_Status.str.count("Returnee").sum()
M3_NoHistory = table3_df4.M3_Status.str.count("No Purchases").sum()

M4_Repeater = table3_df4.M4_Status.str.count("Repeater").sum()
M4_Inactive = table3_df4.M4_Status.str.count("Inactive").sum()
M4_Engaged = table3_df4.M4_Status.str.count("Engaged").sum()
M4_New = table3_df4.M4_Status.str.count("Just Purchased").sum()
M4_Returnee = table3_df4.M4_Status.str.count("Returnee").sum()
M4_NoHistory = table3_df4.M4_Status.str.count("No Purchases").sum()

M5_Repeater = table3_df4.M5_Status.str.count("Repeater").sum()
M5_Inactive = table3_df4.M5_Status.str.count("Inactive").sum()
M5_Engaged = table3_df4.M5_Status.str.count("Engaged").sum()
M5_New = table3_df4.M5_Status.str.count("Just Purchased").sum()
M5_Returnee = table3_df4.M5_Status.str.count("Returnee").sum()
M5_NoHistory = table3_df4.M5_Status.str.count("No Purchases").sum()

M6_Repeater = table3_df4.M6_Status.str.count("Repeater").sum()
M6_Inactive = table3_df4.M6_Status.str.count("Inactive").sum()
M6_Engaged = table3_df4.M6_Status.str.count("Engaged").sum()
M6_New = table3_df4.M6_Status.str.count("Just Purchased").sum()
M6_Returnee = table3_df4.M6_Status.str.count("Returnee").sum()
M6_NoHistory = table3_df4.M6_Status.str.count("No Purchases").sum()

metric_values = [
    ["New Customers", M1_Engaged, M2_New, M3_New, M4_New, M5_New, M6_New],
    ["Repeater", 0, M2_Repeater, M3_Repeater, M4_Repeater, M5_Repeater, M6_Repeater],
    ["Engaged", M1_Engaged, M2_Repeater, M3_Engaged, M4_Engaged, M5_Engaged, M6_Engaged],
    ["Inactive", 0, M2_Inactive, M3_Inactive, M4_Inactive, M5_Inactive, M6_Inactive],
    ["Returnees", 0, 0, M3_Returnee, M4_Returnee, M5_Returnee, M6_Returnee],
    ["No First Purchases", M1_NoHistory, M2_NoHistory, M3_NoHistory, M4_NoHistory, M5_NoHistory, M6_NoHistory],
]
table3_df6 = pd.DataFrame(metric_values, columns=["Customer_Status", "January", "February", "March", "April", "May", "June"])

table3_df6