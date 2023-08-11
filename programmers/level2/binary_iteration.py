def solution(s):
    answer = []
    del_zero_count = 0
    lot_count = 0
    while int(s, 2) != 1:
        before_len = len(s)
        s = s.replace('0', '')
        after_len = len(s)
        del_zero_count += before_len - after_len
        lot_count += 1
        if after_len == 1:
            break
        s = bin(after_len).replace('0b', '')
        
    answer = [lot_count, del_zero_count]
    return answer