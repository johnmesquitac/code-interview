from signal import valid_signals
from turtle import left


'''class TreeNode(object):
    def __init__(self, val=0, lef=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

def convert_array(arr, left, right):
    if left<right:
        middle = (left+right)//2
        root = TreeNode(val = arr[middle])
        root.left = convert_array(arr, left, middle-1)
        root.rigt = convert_array(arr, middle+1, right)
        return right
    elif right==left:
        return TreeNode(val=arr[right])

def sortedArrayToBST(arr):
    root = None
    if arr>0:
        root = convert_array(arr, 0, len(arr)-1)
    return root