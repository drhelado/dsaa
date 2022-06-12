class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        def dfs(s):
            if not s:
                return 0

            if s in memo:
                return memo[s]

            words_count = 0

            for i in range(len(s)):
                cur_word = s[:i+1]

                if cur_word in wordSet:
                    if i == len(s) - 1:
                        words_count = 1
                    else:
                        rest_words_count = dfs(s[i+1:])

                        if rest_words_count > 0:
                            words_count = rest_words_count + 1
                            break

            memo[s] = words_count

            return words_count

        wordSet = set(words)

        ans = []
        memo = {}

        for word in words:
            if dfs(word) > 1:
                ans.append(word)

        return ans
