import pandas as pd
import dask
dask.config.set({'dataframe.query-planning': True})

import dask.dataframe as da

data = pd.read_csv("mixdata.csv" , encoding='cp1252')



print(data.info())
data.drop(data.columns[0],axis=1)
size128MB = int(data.memory_usage().sum()/data.count()[0]) 
print(data.count()[0]) 
print("size128MB")
print(size128MB)
noofchunk = int((128 * 1e6 / size128MB))
print(noofchunk)

ddf = da.from_pandas(data,chunksize=noofchunk) #chunksize is no of row
ddf.to_parquet("demo3")
