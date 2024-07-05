from add_two_numbers import Solution, ListNode

# Helper function to create a linked list from a list of numbers
def create_linked_list(elements):
    dummy_root = ListNode(0)
    ptr = dummy_root
    for element in elements:
        ptr.next = ListNode(element)
        ptr = ptr.next
    ptr = dummy_root.next
    return ptr

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Test cases
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

# Instantiate the Solution class
solution = Solution()

# Call the addTwoNumbers method and print the result
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)