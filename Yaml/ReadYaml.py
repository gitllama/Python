# -*- coding: utf-8 -*-

import yaml

f = open("database.yaml", "r")
dataMap = yaml.load(f)
f.close()

df dataMap.

#print(dataMap["data"]["cis"])
#print(dataMap["database"]["note"])

with open("data2.yaml", "w") as fw:
    fw.write(yaml.dump(dataMap, default_flow_style=False))
