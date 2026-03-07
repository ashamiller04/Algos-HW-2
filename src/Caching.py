#Main file for reading input and writing output for the cache classes
from get_inputs import get_input
from FIFO import FIFO
from LRU import LRU
from OPTFF import OPTFF
import sys


#testing get_inputs
#print(get_input(f"{sys.argv[1]}_{sys.argv[2]}.in"))

def runCaching(k, m, requests):
    #return a tuple of the misses per cache type

    #creating Caches
    f_cache = FIFO(k)
    l_cache = LRU(k)
    ff_cache = OPTFF(k, requests)

    for i in requests:

        curr = int(i)
        curr_index = requests.index(i)

        if f_cache.get(curr) == -1:
            f_cache.miss()
        f_cache.put(curr, curr)

        if l_cache.get(curr) == -1:
            l_cache.miss()
        l_cache.put(curr, curr)


        if ff_cache.get(curr) == -1:
            ff_cache.miss()
        ff_cache.update(curr, curr, curr_index)

    #making miss tuple
    total_misses = (f_cache.misses, l_cache.misses, ff_cache.misses)

    return total_misses


#Creating Output file
def cachingOutput(k, m, requests):
    total_misses = runCaching(k, m, requests)
    with open(f"../data/{k}_{m}.out", 'w') as file:
        file.write(f"FIFO  : {total_misses[0]}\n")
        file.write(f"LRU   : {total_misses[1]}\n")
        file.write(f"OPTFF : {total_misses[2]}\n")


#runs program
cachingOutput(*get_input(f"{sys.argv[1]}_{sys.argv[2]}.in"))