class Solution:
    def reorganizeString(self, s: str) -> str:

        frequencyDict = dict()

        for letter in s:
            if letter in frequencyDict:
                frequencyDict[letter] += 1
            else:
                frequencyDict[letter] = 1

        maxHeap = []
        for letter, frequency in frequencyDict.items():
            heappush(maxHeap, (-frequency, letter))

        result = []
        previousLetter = None
        previousCount = 0
        while maxHeap:
            frequency, letter = heappop(maxHeap)
            result.append(letter)
            frequency += 1
            if previousCount != 0:
                heappush(maxHeap, (previousCount, previousLetter))
            previousCount = frequency
            previousLetter = letter
        result = "".join(result)

        return result if len(result) == len(s) else ''
