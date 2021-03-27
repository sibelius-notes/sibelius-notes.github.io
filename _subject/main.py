import os

for filename in os.listdir('.'):
    if 'main' in filename:
        continue
    with open(filename, "r", encoding="utf8") as in_file:
        buf = in_file.readlines()
    base = os.path.splitext(filename)[0]
    # arr = base.split('-')
    # add = '/'+ arr[0][-2:] + '-' + arr[1] + "/" + arr[3].replace('old', '').upper() +"/"
    print(base)
    add = "/subject/" + base + "/"
    

    with open(filename, "w", encoding="utf8") as out_file:
        for line in buf:
            if line == "redirect_from:\n":
                line = line + "    - " + add + "\n"
            out_file.write(line)
    

    