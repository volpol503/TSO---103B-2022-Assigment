from typing import Any
class ListNode:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next

  def __repr__(self):
    return f"Элемент ListNode со значением {self.val}"

def add_to_the_end(head: ListNode, add_val: Any) -> None:
  pointer = head
  while pointer.next:
    pointer = pointer.next
  pointer.next = ListNode(add_val)
  
h = ListNode(1)
add_to_the_end(h,'cat')
add_to_the_end(h,'bird')
print(h)
print(h.next)
print(h.next.next)
print(h.next.next.next)

def add_to_the_front(head: ListNode, add_val: Any) ->    ListNode:
    node = ListNode(add_val)
    node.next = head
    return node

h = add_to_the_front(h,0)

print(h)
print(h.next)
add_to_the_end(h,'horse')
print(h.next.next)

def find_mid(head: ListNode) -> ListNode:
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow

print('---------')
print(find_mid(h))
