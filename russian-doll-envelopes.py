n = len(envelopes)
        envelopes.sort()
        dp=[1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if dp[j]>=dp[i]:
                    if envelopes[j][0]<envelopes[i][0] and envelopes[j][1]<envelopes[i][1]:
                        dp[i]=dp[j]+1
        
        return max(dp)
