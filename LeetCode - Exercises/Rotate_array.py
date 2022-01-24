'''Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
'''

def rotate_array(k, nums):
    k = k%nums
    while k>0:
        nums.insert(0, nums.pop())
        k-=1
    return nums