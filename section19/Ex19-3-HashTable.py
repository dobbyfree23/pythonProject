'''
파일명: Ex19-3-HashTable.py

해시테이블(Hash Table)
    해시테이블은 키와 값을 저장하는 데이터 구조로,
    요소를 빠르고 효율적인 검색, 삽입, 삭제를 허용한다.
    해시 함수는 키를 입력으로 받아 값을 저장하거나
    검색할 수 있는 배열 인덱스를 반환한다.
'''

class HashTable:

    def __init__(self, size):
        self.size = size
        #  self.hash_table = [None, None, None, None, None, None, None, None, None, None]
        self.hash_table = [None] * self.size

    def has_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        '''
         size = 10
         key = 'John Doe', value='555-555-5555'

         hash_index = 7
         hash_table = [None, None, None, None, None, None, None, [('John Doe', value='555-555-5555')], None, None]
        '''

        hash_index = self.has_function(key)

        if self.hash_table[hash_index] is None:
            self.hash_table[hash_index] = []

        self.hash_table[hash_index].append((key, value))

    def search(self, key):
        print(self.hash_table)
        '''
        [None, None, [('Jane Doe', '555-555-5556')], None, [('Jim Doe', '555-555-5557')], None, [('김태호', '555-555-5558')], None, [('John Doe', '555-555-5555')], None]
        key = 'John Doe'
        hash_index = 8
        bucket = [('John Doe', '555-555-5555')]
        '''
        hash_index = self.has_function(key)
        bucket = self.hash_table[hash_index]
        if bucket is None:
            return None

        for k, v in bucket: # 튜플의 값을 언패킹으로 k, v 로 받는다
            print(k, v)
            if k == key:
                return v

        return None


# 실행코드
hash_table = HashTable(10)  # 크기가 10인 hashtable 생성
hash_table.insert('John Doe', '555-555-5555')
hash_table.insert('Jane Doe', '555-555-5556')
hash_table.insert('Jim Doe', '555-555-5557')
hash_table.insert('김태호', '555-555-5558')

print(hash_table.search('John Doe'))














