"""
    Reorder List

    Description:
    You are given the head of a singly linked list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln

    Reorder the list to be in the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

    Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

    Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

    Constraints:
    - The number of nodes in the list is in the range [1, 5 * 10^4].
    - 1 <= Node.val <= 1000

"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle_setter = head
        middle_ensurer = head.next
        
        while middle_ensurer is not None and middle_ensurer.next is not None: 
            middle_setter = middle_setter.next
            middle_ensurer = middle_ensurer.next.next
            
        continuous_list = middle_setter.next
        disconnector_to_prevNode = middle_setter.next = None
        
        while continuous_list is not None:
            continuous_list_tracker = continuous_list.next
            continuous_list.next = disconnector_to_prevNode
            disconnector_to_prevNode = continuous_list
            continuous_list = continuous_list_tracker
        
        normal_list = head
        end_list = disconnector_to_prevNode
        
        while end_list is not None:
            continuous_normal_list = normal_list.next
            continuous_end_list = end_list.next
            
            normal_list.next = end_list
            end_list.next = continuous_normal_list
            
            normal_list = continuous_normal_list
            end_list = continuous_end_listclass Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle_setter = head
        middle_ensurer = head.next
        
        while middle_ensurer is not None and middle_ensurer.next is not None: 
            middle_setter = middle_setter.next
            middle_ensurer = middle_ensurer.next.next
            
        continuous_list = middle_setter.next
        disconnector_to_prevNode = middle_setter.next = None
        
        while continuous_list is not None:
            continuous_list_tracker = continuous_list.next
            continuous_list.next = disconnector_to_prevNode
            disconnector_to_prevNode = continuous_list
            continuous_list = continuous_list_tracker
        
        normal_list = head
        end_list = disconnector_to_prevNode
        
        while end_list is not None:
            continuous_normal_list = normal_list.next
            continuous_end_list = end_list.next
            
            normal_list.next = end_list
            end_list.next = continuous_normal_list
            
            normal_list = continuous_normal_list
            end_list = continuous_end_list
