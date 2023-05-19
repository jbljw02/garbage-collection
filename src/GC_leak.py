class Node:
    def __init__(self, value):
        self.value = value
        # 현재 노드가 다음 노드를 참조하지 않게 하여 메모리 누수 방지를 의도
        self.next = None

# 순환 참조 구조를 이루는 함수 생성
def circular_reference():
    node1 = Node(1)
    node2 = Node(2)
    # node1과 node2가 서로 참조하고 있으므로 GC의 대상 X
    node1.next = node2
    node2.next = node1
    return node1, node2

def main():
    while True:
        circular_reference()

main()
