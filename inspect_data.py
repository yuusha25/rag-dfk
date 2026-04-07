import json
import sys
import glob
import os

res = []
for file in glob.glob("dataset/*.json"):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        if len(data) > 0:
            sample = {k:v for k,v in data[0].items() if k != "embedding"}
            res.append({"file": os.path.basename(file), "keys": list(data[0].keys()), "sample": sample})

with open("dataset_schemas.json", "w", encoding="utf-8") as out:
    json.dump(res, out, indent=2)
