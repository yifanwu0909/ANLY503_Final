import pandas as pd
df = pd.read_csv("psam_pusb.csv")
df = df.sample(frac=0.05)
df = df.dropna(subset=["PINCP"])
df = df[df["PINCP"] != 0.0]
df_income = df[["PINCP", "MAR"]]
df_income.to_csv("income_marriage300.csv")


