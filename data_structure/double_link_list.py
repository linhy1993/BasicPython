# -*- coding: utf-8 -*-
__author__ = 'lhy'
__date__ = '2019-09-08 14:42'


class Node(object):
    """结点"""

    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
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
        node.next.prev = node

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
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < (pos):
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 判断头结点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:  # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.append(8)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    # 1 2 8 4 5 6
    dll.insert(-1, 9)  # 9 1 2 8 4 5 6
    dll.travel()
    dll.insert(2, 100)  # 1 2 100 8 4 5 6
    dll.travel()
    dll.insert(100, 2)  # 1 2 100 8 4 5 6 2
    dll.travel()
    dll.remove(100)
    dll.travel()
