'''Given an array of integers nums and an integer target, return indices of the
 two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
 use the same element twice.

You can return the answer in any order.'''
from tkinter import N
from typing import List #type hinting

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} # val: index dictionary

        for pos, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], pos]
            prevMap[num] = pos
        
        return

if __name__ == "__main__":

    nums = [2,7,11,15]
    target = 9

    Solution.twoSum(nums, target)



