import json
import pandas.io.json as pd_json

with open("data.json", "r") as f:
    data = pd_json.loads(f.read())
    module_obj = pd_json._normalize
    # print(help(module_obj))
    df = pd_json._normalize.json_normalize((data,record_path:="records"))
    print(df.head(2))


