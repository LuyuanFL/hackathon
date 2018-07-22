import sys
import re
import numpy as np
line2=''
f = open(r"C:\\Users\iucn\Desktop\lesson.txt")
lines = f.read()
result = str(re.findall("(\d\d:\d\d+)", lines))
result2 = re.findall("(\d\d+)", result)
a = np.array(result2)
if(len(a)>27):
    for q in range(len(a)-27):
        a = np.array(result2)
if (len(a)<27):
    for q in range(27-len(a)):
        a.append(0);
b=a.reshape(7,4)
print(b)

