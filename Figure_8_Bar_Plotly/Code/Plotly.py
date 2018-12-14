import plotly.plotly as py
import plotly
from plotly import tools
plotly.tools.set_credentials_file(username='WuYifan', api_key='u2QEq8fd0TTozYHjLzXQ')
#percent of saying very important:
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("pew.csv")
df = df[['marital', "q15a", "q15b", "q15c", "q15d", "q15e", "q15f", "q15g", "q15h", "q15i"]]
colname = ["Faithfulness", "Income", "Same religious", "Good housing", 
           "Political View", "Sexual Relationship", "Shareing Chores", "Children", 
           "Tastes and interests"]
df = df.dropna(axis='rows')
y = df[df['marital'] == 1]
n = df[df['marital'] == 6]

y_percent = []
for i in list(y)[1:]:
    y_percent_i = y[i].value_counts()[1] / len(y)
    y_percent.append(y_percent_i)

n_percent = []
for i in list(y)[1:]:
    n_percent_i = n[i].value_counts()[1] / len(n)
    n_percent.append(n_percent_i)
    

gray = 'rgb(224,224,224)'
blue = 'rgb(116,173,209)'
org = 'rgb(253,174,97)'

cub_trace = go.Bar(
    y = y_percent,
    x=colname,
    name='Now Married',
    orientation = 'v',
    marker={'color': [blue] * 9}
)
libpp_trace = go.Bar(
    y = n_percent,
    x=colname,
    name='Never Married',
    orientation = 'v',
    marker={'color': [org] * 9}
)
data = [cub_trace, libpp_trace]
grouped_layout = go.Layout(barmode='group', title ='Percent of People Rating "Very Important" in Various Factors in Marriage')

fig_cond = go.Figure(data = data, layout = grouped_layout)
py.iplot(fig_cond, filename='grouped bar')
