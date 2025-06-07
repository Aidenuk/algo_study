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




