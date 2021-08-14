
# File: BinaryTree.py
# Author(s): Shreejit Verma (shreejiv@andrew.cmu.edu), YingTu(yingt@andrew.cmu.edu)
# Date: 08/13/2021

class BinaryTree:
    class _BTNode:
        def __init__(self, value, left = None, right = None):
            self._value = value
            self._left = left
            self._right = right

    def __init__(self):
        self._top = None

    def insert(self, value):
        if self._top == None:
            self._top = BinaryTree._BTNode(value)
        else:
            self._insert_help(self._top, value)

    def _insert_help(self, cur_node, value):
        if value < cur_node._value:
            if cur_node._left == None:
                cur_node._left = BinaryTree._BTNode(value)
            else:
                self._insert_help(cur_node._left, value)
        elif value > cur_node._value:
            if cur_node._right == None:
                cur_node._right = BinaryTree._BTNode(value)
            else:
                self._insert_help(cur_node._right, value)

    def __str__(self):
        return self._str_help(self._top)

    def _str_help(self, cur_node):
        if cur_node == None:
            return '';
        else:
            left_str = self._str_help(cur_node._left)
            right_str = self._str_help(cur_node._right)
            ret = str(cur_node._value)
            if left_str:
                ret = left_str + ' ' + ret
            if right_str:
                ret = ret + ' ' + right_str
            return ret

    def sum(self):
        return self._sum_help(self._top)

    def _sum_help(self, cur_node):
        if cur_node == None:
            return 0;
        else:
            return (self._sum_help(cur_node._left)
                    + cur_node._value
                    + self._sum_help(cur_node._right))

    def size(self):
        return self._size_help(self._top)

    def _size_help(self, cur_node):
        if cur_node is None:
            return 0
        else:
            return self._size_help(cur_node._left) + 1 + self._size_help(cur_node._right)

    def print_pretty(self):
        self._print_pretty(self._top, 0)

    def _print_pretty(self, cur_node, level=0):
        if cur_node != None:
            self._print_pretty(cur_node._left, level + 1)
            print(' ' * 4 * level, cur_node._value)
            self._print_pretty(cur_node._right, level + 1)

    def depth(self):
        return self._depth(self._top)

    def _depth(self, cur_node):
        if cur_node is None:
            return 0;

        else:
            depth_l = self._depth(cur_node._left)
            depth_r= self._depth(cur_node._right)

            if (depth_l > depth_r):
                return depth_l + 1
            else:
                return depth_r + 1

    def __eq__(self, other):
        return self.__eq__help(self._top, other._top)

    def __eq__help(self, node_p, node_q):
        if not node_p and not node_q:
            return True
        if not node_p or not node_q:
            return False
        if node_p._value != node_q._value:
            return False
        return self.__eq__help(node_p._left, node_q._left) and self.__eq__help(node_p._right, node_q._right)

    def min(self):
        if self._top is None:
            return None
        return self._min(self._top)

    def _min(self, cur_node):
        if cur_node is None:
            return float('inf')
        final = cur_node._value
        left_final = self._min(cur_node._left)
        right_final = self._min(cur_node._right)
        if left_final < final:
            final = left_final
        if right_final < final:
            final = right_final
        return final

    def max(self):
        if self._top is None:
            return None
        return self._max(self._top)

    def _max(self, cur_node):
        if cur_node is None:
            return float('-inf')
        final = cur_node._value
        left_final = self._max(cur_node._left)
        right_final = self._max(cur_node._right)
        if (left_final > final):
            final = left_final
        if (right_final > final):
            final = right_final
        return final

    def mean(self):
        if self._top is None:
            return None
        return self.sum()/self.size()
'''
        if self._top is None:
            return None
        cur_node = self._top
        while cur_node._left:
            cur_node = cur_node._left
        return cur_node._value
'''




