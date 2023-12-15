# Reverse a Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Example 1:
### Input:
[1,2,3,4,5]

### Output:
[5,4,3,2,1]


## Example 2:
### Input:
[1,2]

### Output:
[2,1]


## Example 3:
### Input:
[]

### Output:
[]


```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currentNode = head
        lastNode = None
        
        while currentNode is not None:
            itr_tracker = currentNode.next
            currentNode.next = lastNode
            lastNode = currentNode
            currentNode = itr_tracker
        return lastNode