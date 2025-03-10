<h2>1. Garbage Collection(쓰레기 수집)이란?</h2>

<p>Garbage Collection은 프로그래밍 언어에서 메모리 관리를 자동화하는 기술입니다. 이 기법은 동적 할당된 메모리 영역 가운데 '더 이상 사용할 수 없게 된 영역'을 
탐지하여 자동으로 해제해줍니다. '더 이상 사용할 수 없게 된 영역'이란 어떤 변수도 가리키지 않게 된 영역을 의미합니다. </p>
<p>그러나 Garbage Collection은 몇 가지 위험성을 지니고 있습니다.</p>

<h3>Garbage Collection의 단점</h3>
<b>1. 자원 소비</b>
<p>Garbage Collector는 CPU 및 메모리 등의 자원을 소비합니다. Garbage Collection이 실행될 때마다 특정 자원이 할당되므로 이는 프로그램의 성능에 영향을 미칠 수 있습니다.</p>
<b>2. 실행 시간에 대한 비용</b>
<p>Garbage Collector는 실행되는 동안 프로그램에 추가적인 부담을 줄 수 있습니다. GC는 수행 중에 프로그램의 실행이 잠시 멈추는 'Stop-the-World' 방식을 사용하므로 프로그램의 잠시 중단될 수도 있습니다. 이러한 중단은 규모가 큰 프로그램에는 큰 문제를 초래할 수 있습니다.</p>
<b>3. 실행 타이밍 예측의 어려움</b>
<p>Garbage Collector는 주기적으로 필요한 상황에 스스로 동작하므로, 정확히 언제 실행될지 예측하기가 어렵습니다. 따라서 불규칙적인 Garbage Collection으로 인하여 프로그램의 실행 시간과 메모리 사용량을 예측하는 것이 어려워질 수 있습니다.</p>

<br>

<h2>2. Garbage Collection의 필요성</h2>

<p>하지만 위 단점들에도 불구하고, Garbage Collection은 사용자에게 여러 이점들을 제공해주기 때문에 대부분의 프로그래밍 언어에 필수적인 기능입니다.</p>

<h3>Garbage의 Collection의 장점</h3>
<b>1. 메모리 누수 방지</b>
<p><b>Garbage Collector는 더 이상 사용되지 않는 객체를 식별하여 자동적으로 메모리를 해제해줌으로써 메모리 누수를 방지합니다.</b> '메모리 누수'란 프로그램에서 사용하지 않는 메모리가 지속적으로 쌓이는 현상으로, 적절히 관리되지 않는다면 시스템의 성능에 부정적인 영향을 끼칠 수 있습니다.</p>
<b>2. 개발의 생산성 증대</b>
<p><b>Garbage Collector을 통해 개발자는 메모리 할당과 해제에 관여할 필요없이 개발에만 집중할 수 있게 됩니다.</b> 개발자가 메모리 할당 및 해제를 명시적으로 처리하면 실수가 발생할 확률이 높으며, 이로 인해 메모리에 관한 문제가 발생할 수 있습니다. 그러나 Garbage Collection을 통해 개발자는 메모리 관리에 대한 부담을 상대적으로 내려놓을 수 있게 되어 개발의 생산성을 향상시킬 수 있습니다.</p>
<b>3. 동적 메모리 관리</b>
<p><b>Garbage Collector는 동적 할당된 메모리의 사용을 지속적으로 추적하고 관리합니다.</b> 이는 프로그램 실행 중에도 메모리의 할당과 해제를 동적으로 처리할 수 있음을 의미합니다. Garbage Collector는 메모리의 사용량을 실시간으로 최적화하고, 메모리의 할당 및 해제로 인한 프로그램의 버그를 최소화합니다.</p>

<p>결과적으로 Garbage Collection으로 인해 개발자는 메모리 관리에 신경을 쓸 필요가 없어지므로 더욱 안전하고 생산적으로 코드를 작성할 수 있게 됩니다. 이는 프로그램의 개발과 유지보수가 더욱 간편해지는 효과를 가져올 수 있습니다.</p>

<br>

<h2>3. Garbage Collection의 동작 원리</h2>
<b>1. 도달 가능한 객체 식별</b>
<p>Garbage Collector는 프로그램에서 사용중인 객체들 중 접근이 가능한 객체를 찾습니다. '도달 가능한 객체'란 프로그램에서 직간접적으로 참조되고 있는 객체를 의미합니다.</p>
<b>2. 도달 가능한 객체와 그렇지 않은 객체 구분</b>
<p>Garbage Collector는 도달 가능한 객체를 식별하고, 해당 객체를 그렇지 않은 객체와 구분합니다. 도달 가능한 객체는 메모리에서 해제되지 않도록 표시합니다.</p>
<b>3. 도달 불가한 객체 청소</b>
<p>Garbage Collector는 도달 불가능한 객체를 메모리에서 제거합니다. 이를 통해 메모리의 공간을 더 확보할 수 있게 됩니다.</p>

<br>

<h2>4. Garbage Collection이 제대로 동작하려면?</h2>

```python
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
```

<p>위 예제에서는 'Person' 클래스를 정의하고 'remove_unusedObjects()' 함수를 이용하여 불필요한 객체 참조를 제거합니다. removed_unusedObjects() 함수 내에서는 person 객체를 생성했지만 실제로는 사용되지 않았으므로 참조를 해제한 것입니다. 이와 같이 불필요한 참조를 제거하면 Garbage Collector는 해당 객체를 도달 불가능한 것으로 판단하고 메모리에서 해제합니다.</p>

<br>

<h2>5. Garbage Collection에도 불구하고 메모리 누수가 발생하는 경우</h2>

```python
# 순환 참조 구조를 가지는 함수
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
```

<p>위 예제에서는 '순환 참조'로 인하여 메모리 누수가 발생합니다. 순환 참조란 서로 다른 요소들이 서로를 참조하는 현상을 말합니다. 위 코드에서는 "self.next = None"을 통해 현재 노드가 다음 노드를 참조하지 않게 했음에도 불구하고 'circular_reference()' 함수에서 'node1'과 'node2'가 서로를 참조하는 순환 참조가 발생합니다. Garbage Collector는 순환 참조된 객체들을 임의로 해제할 수 없으므로 메모리 누수가 발생하게 됩니다. 이러한 경우에는, 사용하지 않는 객체에 대하여 개발자가 명시적으로 참조를 해제 해줘야 합니다.</p>
