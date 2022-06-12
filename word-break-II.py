class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        dp = {}

        def recursive(s):
            if s in dp:
                return dp[s]

            result = []

            for w in wordDict:
                if s[:len(w)] == w:
                    if len(w) == len(s):
                        result.append(w)
                    else:
                        tmp = recursive(s[len(w):])

                        for t in tmp:
                            result.append(w + " " + t)
            dp[s] = result
            return result

        return recursive(s)
