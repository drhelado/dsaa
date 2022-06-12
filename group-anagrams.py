class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:





        res = defaultdict(list) # mapping charCount to list of Anagrams

        # print('res start', (res))

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                # set the index of the character by taking the number for a which is the first character - number for current character
                count[ord(c) - ord("a")] += 1 # ascii value

            # print('count', (count))

            # print(tuple(count))

            # push the word to the pattern it created on the count array, each character it contains is a 1 and the rest are 0
            # any words that contain the same characters will be pushed on the same index (count), automatically grouping words
            res[tuple(count)].append(s)

            # print('res', (res))

        return res.values()
