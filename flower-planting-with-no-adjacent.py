from collections import deque
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph =[set() for i in range(n)]
        for i in paths:
            graph[i[0]-1].add(i[1])
            graph[i[1]-1].add(i[0])
        flowers=[0 for i in range(n)]
        visited=[0 for i in range(n)]
        for j in range(n):
            if visited[j]==0:
                visited[j]=1
                q = deque()
                q.append(j+1)
                while q:
                    
                    curr=q.popleft()
                    for i in graph[curr-1]:
                        if visited[i-1]==0:
                            q.append(i)
                            visited[i-1]=1
                    taken = set()
                    for i in graph[curr-1]:
                        if flowers[i-1]!=0: taken.add(flowers[i-1])
                    for i in range(1,5):
                        if i not in taken:
                            flowers[curr-1]=i
                            break

        
        return flowers
