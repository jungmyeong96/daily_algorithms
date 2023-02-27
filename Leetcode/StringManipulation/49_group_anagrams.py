from typing import List
import collections

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    # sorted는 메모리를 더 사용하여 값을 list형태로 return
    # sort는 메모리를 더 사용하지 않고 자신의 메모리위치에 정렬
    return (list(anagrams.values()))

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))