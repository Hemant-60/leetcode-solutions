class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def create_dict(nums1,nums2):
            d = {}
            for i in nums1:
                for j in nums2:
                    if (i+j) in d:
                        d[i+j]+=1
                    else:
                        d[i+j] = 1
            return d
        d1 = create_dict(nums1,nums2)
        d2 = create_dict(nums3,nums4)
        
        count=0
        for i in d1:
            if i*(-1) in d2:
                count+=(d1[i]*d2[-i])
        
        return count
