import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})


graph_type = input("Tipo de grafico:")

if graph_type == 'scatter':
    df.plot(kind='scatter',x='num_children',y='num_pets',color='red')

if graph_type == 'bar':
    df.plot(kind='bar', x='name', y='age')

if graph_type == 'multiple':
    # get current axis
    ax = plt.gca()
    df_plot = df.plot(kind='line', x='name', y='num_children', ax=ax)
    df_plot.set_ylabel("Children/pets")
    df_plot = df.plot(kind='line', x='name', y='num_pets', color='red', ax=ax)
    
if graph_type == 'group':
    df.groupby('state')['name'].nunique().plot(kind='bar')

if graph_type == 'stacked':
    df.groupby(['state', 'gender']).size().unstack().plot(kind='bar', stacked=True)

if graph_type == 'stackedgender':
    df.groupby(['gender', 'state']).size().unstack().plot(kind='bar', stacked=True)

if graph_type == 'histogram':
    df[['age']].plot(kind='hist', bins=[0,20,40,60,80,100],rwidth=0.8)

plt.show()
