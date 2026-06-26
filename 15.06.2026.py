class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: "Node | None" = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def add(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove(self, value: int) -> bool:
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def print_list(self) -> None:
        if self.head is None:
            print("Список пуст")
            return

        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))

    def find_by_value(self, value: int) -> int:
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def get_by_index(self, index: int) -> int:
        current = self.head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current.value
            current = current.next
            current_index += 1
        raise IndexError(f"Индекс {index} выходит за границы списка")


if __name__ == "__main__":
    lst = LinkedList()

    for value in [10, 25, 37, 42, 58, 63, 71]:
        lst.add(value)

    print("Исходный список:")
    lst.print_list()

    lst.add(99)
    print("\nПосле добавления 99:")
    lst.print_list()

    print("\nПоиск 42:", lst.find_by_value(42))
    print("Поиск 100:", lst.find_by_value(100))

    print("\nИндекс 0:", lst.get_by_index(0))
    print("Индекс 4:", lst.get_by_index(4))

    lst.remove(37)
    print("\nПосле удаления 37:")
    lst.print_list()

    lst.remove(10)
    print("\nПосле удаления 10:")
    lst.print_list()
