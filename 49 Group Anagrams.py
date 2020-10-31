from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dic = {}
    for s in strs:
        key = tuple(sorted(s))
        if key in dic:
            dic[key].append(s)
        else:
            dic[key] = [s]
    return list(dic.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))