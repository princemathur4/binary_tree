import random
from solution import BalancedBinarySearchTree

l = [random.randrange(1, 50, 1) for i in range(10)]
tree = BalancedBinarySearchTree(arr=l)
tree.root.display()

random_val = random.randint(0, max(l))
no_of_smaller_elements = tree.root.get_no_of_smaller_elements(random_val)
print(f"\nNo. of elements smaller than {random_val} in the tree are: {no_of_smaller_elements}")