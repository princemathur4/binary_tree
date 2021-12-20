class TreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_no_of_smaller_elements(self, num: int) -> int:
        """
        Returns the number of smaller elements for any given number in the tree structure
        :param num: int
        :return: int
        """
        res = 0
        if self.data is None:
            return res

        if num <= self.data:
            if self.left is not None:
                res += self.left.get_no_of_smaller_elements(num)
        elif num > self.data:
            res += 1
            if self.left is not None:
                res += (self.left.get_no_of_smaller_elements(num))
            if self.right is not None:
                res += (self.right.get_no_of_smaller_elements(num))

        return res

    def display(self):
        """
        Function to pretty0print the whole tree
        (Copied code from: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python)
        """
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BalancedBinarySearchTree:

    def __init__(self, arr):
        self.root = self.create_sub_trees(arr=sorted(arr), start=0, end=len(arr)-1)

    def create_sub_trees(self, arr, start, end):
        """
        Creates balanced binary search tree using a sorted list
        :param arr: list (sorted array)
        :param start: int (start of the array range)
        :param end: int (end of the array range)
        :return: root of the tree [TreeNode] or None
        """
        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(data=arr[mid])

        root.left = self.create_sub_trees(arr, start, mid-1)
        root.right = self.create_sub_trees(arr, mid+1, end)
        return root

    def get_no_of_smaller_elements(self, num):
        return self.root.get_no_of_smaller_elements(num=num)