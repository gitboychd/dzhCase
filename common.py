from functools import reduce
from typing import List
from collections import defaultdict



class Solution:
    def removeDuplicates(self,nums1,m,nums2,n):
        nums1= nums1[0:m]+nums2[0:n]
        # print(nums1[0:m])
        # print(nums2[0:n])
        nums1.sort()
        return nums1

if __name__ == "__main__":
    nums1 = [1, 2, 3,0,0,0]
    m=3
    nums2=[2,5,6]
    n=3
    print(Solution().removeDuplicates(nums1,m,nums2,n))
    nums1 = [1]
    m =1
    num2=[]
    n=0
    print(Solution().removeDuplicates(nums1,m,nums2,n))

