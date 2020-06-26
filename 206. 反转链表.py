# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 递归
        if head == None or head.next == None:
            return head

        p = self.reverseList(head.next)
        # 交换当前head 和 head.next
        head.next.next = head
        head.next = None
        return p
        '''
        #解题思路：新建一个头结点，将所有的原链表节点从头到尾逐一取下，采用头插法插入整个链表到新建节点之前，则完成了链表逆序的目的。
        new_head = None

        while head :     
            tmp = head.next      # 备份原来head节点的next地址
            head.next = new_head
            new_head = head
            head = tmp

        return new_head
        '''