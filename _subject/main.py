import os
import json 

with open('../_data/crs.json') as f:
    data = json.load(f)

def get_full(s):
    for i in data:
        if i['code'].lower() == s:
            return i['name']
    return "N/A"


for filename in os.listdir('.'):
    if 'main' in filename:
        continue
    with open(filename, "r", encoding="utf8") as in_file:
        buf = in_file.readlines()
    base = os.path.splitext(filename)[0]
    # arr = base.split('-')
    # add = '/'+ arr[0][-2:] + '-' + arr[1] + "/" + arr[3].replace('old', '').upper() +"/"
    print(base, get_full(base))
    
    
    with open(filename, "w", encoding="utf8") as out_file:
        for line in buf:
            if "title: " in line:
                line = "title: " + get_full(base) + "\n"
            out_file.write(line)
    

    