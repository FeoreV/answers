class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop из пустого стека")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek из пустого стека")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def print_stack(self):
        if self.is_empty():
            print("Стек пуст")
        else:
            print("Стек:", " | ".join(str(x) for x in reversed(self._data)))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value):
        node = Node(value)
        if self._tail is not None:
            self._tail.next = node
        self._tail = node
        if self._head is None:
            self._head = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek из пустой очереди")
        return self._head.value

    def is_empty(self):
        return self._size == 0

    def print_queue(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        elements = []
        current = self._head
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print("Очередь:", " -> ".join(elements))


if __name__ == "__main__":
    print("СТЕК")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.print_stack()
    print("peek:", s.peek())
    print("pop:", s.pop())
    s.print_stack()

    print("\nОЧЕРЕДЬ")
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.print_queue()
    print("peek:", q.peek())
    print("dequeue:", q.dequeue())
    q.print_queue()
