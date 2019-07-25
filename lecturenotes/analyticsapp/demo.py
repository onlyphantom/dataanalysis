import pandas as pd

dat = pd.read_csv(
    "https://raw.githubusercontent.com/onlyphantom/dataanalysis/master/data_input/techcrunch.csv"
)

cond1 = dat["company"] == "Tesla Motors"
result = dat.loc[
    cond1, ["company", "round", "raisedCurrency", "raisedAmt"]
].sort_values(["round", "raisedAmt"])

print(result)
