fpath = "2020-05-01-PMATH347.md"
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
    - /{}/{}
""".format(sub, num, sub, num, subl, num, subl, num)
contents.insert(6, value)

f = open(fpath, "w")
contents = "".join(contents)
f.write(contents)
f.close()
