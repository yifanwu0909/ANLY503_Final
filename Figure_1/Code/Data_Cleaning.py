import pandas as pd

df16 = pd.read_csv("regional_16.csv")
df15 = pd.read_csv("regional_15.csv")
df14 = pd.read_csv("regional_14.csv")
df13 = pd.read_csv("regional_13.csv")
df12 = pd.read_csv("regional_12.csv")
df11 = pd.read_csv("regional_11.csv")
df10 = pd.read_csv("regional_10.csv")
df09 = pd.read_csv("regional_09.csv")

#male married
l = [list(df16["HC02_EST_VC03"])[-4:]]
l.append(list(df15["HC02_EST_VC03"])[-4:])
l.append(list(df14["HC02_EST_VC03"])[-4:])
l.append(list(df13["HC02_EST_VC03"])[-4:])
l.append(list(df12["HC02_EST_VC03"])[-4:])
l.append(list(df11["HC02_EST_VC03"])[-4:])
l.append(list(df10["HC02_EST_VC03"])[-4:])
l.append(list(df09["HC02_EST_VC03"])[-4:])
male_married_list = l.copy()
male_married = pd.DataFrame(male_married_list, columns=['NE','MW', 'S', 'W'])
male_married['year'] = range(2009, 2017)[::-1]
male_married = male_married.sort_values(by=['year'])
#male_married = pd.melt(male_married, id_vars = ['year'])
male_married.to_csv("male_married.csv")

#female married
l = [list(df16["HC02_EST_VC10"])[-4:]]
l.append(list(df15["HC02_EST_VC10"])[-4:])
l.append(list(df14["HC02_EST_VC10"])[-4:])
l.append(list(df13["HC02_EST_VC10"])[-4:])
l.append(list(df12["HC02_EST_VC10"])[-4:])
l.append(list(df11["HC02_EST_VC10"])[-4:])
l.append(list(df10["HC02_EST_VC10"])[-4:])
l.append(list(df09["HC02_EST_VC10"])[-4:])
female_married_list = l.copy()
female_married = pd.DataFrame(female_married_list, columns=['NE','MW', 'S', 'W'])
female_married['year'] = range(2009, 2017)[::-1]
female_married = female_married.sort_values(by=['year'])
female_married.to_csv("female_married.csv")
