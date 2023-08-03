import collections
# doubly linked list implementation of linked lists
linked_list = collections.deque([])

linked_list.append(10)
linked_list.append("Adam")
linked_list.append(False)

linked_list.appendleft("This is new item")

print(linked_list)
#pop returns and removes let most item

print(linked_list.pop())
print(linked_list.popleft())

print(linked_list[1])