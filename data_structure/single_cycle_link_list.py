# -*- coding: utf-8 -*-
__author__ = 'lhy'
__date__ = '2019-09-08 15:10'


# 单链表的操作
# is_empty()
# length
# travel()遍历整个链表
# add(item)链表头部添加元素
# append(item)链表尾部添加元素
# insert(pos, item)指定位置添加元素
# remove(item)删除节点
# search(item)查找节点是否存在

class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """单向循环列表"""

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        # cur游标，用来移动遍历节点
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，cur指向尾节点
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 退出循环就是尾节点
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """链表尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            if cur.elem == item:
                # 判断头结点
                if cur == self.__head:
                    # 找到尾节点
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    # 退出循环，rear指向尾节
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾节点，但是节点的元素未打印
        if cur.elem == item:
            return True
        return False


if __name__ == '__main__':
    li = SingleCycleLinkList()
    print(li.is_empty())
    print(li.length())

    li.append(1)
    print(li.is_empty())
    print(li.length())

    li.append(2)
    li.append(8)
    li.append(4)
    li.append(5)
    li.append(6)
    # 1 2 8 4 5 6
    li.insert(-1, 9)  # 9 1 2 8 4 5 6
    li.travel()
    li.insert(2, 100)  # 1 2 100 8 4 5 6
    li.travel()
    li.insert(100, 2)  # 1 2 100 8 4 5 6 2
    li.travel()
    li.remove(100)
    li.travel()
