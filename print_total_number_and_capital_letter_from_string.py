import re
s='Vtu@123.e'
c=0
d=dict()
for i in s:
    if re.findall('[0-9]+',i):
        c=c+1
d["num"]=c
c=0
for i in s:
    if re.findall('[A-Z]+',i):
        c=c+1
d["ALPHA"]=c
print(d)
