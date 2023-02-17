import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase ="APS"

# Collection  Name
collection = "Sensor"

data_file="/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__":
    df=pd.read_csv(data_file)
    print("rows and columns : ",df.shape)

#convert data into json format to dump it into mongodb
df.reset_index(drop = True,inplace=True) #dropping the row index
json_data = list(json.loads(df.T.to_json()).values())

#inserting json data to mongodb
client[dataBase][collection].insert_many(json_data)




