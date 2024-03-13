class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Додає новий вузол до кінця списку."""
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_list(self):
        """Друкує весь список."""
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def reverse(self):
        """Реверсує список."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        """Сортує список використовуючи сортування злиттям."""
        self.head = self._sort_list(self.head)

    def _sort_list(self, head):
        if head is None or head.next is None:
            return head
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self._sort_list(head)
        right = self._sort_list(next_to_middle)
        sorted_list = self._merge_sorted_lists(left, right)
        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge_sorted_lists(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a
        if a.value <= b.value:
            result = a
            result.next = self._merge_sorted_lists(a.next, b)
        else:
            result = b
            result.next = self._merge_sorted_lists(a, b.next)
        return result

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Об'єднує два відсортовані списки в один відсортований."""
        dummy = current = Node(0)
        while list1 and list2:
            if list1.value < list2.value:
                current.next, list1 = list1, list1.next
            else:
                current.next, list2 = list2, list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next


def main():
    # Створення списків
    list1 = LinkedList()
    list2 = LinkedList()

    for value in [3, 2, 1]:
        list1.append(value)

    for value in [6, 5, 4]:
        list2.append(value)

    # Реверсування списку
    list1.reverse()
    print("Reversed list:")
    list1.print_list()  # Виведе: 1 2 3

    # Сортування списку
    list2.sort()
    print("Sorted list:")
    list2.print_list()  # Виведе: 4 5 6

    # Об'єднання двох відсортованих списків
    merged_list_head = LinkedList.merge_sorted_lists(list1.head, list2.head)
    merged_list = LinkedList()
    merged_list.head = merged_list_head
    print("Merged list:")
    merged_list.print_list()  # Виведе: 1 2 3 4 5 6


if __name__ == "__main__":
    main()
