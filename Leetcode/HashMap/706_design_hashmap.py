class MyHashMap:
#개별체이닝 방식으로 구현
#서브젝트에서는 키값이 정수형으로 들어오기 때문에 hash값의 구분이 다소 모호하게 생각될 수 있습니다.
#h(x) = x % m
#h(x)는 입력 키 x의 해수함수를 통한 결과
#x는 key
#m은 해시테이블 크기

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        #존재하지 않는 key 조회할 경우 default를 생성해주는 dict으로 에러방지


    #삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size #해시함수를 통한 인덱스 계산
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        #인덱스에 노드가 존재하는 경우 연결리스트처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)
    
    #조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        #노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        
    #삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        #인덱스의 첫번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        #연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
        

# 객체를 저장하기 위한 연결리스트 (개별 체이닝 구현 객체)
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)