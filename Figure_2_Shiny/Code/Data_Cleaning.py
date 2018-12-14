df_0 = pd.read_excel("birth_place.xlsx")
df = df_0.iloc[24:30]
df = df.T
total = df["Foreign born:"]
df["Never married"] = df["Never married"] / total
df["Now married, except separated"] = df["Now married, except separated"] / total
df["Divorced"] = df["Divorced"] / total
df["Separated"] = df["Separated"] / total
df["Widowed"] = df["Widowed"] / total
df.to_csv("Foreign.csv")

df = df_0.iloc[12:18]
df = df.T
total = df["Born in state of residence:"]
df["Never married"] = df["Never married"] / total
df["Now married, except separated"] = df["Now married, except separated"] / total
df["Divorced"] = df["Divorced"] / total
df["Separated"] = df["Separated"] / total
df["Widowed"] = df["Widowed"] / total
df.to_csv("Born Other state.csv")

df = df_0.iloc[18:24]
df = df.T
total = df["Native; born outside the United States:"]
df["Never married"] = df["Never married"] / total
df["Now married, except separated"] = df["Now married, except separated"] / total
df["Divorced"] = df["Divorced"] / total
df["Separated"] = df["Separated"] / total
df["Widowed"] = df["Widowed"] / total
df.to_csv("Native born outside of US.csv")

df = df_0.iloc[24:30]
df = df.T
total = df["Foreign born:"]
df["Never married"] = df["Never married"] / total
df["Now married, except separated"] = df["Now married, except separated"] / total
df["Divorced"] = df["Divorced"] / total
df["Separated"] = df["Separated"] / total
df["Widowed"] = df["Widowed"] / total
df.to_csv("Foreign.csv")

