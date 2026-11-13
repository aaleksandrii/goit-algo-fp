class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: "Node | None" = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def append(self, data: int) -> None:
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node


    def display_list(self) -> list[int]:
        result: list[int] = []
        current = self.head

        if current is None:
            return result

        while current is not None:
            result.append(current.data)
            current = current.next

        return result


    def __str__(self) -> str:
        if self.head is None:
            return "List is empty"
        return " -> ".join(str(x) for x in self.display_list())


def reverse(linked_list: LinkedList) -> LinkedList:
    current = linked_list.head
    prev: Node | None = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linked_list.head = prev

    return linked_list


def insertion_sort(linked_list: LinkedList) -> LinkedList:
    current = linked_list.head
    sorted_linked_list_head: Node | None = None

    while current:
        next_node = current.next

        if sorted_linked_list_head is None or sorted_linked_list_head.data >= current.data:
            current.next = sorted_linked_list_head
            sorted_linked_list_head = current
        else:
            temp = sorted_linked_list_head
            while temp.next and temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current

        current = next_node

    linked_list.head = sorted_linked_list_head
    return linked_list


def merge(left_linked_list: LinkedList, right_linked_list: LinkedList) -> LinkedList:
    node = Node(0)
    tail = node

    left = left_linked_list.head
    right = right_linked_list.head

    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right

    result_linked_list = LinkedList()
    result_linked_list.head = node.next
    return result_linked_list


def generate_linked_list(dataset: list[int]) -> LinkedList:
    linked_list = LinkedList()
    
    for i in dataset:
        linked_list.append(i)

    return linked_list


if __name__ == "__main__":
    dataset1 = [4, 1, 5, 9, 5, 8]
    dataset2 = [9, 3, 5, 1, 4, 0]


    reversed_linked_list = generate_linked_list(dataset1)
    print("Reversed linked list")
    print(f"  initial linked list: {reversed_linked_list}")

    reverse(reversed_linked_list)
    print(f"  reversed linked list: {reversed_linked_list}")
    print()


    insertion_linked_list = generate_linked_list(dataset1)
    print("Insertion linked list")
    print(f"  initial linked list: {insertion_linked_list}")

    insertion_sort(insertion_linked_list)
    print(f"  insertion sorted linked list: {insertion_linked_list}")
    print()


    merge_linked_list_left = insertion_sort(generate_linked_list(dataset1))
    merge_linked_list_right = insertion_sort(generate_linked_list(dataset2))
    print("Merge linked list")
    print(f"  initial linked list left: {merge_linked_list_left}")
    print(f"  initial linked list right: {merge_linked_list_right}")

    merged_linked_list = merge(merge_linked_list_left, merge_linked_list_right)
    print(f"  merged linked list: {merged_linked_list}")
    print()
