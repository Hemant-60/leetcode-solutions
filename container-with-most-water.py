'''
Author : Hemant Rana
Date : 30th Aug 2020
link : https://leetcode.com/problems/container-with-most-water
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        h_len=len(height)
        max_area=0
        b,e=0,h_len-1
        
        while(b<e):
            area=min(height[b],height[e])*(e-b)
            max_area=max(area,max_area)
            
            if(height[b]>height[e]):
                e-=1
            else:
                b+=1
                    
        
        return max_area
