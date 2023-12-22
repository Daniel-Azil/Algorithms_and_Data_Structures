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