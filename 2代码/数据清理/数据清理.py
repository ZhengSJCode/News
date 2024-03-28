import pandas as pd
import numpy as np


df=pd.read_csv('data.csv',encoding='utf-8',index_col=['freshTime'],low_memory=False,dtype=float)
# print(df.head)


# x=df.groupby('freshTime').mean()
positive_prob_DateMean=df.groupby('freshTime')['positive_prob'].mean()
# confidence_DateMean=df.groupby('freshTime')['confidence'].mean()
# negative_prob=df.groupby('freshTime')['negative_prob'].mean()
# sentiment_DateMean=df.groupby('freshTime')['sentiment'].mean()

# y=df.groupby('freshTime')['id'].count()
# c=pd.concat([x,y],axis=1)


# c.to_csv('Result.csv')

print(positive_prob_DateMean)



