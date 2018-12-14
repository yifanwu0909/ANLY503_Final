import pandas as pd
latlong = pd.read_csv('fips_latlong.csv')
latlong['long'] = [float(i[1:-1]) * (-1) for i in latlong['long']]
latlong['lat'] = [float(i[0:-1]) for i in latlong['lat']]
latlong['fips'] = latlong['fips'].astype(int)
df = pd.read_csv('mar_divc_county.csv', encoding='latin-1')
df = df[['GEO.id2', 'HC02_EST_VC01', 'HC04_EST_VC01', 'GEO.display-label']]
df = df[1:]
df.columns = ['fips', 'mar_rate', 'div_rate', 'county']
df['fips'] = df['fips'].astype(int)
df['mar_rate'] = df['mar_rate'].astype(float)
df['div_rate'] = df['div_rate'].astype(float)
df = df.merge(latlong, left_on ='fips', right_on = 'fips', how = 'inner')
df.columns = ['GEOID', 'mar_rate', 'div_rate', 'county', 'lat', 'long']
df.to_csv("leaflet_mar.csv")

df_div = df[df['div_rate'] > 16.0]
print(len(df_div))
df_div.to_csv("leaflet_div.csv")
