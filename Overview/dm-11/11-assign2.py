import numpy as np
import pandas as pd
from IPython.display import display

csv_in = "sushi_corr-min4.csv"
min_common_items = 4

pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

df = pd.read_csv(csv_in, delimiter=",", skiprows=0, header=0)
df.index = df.columns


def predict_scores(df_sim, ser_target):
    ret = {}
    for item1 in df_sim.index:
        v1 = df_sim.loc[item1]
        if v1.notnull().sum() < min_common_items:
            continue
        v11 = v1[v1.notnull()]
        t11 = ser_target[v1.notnull()]
        pred1 = (v11 * t11).sum() / np.abs(v11).sum()
        ret[item1] = pred1

    ser_ret = pd.Series(ret)

    return ser_ret.sort_values(ascending=False)


def get_recomm_by_item_sim(df, target_dic):
    ser_target = pd.Series(target_dic)
    df_scores = df[ser_target.index]
    df_scores = df_scores.drop(index=ser_target.index)
    recomm = predict_scores(df_scores, ser_target)

    return recomm


print("Available sushi items (toppings):")
print(list(df.columns))
item_dic = {}
while True:
    item1 = input("Sushi item (topping):")
    if item1 == "":
        break
    elif item1 not in df.columns:
        print("Sorry, item", item1, "is not available")
        continue
    try:
        rate1 = int(input("Rating for the item:"))
        if rate1 < 1 or rate1 > 10:
            raise (exception)
    except:
        print("Sorry, rating should be 1..9")
        continue

    item_dic[item1] = rate1

print("Input:")
print(item_dic)
print("Recommendation:")
recomm = get_recomm_by_item_sim(df, item_dic)
print(recomm.head())
