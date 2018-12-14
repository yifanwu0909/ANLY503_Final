import pandas as pd
import networkx as nx
import numpy as np

df = pd.read_csv("pew.csv")
df = df[["q15a", "q15b", "q15c", "q15d", "q15e", "q15f", "q15g", "q15h", "q15i"]]
df.columns = ["Faithfulness", 
              "An adequate income", 
              "Shared religious beliefs", 
              "Housing", 
              "Political View", 
              "Sexual relationship", 
              "Sharing household chores", 
              "Children", 
              "Tastes and interests"]
df = df[df != 9].dropna(axis='rows')
G = nx.Graph()
for index, row in df.iterrows():
    df_i = row.to_frame()
    df_i.columns = ['A']
    df_i['A'] = df_i['A'].astype(str)
    df_i = pd.get_dummies(df_i, prefix='A')
    df_i.reset_index(level=0, inplace=True)
    if 'A_1.0' in df_i:
        df_i = df_i[df_i['A_1.0'] == 1]
        print(df_i)    
        G.add_nodes_from(df_i['index'].values)
        l = list(df_i)
        del l[0]
        #print(l)
        for i, group in df_i.groupby(l)['index']:
            for u, v in itertools.combinations(group, 2):  
                #print(u, v)
                if G.has_edge(u, v):
                    G[u][v]['weight'] += 1
                else:
                    G.add_edge(u, v, weight = 1)
#len(df)

edge = pd.DataFrame(columns=['Source', 'Target', 'Value'])
for line in nx.generate_edgelist(G, delimiter=',', data=True):
    #print(line)
    new_row = [line.split(',')[0], line.split(',')[1], int(line.split(':')[1].split('}')[0][1:])]
    df_append = pd.DataFrame([new_row], columns=['Source', 'Target', 'Value'])
    #print(df_append)
    edge = pd.concat([edge, df_append])
    
nx.write_edgelist(G, 'test2.edgelist', delimiter=',', data=True)
edge = edge[edge["Value"] >= 800]
edge.to_csv("edge.csv")    
