'''
Author : Hemant Rana
Date : 31st Aug 2020
link : https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lnums = len(nums)
        d = {}
        for i in range(0, lnums):
            if (nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        kd = list(d.keys())
        inf = -1
        lkd = len(kd)
        res = []

        for i in range(0, lkd):
            if (kd[i] >= 0):
                inf = i
                break

        if (inf == -1):
            return []
        elif (inf == 0):
            if (0 in d):
                if (d[0] >= 3):
                    return [[0, 0, 0]]
        else:
            tindex = inf
            diff = 0
            if (kd[inf] == 0):
                if (d[0] >= 3):
                    res.append([0, 0, 0])
                inf += 1

            for i in range(inf, lkd):
                trav={}
                for j in range(0, min(tindex, inf)):
                    if (abs(kd[j]) > kd[i]):
                        diff = abs(kd[j] + kd[i])
                    else:
                        diff = -(kd[j] + kd[i])

                    if diff not in trav:
                        # print("Here")
                        if diff == kd[j]:
                            if d[kd[j]] >= 2 :
                                res.append([diff, diff, kd[i]])
                        elif diff == kd[i]:
                            if d[kd[i]] >= 2:
                                res.append([kd[j], diff, diff])
                        else:
                            if (diff in d):
                                res.append([kd[j], kd[i], diff])
                    trav[kd[j]]=1


                # print(i,"---",d,"-----",res)
                d.pop(kd[i])


        return res
