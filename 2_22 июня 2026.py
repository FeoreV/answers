class Book:
    def __init__(self, title, author, publisher, pages):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages

    def show(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Издательство: {self.publisher}")
        print(f"Страниц: {self.pages}")
        print()


class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, book):
        new_node = Node(book)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def show_all(self):
        current = self.head
        while current is not None:
            current.book.show()
            current = current.next


class TreeNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class BookTree:
    def __init__(self):
        self.root = None

    def insert(self, book):
        if self.root is None:
            self.root = TreeNode(book)
        else:
            self._insert(self.root, book)

    def _insert(self, node, book):
        if book.title < node.book.title:
            if node.left is None:
                node.left = TreeNode(book)
            else:
                self._insert(node.left, book)
        else:
            if node.right is None:
                node.right = TreeNode(book)
            else:
                self._insert(node.right, book)

    def show_all(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            node.book.show()
            self._inorder(node.right)


b1 = Book("Мастер и Маргарита", "Булгаков М.А.", "АСТ", 480)
b2 = Book("Война и мир", "Толстой Л.Н.", "Эксмо", 1274)
b3 = Book("Преступление и наказание", "Достоевский Ф.М.", "АСТ", 608)
b4 = Book("Евгений Онегин", "Пушкин А.С.", "Просвещение", 224)
b5 = Book("Мёртвые души", "Гоголь Н.В.", "Эксмо", 352)

lst = LinkedList()
lst.add(b1)
lst.add(b2)
lst.add(b3)
lst.add(b4)
lst.add(b5)

print("=== Список ===")
lst.show_all()

tree = BookTree()
tree.insert(b1)
tree.insert(b2)
tree.insert(b3)
tree.insert(b4)
tree.insert(b5)

print("=== Дерево ===")
tree.show_all()
