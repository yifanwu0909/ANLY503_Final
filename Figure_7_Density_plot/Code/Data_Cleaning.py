df = pd.read_csv("pew.csv")
df = df[['q30f1', 'q31f2', 'sex']]
m = df[df['sex'] == 1][['sex', 'q31f2']]
f = df[df['sex'] == 2][['sex', 'q30f1']]
m = m.dropna(subset=["q31f2"])
m = m[m != 99].dropna(axis='rows')
f = f.dropna(subset=["q30f1"])
f = f[f != 99].dropna(axis='rows')
m.columns = ['sex', 'Ideal_Marriage_Age']
f.columns = ['sex', 'Ideal_Marriage_Age']

m.to_csv('m_ideal_m_age.csv')
f.to_csv('f_ideal_m_age.csv')

ideal_marriage_age = pd.concat([m, f])
ideal_marriage_age.to_csv('ideal_marriage_age.csv')
