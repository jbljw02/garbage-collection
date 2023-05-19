
# '순환 참조' 구조를 가지는 함수
def circular_reference():

    # a 리스트와 b 리스트가 서로 참조
    a = [1]
    b = [a]
    a.append(b)
    return a, b

def main():
    while True:
        circular_reference()

main()
