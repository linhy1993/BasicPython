# -*- coding: utf-8 -*-
__author__ = 'lhy'
__date__ = '2019-09-01 15:50'


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


class SingleLinkList(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        # cur游标，用来移动遍历节点
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
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
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                #判断头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    li = SingleLinkList()
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
