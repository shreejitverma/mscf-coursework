
# File:    BinaryTree_hw2.py
# Authors: [Team 6 -> 1. Atul Daluka (adaluka@andrew.cmu.edu) and 2. Shreejit Verma (shreejiv@andrew.cmu.edu)]
# Date:    [Friday - August 20, 2021]

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
        if(cur_node == None):
            return 0
        else:
            return self._size_help(cur_node._left) + self._size_help(cur_node._right) + 1
    def print_pretty(self):
        return self._print_pretty_help(self._top, 0)
    def _print_pretty_help(self, cur_node, level):
        if cur_node != None:
            self._print_pretty_help(cur_node._right, level + 1)
            print('\t' * level, cur_node._value)
            self._print_pretty_help(cur_node._left, level + 1)
    def depth(self):
        return self._depth_help(self._top)
    def _depth_help(self, cur_node):
        if(cur_node == None):
            return 0
        else:
            return max(self._depth_help(cur_node._left) + 1, self._depth_help(cur_node._right) + 1)
    def val_nodes(self):
        return self.__str__().split(" ")
    def __eq__(self, BinaryTree):
        if (BinaryTree._top == None) and ((self._top == None)):
            return True
        else:
            tree_nodes_1 = self.val_nodes()
            tree_nodes_2 = BinaryTree.val_nodes()
            return tree_nodes_2 == tree_nodes_1
    def min(self):
        return self._min_help(self._top)
    def _min_help(self, cur_node):
        if cur_node == None:
            return None;
        else:
            while(cur_node._left != None):
                cur_node = cur_node._left
            return cur_node._value
    def max(self):
        return self._max_help(self._top)
    def _max_help(self, cur_node):
        if cur_node == None:
            return None;
        else:
            while(cur_node._right != None):
                cur_node = cur_node._right
            return cur_node._value
    def mean(self):
        return self._mean_help(self._top)
    def _mean_help(self, cur_node):
        if(cur_node == None):
            return None
        else:
            return self.sum()/self.size()
    def __contains__(self, value):
        return self.__contains__help(self._top, value)
    def __contains__help(self, cur_node, value):
        while(cur_node != None):
            if value < cur_node._value:
                return self.__contains__help(cur_node._left, value)
            elif value > cur_node._value:
                return self.__contains__help(cur_node._right, value)
            else:
                return True
        return False
    # To be worked on:
    def copy(self):
        copy_tree = self
        return self.copy_help(copy_tree._top)

    def copy_help(self, cur_node):
        if cur_node._right is not None:
            copy_tree._right = self.copy_help(copy_tree, cur_node._right)
        if cur_node._left is not None:
            copy_tree._left = self.copy_help(copy_tree, cur_node._left)
        return copy_tree

    '''
    def mirror_copy(self):
        mirror = BinaryTree._BTNode(self._top)
        if self._right is not None:
            mirror._left = self._right.mirror_copy()
        if self._left is not None:
            mirror._right = self._left.mirror_copy()
        return mirror
    '''

    def negate(self):
        return self._negate_help(self._top)
    def _negate_help(self, cur_node):
        if cur_node != None:
            self._negate_help(cur_node._right, level + 1)
            print(cur_node._value)
            self._negate_help(cur_node._left, level + 1)


