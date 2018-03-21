# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    #为list添加一个node
    def add(self, list, x):
        new = ListNode(x)
        t = list
        while not t.next is None:
            t = t.next
        t.next = new

    #为list添加一组node
    def append(self, list, l1):
        t = list
        while not t.next is None:
            t = t.next
        t.next = l1

    #辅助功能，输入数
    def input_number(self, l1):
        a = input()
        a = a[1:-1]
        nums = a.split(',')
        for i in nums:
            self.add(l1, i)
        return l1.next

    #辅助功能，输出数
    def print_number(self, l1):
        num = ''
        tmp = l1
        while tmp != None:
            num = num + str(tmp.val)
            tmp = tmp.next
        print(num)

    #主程序分离后的单元，用于在长度不同时判断两数应如何加
    def add_outer(self,ans,t1,pre_num):
        self.append(ans,t1)     #将ans和多余的node连接
        tmp = t1
        #判断进位
        while pre_num:
            if tmp == None:
                self.add(ans, '1')
                pre_num = 0
            else:
                this_num = int(tmp.val) + pre_num
                tmp.val = str(this_num % 10)
                pre_num = this_num // 10
                tmp = tmp.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = l1
        t2 = l2
        ans = ListNode(0)
        pre_num = 0
        while t1 != None or t2 != None:
            this_num = int(t1.val) + int(t2.val)+pre_num
            now_num = this_num % 10
            self.add(ans, now_num)
            pre_num = this_num // 10
            t1 = t1.next
            t2 = t2.next
            if not t1 and not t2 and pre_num == 1:
                self.add(ans, '1')
                break
            if not t1:
                self.add_outer(ans,t2,pre_num)
                break
            if not t2:
                self.add_outer(ans,t1, pre_num)
                break
        return ans.next


if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode(0)
    l1 = sol.input_number(l1)
    # sol.print_number(l1)
    l2 = ListNode(0)
    l2 = sol.input_number(l2)
    # sol.print_number(l2)
    ans = sol.addTwoNumbers(l1, l2)
    ans_list = []
    tmp = ans
    while tmp != None:
        ans_list.append(int(tmp.val))
        tmp = tmp.next
    print(ans_list)
