import glob
all = glob.glob("*.md")

for fpath in all:
    #fpath = "2020-05-01-PMATH347.md"
    f = open(fpath, "r")
    contents = f.readlines()
    f.close()

    line3 = contents[2].split()
    sub = line3[1]
    subl = sub.lower()
    num = line3[2]

    value = """redirect_from:
    - /{}/{}
    - /{}/{}/
    - /{}/{}
    - /{}/{}/\n""".format(sub, num, sub, num, subl, num, subl, num)
    if "redirect_from" not in contents[6]:
        continue
    #contents.insert(6, value)
    ten = contents[10].rstrip('\n') + '/\n'
    contents[10] = ten

    f = open(fpath, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
