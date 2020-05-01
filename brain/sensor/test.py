import json   
   
with open("data.json","r+") as f:
    x = json.load(f)

for i in x:
    if(i["sensor"]=='motion'):
        i["value"] = "ha"


with open("data.json","w") as f:
    json.dump(x, f, ensure_ascii=False, indent=4)

print(x)