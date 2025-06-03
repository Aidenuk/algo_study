# Hashtable = Fast insertion, look up, deletion of key/value pairs
#             Not ideal for small data sets, great with large data sets
      
# Hashing   = Takes a key and computes an integer (formula will vary based on key & data type) 
#             In a Hashtable, we use the hash % capacity to calculate an index number
#             key.hashCode() % capacity = IndexError

# Bucket    = an indexed storage location for one or more Entries
#             can store multiple Entries in case of collision (linked similarly a LinkedList)

# collision = hash function generates the same index for more than one key 
#             less collisions = more efficiency

# Runtime complexity = Best Case O(1) -> if no collisions
#                      Worst Case O(n) -> when there is a lot collisions

# L = ["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict


def groupAnograms(L):
    anogram_map = defaultdict(list)
    result = []
    for e in L:
        sorted_e = tuple(sorted(e))
        anogram_map[sorted_e].append(e)
    for res in anogram_map.values():
        result.append(res)
    
    print(result)


groupAnograms(["eat", "tea", "tan", "ate", "nat", "bat"])


#in terms of memory O(n)
#in terms of time complexity O(1)


hashset = {}
hashset[100] = "bob"
hashset[102] = "Alex"
hashset[103] = "Ted"


# hashset.pop(102)

for value in hashset:
    print(f'key: {value} - value: {hashset[value]}')
