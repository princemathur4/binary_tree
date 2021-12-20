## Problem Statement:
### Counting Lesser Numbers

Paul has a set of unique numbers. He wants to store numbers in a binary tree such that
whenever a number is given, he can exactly tell how many numbers are less than the given
number.
Help Paul by coding the logic in your language of choice without using any libraries for tree
implementation.

## Solution

Using Balanced Binary search trees, 
we can recursively search for the number of nodes-values smaller than a given number,
in the best case, in O(log N) time and in the worst case O(N) time.<br>
where N=Number of nodes in the tree

## Time complexity Analysis:
    For creating the balanced binary search tree:
    ** Worst Case Time complexity **
    -> O(N * log N)
    As we are sorting the array before creating the B.S.T
    
    For running logic for fetching the number of smaller elements than a given number:
    ** Worst Case Time complexity **
    -> O(N) (where N=Number of nodes in the tree)
    If the given 'num' is >= largest number in the tree,
    then it will have to traverse the whole tree
    to individually check which number is smaller than current one

## Space complexity Analysis:
    ** Worst Case Space complexity **
     -> O(N) (for storing data as a tree) + O(N) (Recursion stack space)
     -> O(N) (where N=Number of nodes in the tree)

### Structure
- solution.py : contains the code for problem's solution
- example.py : contains a sample code to test out the solution