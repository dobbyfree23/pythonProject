'''
파일명: Ex20-1-Linked.py

연결 리스트(Linked List)
    저장된 각 데이터가 (데이터)+(다음 데이터의 포인터)로 이루어진 것으로
    한 방향으로만 탐색 가능한 구조
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)   # 새로운 노드 생성

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
