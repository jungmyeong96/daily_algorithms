from collections import defaultdict
from collections import Counter

def numJewelsInStones(jewels: str, stones: str) -> int:
    #1.해시테이블을 이용함
    # jeweler = {}
    # count = 0

    # for stone in stones:
    #     if stone not in jeweler:
    #         jeweler[stone] = 1
    #     else:
    #         jeweler[stone] += 1
    
    # for jewel in jewels:
    #     if jewel in jeweler:
    #         count += jeweler[jewel]
    
    # return count


    #2. defaultdict을 이용한 비교
    # jeweler = defaultdict(int)
    # count = 0

    # for stone in stones:
    #     jeweler[stone] += 1
    
    # for jewel in jewels:
    #     count += jeweler[jewel]
    
    # return count

    #3. counter를 사용하여 갯수 파악
    # jeweler = Counter(stones)
    # count = 0
    
    # for jewel in jewels:
    #     count += jeweler[jewel]
    
    # return count

    #4. 리스트 컴프리핸션을 이용한 방식
    return sum([stone in jewels for stone in stones])

print(numJewelsInStones("aA", "aAAbbbb"))