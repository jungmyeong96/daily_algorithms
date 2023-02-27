from typing import List
import collections

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    
    return (list(anagrams.values()))

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))