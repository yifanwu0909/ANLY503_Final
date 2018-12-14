df = pd.read_csv("pew.csv")
df = df[['q14', 'sex']]
df = df[df != 9].dropna(axis='rows')
df['q14'] = df['q14'].astype(int)
df['q14'] = df['q14'].astype(str)
l = []
for i in df['q14']:
    if i == '1':
        l.append('Mutual Happiness')
    elif i == '2':
        l.append('Bearing and Raising Children')
    elif i == '3':
        l.append("Both")
    elif i == '4':
        l.append('Neither')
df['Purpose_of_Marriage'] = l  

df_purpose = pd.DataFrame.from_dict(Counter(l), orient='index').reset_index()
df_purpose.columns = ['Purpose', 'Count']
df_purpose['Percent'] = 100 * df_purpose['Count'] / sum(df_purpose['Count'])
df_purpose
df_purpose.to_csv("r_plotly_purpose_of_marriage.csv")
