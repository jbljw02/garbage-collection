class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Person(name={self.name})"

# 불필요한 객체 참조를 제거하는 함수
def remove_unusedObjects():

    person = Person("Chilwell")

    # person을 사용한 후, 더 이상 필요하지 않은 경우 참조를 None으로 설정합니다.
    person = None

# remove_unused_objects() 함수를 호출하여 불필요한 객체 참조를 제거합니다.
remove_unusedObjects()