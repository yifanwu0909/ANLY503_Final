df = pd.read_csv('divorce_state.csv')
df = df.sort_values(by=['divorce_rate'])

color = ["#FFFFCC"] * 10 + ["#FFEDA0"] * 10 + ["#FED976"] * 2 + ["#FEB24C"] * 2 + ["#FD8D3C"] * 2  + ["#FC4E2A"] * 2 + ["#E31A1C"] * 8  + ["#BD0026"] * 8 + ["gray0"] * 8
df['color'] = color

df.to_csv('divorce_state_cleaned.csv')
