def twoSum(nums, target):
    pairs = {}
    for count, pair1 in enumerate(nums):
        pair2 = target-pair1
        if pair2 in pairs:
            return [count, pairs[pair2]]
        pairs[pair1] = count