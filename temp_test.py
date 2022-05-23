import os

ficher = os.popen("./test")
res = ficher.read()
print(res)
