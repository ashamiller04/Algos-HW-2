#To Run: python generator.py [k] [m]
# k = cache capacity, m = number of requests

import random
import sys

#Validating Input
try:
    k = int(sys.argv[1])

except:
    print("Invalid Cache Capacity")
    quit()

if not (k>=1):
    print("Cache Capacity cannot be less than 1")
    quit()

try:
    m = int(sys.argv[2])

except:
    print("Invalid Number of Requests")
    quit()


#Initializing Request IDs
ID_list = random.choices(range(0, 100), k=m)

list_length = len(ID_list)

#Writing File
with open(f"{k}_{m}.in", 'w') as f:
    f.write(f"{k} {m}\n")
    for ID in ID_list:
        f.write(str(ID))
        if (list_length > 1):
            f.write(" ")
        list_length -= 1

#working! i think