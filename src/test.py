import re
print(re.split(r"[,\s](?!\,)\s", "abc\,ccc,deds,\,\,dada"))